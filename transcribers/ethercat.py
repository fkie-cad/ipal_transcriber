from pyshark.packet.packet import Packet as PysharkPacket
from scapy.packet import Packet as ScapyPacket

from transcriber.messages import IpalMessage, Activity
from transcribers.transcriber import Transcriber
import transcriber.settings as settings


AUTO_INCR_ADDR = 0
CONFIG_ADDR = 1
BROADCAST_ADDR = 2
LOGICAL_ADDR = 3

FMMU_OFFSET = 0x600
FMMU_ENTITY_NUMBER = 16
FMMU_ENTITY_LENGTH = 16
FMMU_END = FMMU_OFFSET + FMMU_ENTITY_NUMBER * FMMU_ENTITY_LENGTH


class FMMUEntity:
    raw = [0] * 16

    def __init__(self, data=[], offset=0):
        self.update(data, offset)

    def update(self, data, offset):
        i = 0
        while i < len(data):
            self.raw[offset + i] = data[i]
            i += 1


    def logic_start_addr(self):
        return self.raw[3] + (self.raw[2] << 8) + (self.raw[1] << 16) + (self.raw[0] << 24)

    def mapping_length(self):
        return self.raw[5] + (self.raw[4] << 8)

    def phys_start_addr(self):
        return self.raw[9] + (self.raw[8] << 8)

    def enabled(self):
        return self.raw[0xC] & 0x1 == 1


class EtherCatTranscriber(Transcriber):
    _name = "ethercat"
    _cmd_value_map = {
        0x00: "NOP",
        0x01: "APRD",
        0x02: "APWR",
        0x03: "APRW",
        0x04: "FPRD",
        0x05: "FPWR",
        0x06: "FPRW",
        0x07: "BRD",
        0x08: "BWR",
        0x09: "BRW",
        0x0a: "LRD",
        0x0b: "LWR",
        0x0c: "LRW",
        0x0d: "ARMW",
        0x0e: "FRMW",
    }
    _activity_map = {
        0x00: "inform",
        0x01: "interrogate",
        0x02: "command",
        0x03: "command",
        0x04: "interrogate",
        0x05: "command",
        0x06: "command",
        0x07: "interrogate",
        0x08: "command",
        0x09: "command",
        0x0a: "interrogate",
        0x0b: "command",
        0x0c: "command",
        0x0d: "command",
        0x0e: "command",
    }
    # Maps configured addresses to auto-increment addresses
    # Both addresses should be strings.
    _config_addr_map = {}

    # Stores the FMMUs of all slaves.
    # The map maps slave addresses to FMMUs.
    # FMMUs are saved as maps from entity memory offset to FMMUEntity.
    # If the corresponding auto-increment address is unknown, configured
    # addresses can be uses as (CONFIG_ADDR, <addr>). As soon as the auto-
    # increment address of this slave is known, its FMMU should be moved to the
    # key (AUTO_INCR_ADDR, <addr>).
    _fmmu_entities_map = {}


    @classmethod
    def state_identifier(cls, msg, key):
        return key

    def matches_protocol(self, pkt):
        return "ECAT" in pkt or "EtherCat" in pkt

    def parse_packet(self, pkt):
        if isinstance(pkt, PysharkPacket):
            return self.parse_packet_pyshark(pkt)
        elif isinstance(pkt, ScapyPacket):
            return self.parse_packet_scapy(pkt)
        else:
            print("Packet with unexpected type.")
            return []

    def parse_packet_pyshark(self, pkt):
        res = []

        src = pkt["eth"].src
        dest = pkt["eth"].dst

        # Not good error handling, but these assumptions should hold for our pcaps:
        assert len(pkt.get_multiple_layers("ecatf")) == 1
        assert len(pkt.get_multiple_layers("ecat")) == 1
        assert int(pkt.get_multiple_layers("ecatf")[0].type, 16) == 0x0001

        ecat_layer = pkt.get_multiple_layers("ecat")[0]

        #
        # Iterate over PDUs
        #

        total_length = int(pkt.get_multiple_layers("ecatf")[0].length, 16) # Length of all PDUs combined
        offset = 0
        pdu_count = 0
        #while offset < total_length:
        while f"sub{pdu_count + 1}_cmd" in ecat_layer.field_names:
            pdu_count += 1

            command_value = int(ecat_layer.get_field(f"sub{pdu_count}_cmd"), 16)

            # Calculate value of msg.length
            # TODO: This is obviously still false. The correct value depends on the command and length field (length of data field)
            match command_value:
                case 0x00: # NOP
                    pdu_length = 12 + len(self.data_string_to_bytes(ecat_layer.get_field(f"sub{pdu_count}_data")))
                case 0x01: # APRD
                    pdu_length = 0
                    #pdu_length = 12 + data_length
                case 0x02: # APWR
                    pdu_length = 0
                    #pdu_length = 12 + data_length
                case 0x03: # APRW
                    pdu_length = 0
                case 0x04: # FPRD
                    pdu_length = 0
                    #pdu_length = 12 + data_length
                case 0x05: # FPWR
                    pdu_length = 0
                case 0x06: # FPRW
                    pdu_length = 0
                case 0x07: # BRD
                    pdu_length = 0
                    #pdu_length = 12 + data_length
                case 0x08: # BWR
                    pdu_length = 0
                    #pdu_length = 12 + data_length
                case 0x09: # BRW
                    pdu_length = 0
                case 0x0a: # LRD
                    pdu_length = 0
                    #pdu_length = 12 + data_length
                case 0x0b: # LWR
                    pdu_length = 0
                case 0x0c: # LRW
                    pdu_length = 0
                case 0x0d: # ARMW
                    pdu_length = 0
                case 0x0e: # FRMW
                    pdu_length = 0

            #
            # Parse data
            #

            # We first parse the data to the following format:
            # parsed_data is a dict, that maps slave_addr to another dict D.
            # D maps memory addresses of this slave to their new values.
            # slave_addr is either a auto-increment address of the form
            # (AUTO_INCR_ADDR, <value>) or a configured address of the form
            # (CONFIG_ADDR, <value>). <value> should be a hex string.
            # The memory addresses should be given as integers.
            parsed_data = {}

            match command_value:
                case 0x00: # NOP
                    pass
                case 0x01: # APRD
                    pass
                case 0x02: # APWR
                    pass
                case 0x03: # APRW
                    pass
                case 0x04: # FPRD
                    pass
                case 0x05: # FPWR
                    pass
                case 0x06: # FPRW
                    pass
                case 0x07: # BRD
                    pass
                case 0x08: # BWR
                    pass
                case 0x09: # BRW
                    pass
                case 0x0a: # LRD
                    pass
                case 0x0b: # LWR
                    pass
                case 0x0c: # LRW
                    pass
                case 0x0d: # ARMW
                    pass
                case 0x0e: # FRMW
                    pass

            #
            # Update the address maps
            #
            for slave, mem_update in parsed_data:
                assert (0x10 in mem_update and 0x11 in mem_update) or (not 0x10 in mem_update and not 0x11 in mem_update)
                if 0x10 in mem_update:
                    new_addr = mem_update[0x10] + (mem_update[0x11] << 8)
                    if slave[0] == AUTO_INCR_ADDR:
                        self._config_addr_map[new_addr] = slave[1]
                    elif slave[0] == CONFIG_ADDR:
                        self._config_addr_map[new_addr] = self._config_addr_map[slave[1]]
                        # Maybe we should also remove the old mapping in this case
                    else:
                        raise AssertionError
                        # We have an unexpected address type


            #
            # Construct the data attribute of the IPAL message from parsed_data
            #
            data = {}
            for slave, mem_update in parsed_data:
                for mem_addr_int, value in mem_update:
                    # Convert int to hex str:
                    mem_addr_str = "{0:#06x}".format(mem_addr_int)

                    if slave[0] == AUTO_INCR_ADDR:
                        slave_mem_addr = "aic_" + slave[1] + "/" + mem_addr_str
                    elif slave[0] == CONFIG_ADDR:
                        if slave[1] in self._config_addr_map:
                            slave_mem_addr = "aic_" + self._config_addr_map[slave[1]] + "/" + mem_addr_str
                        else:
                            slave_mem_addr = "phy_" + slave[1] + "/" + mem_addr_str
                    data[slave_mem_addr] = value


            m = IpalMessage(
                id=self._id_counter.get_next_id(),
                src=src,
                dest=dest,
                timestamp=float(pkt.sniff_time.timestamp()),
                protocol=self._name,
                length=pdu_length,
                type=command_value,
                activity=self._activity_map[command_value],
                data=data,
            )
            res.append(m)


        return res


    def parse_packet_scapy(self, pkt):
        res = []

        src = pkt.src
        dest = pkt.dst

        # Not good error handling, but these assumptions should hold for our pcaps:
        assert pkt.type == 0x88a4
        assert pkt["EtherCat"].type == 1

        #
        # Iterate over PDUs
        #

        current_pdu = pkt["EtherCat"].payload
        while True:
            command_value = current_pdu._cmd

            # Calculate value of msg.length
            assert hasattr(current_pdu, "len")
            assert hasattr(current_pdu, "data")
            pdu_length = 12 + current_pdu.len

            #
            # Parse data
            #

            # We first parse the data to the following format:
            # parsed_data is a dict, that maps slave_addr to another dict D.
            # D maps memory addresses of this slave to their new values.
            # slave_addr is either a auto-increment address of the form
            # (AUTO_INCR_ADDR, <value>) or a config address of the form
            # (CONFIG_ADDR, <value>). <value> should be a hex string.
            # The memory addresses should be given as integers.
            # EXCEPTION: If slave_addr is of the form (LOGICAL_ADDR, <addr>)
            # parsed_data[<slave_addr>] is the updated memory value at the given
            # address as an int, because logical addresses combine the slave and
            # the memory address.
            parsed_data = {}

            match command_value:
                # For NOP or reading PDUs we store no data:
                case 0x00 | 0x01 | 0x04 | 0x07 | 0x0a: # NOP, APRD, FPRD, BRD, LRD
                    pass
                # Data should be set in the same way for WR and RW. We only look
                # at writes anyway.
                case 0x02 | 0x03: # APWR, APRW
                    memory_map = {}
                    offset = current_pdu.ado
                    for i in range(current_pdu.len):
                        memory_map[offset + i] = current_pdu.data[i]
                    parsed_data[(AUTO_INCR_ADDR, "{0:#06x}".format(current_pdu.adp))] = memory_map

                case 0x05 | 0x06: # FPWR, FPRW
                    memory_map = {}
                    offset = current_pdu.ado
                    for i in range(current_pdu.len):
                        memory_map[offset + i] = current_pdu.data[i]
                    parsed_data[(CONFIG_ADDR, "{0:#06x}".format(current_pdu.adp))] = memory_map

                case 0x08 | 0x09: # BWR, BRW
                    memory_map = {}
                    offset = current_pdu.ado
                    for i in range(current_pdu.len):
                        memory_map[offset + i] = current_pdu.data[i]
                    parsed_data[(BROADCAST_ADDR, "*")] = memory_map

                case 0x0b | 0x0c: # LWR, LRW
                    i = 0
                    while i < current_pdu.len:
                        addr = self.match_logic_addr(current_pdu.adr + i)
                        if addr == None:
                            parsed_data[(LOGICAL_ADDR, "{0:#010x}".format(current_pdu.adr))] = current_pdu.data[i]
                        else:
                            if not addr[0] in parsed_data:
                                parsed_data[addr[0]] = {}
                            parsed_data[addr[0]][addr[1]] = current_pdu.data[i]
                        i += 1


                case 0x0d: # ARMW
                    assert False, "Do we even have these in our Pcaps?"
                case 0x0e: # FRMW
                    assert False, "Do we even have these in our Pcaps?"

            #
            # Update the address maps
            #
            # We do not look at mem_updates to logical addresses, because we
            # don't know the memory address it should be mapped to.
            for slave, mem_update in filter(lambda x: x[0][0] != LOGICAL_ADDR, parsed_data.items()):
                # 0x10 and 0x11 contain the configured address.
                assert (0x10 in mem_update and 0x11 in mem_update) or (not 0x10 in mem_update and not 0x11 in mem_update)
                if 0x10 in mem_update:
                    self.update_config_addr(slave, mem_update)

                # 0x600 to 0x6ff contain the FMMUs with logic memory maps.
                if any(map(lambda a: a >= 0x600 and a <= 0x6ff, mem_update.keys())):
                    self.update_FMMU(slave, mem_update)


            #
            # Construct the data attribute of the IPAL message from parsed_data
            #
            data = {}
            for slave, mem_update in parsed_data.items():
                if slave[0] == LOGICAL_ADDR:
                    slave_mem_addr = "log_" + slave[1]
                    assert type(mem_update) == int
                    data[slave_mem_addr] = mem_update
                    continue

                for mem_addr_int, value in mem_update.items():
                    # Convert int to hex str:
                    mem_addr_str = "{0:#06x}".format(mem_addr_int)

                    if slave[0] == AUTO_INCR_ADDR:
                        slave_mem_addr = "aic_" + slave[1] + "/" + mem_addr_str
                    elif slave[0] == CONFIG_ADDR:
                        if slave[1] in self._config_addr_map:
                            slave_mem_addr = "aic_" + self._config_addr_map[slave[1]] + "/" + mem_addr_str
                        else:
                            slave_mem_addr = "phy_" + slave[1] + "/" + mem_addr_str

                    elif slave[0] == BROADCAST_ADDR:
                        slave_mem_addr = "*/" + mem_addr_str

                    data[slave_mem_addr] = value


            m = IpalMessage(
                id=self._id_counter.get_next_id(),
                src=src,
                dest=dest,
                timestamp=float(pkt.time),
                protocol=self._name,
                length=pdu_length,
                type=command_value,
                activity=self._activity_map[command_value],
                data=data,
            )
            res.append(m)

            if current_pdu.next == 0:
                break
            else:
                current_pdu = current_pdu.payload

        return res


    def match_response(self, requests, response):
        remove_from_queue = []
        return remove_from_queue

    def get_ado_adp_address(self, i, ecat):
        ado = ecat.get("sub" + str(i +1) + "_ado")
        adp = ecat.get("sub" + str(i +1) + "_adp" )
        current_address = "Ado: " + str(ado) + " Adp: " + str(adp)
        return current_address

    @staticmethod
    def data_string_to_bytes(string_data):
        res = []
        for b in string_data.split(":"):
            res.append(int(b, 16))
        return res

    # Updates the saved configured address for the given slave in the
    # config_addr -> auto_incr_addr mapping (self._config_addr_map).
    # Assumes, that memory_update contains an memory address in the address
    # space of the FMMU.
    # slave should be an address of the form (<ADDR_KIND>, <address>).
    def update_config_addr(self, slave, mem_update):
        new_addr = mem_update[0x10] + (mem_update[0x11] << 8)
        if slave[0] == AUTO_INCR_ADDR:
            self._config_addr_map[new_addr] = slave[1]
        elif slave[0] == CONFIG_ADDR:
            self._config_addr_map[new_addr] = self._config_addr_map[slave[1]]
            # Maybe we should also remove the old mapping in this case
        elif slave[0] == BROADCAST_ADDR:
            print("Changed (Reset?) configured address with boadcast.")
            self._config_addr_map = {}
        elif slave[0] == LOGICAL_ADDR:
            raise AssertionError
            # We got a configured address update for an unknown logical address.

        else:
            raise AssertionError
            # We have an unexpected address type

        # Update FMMU map:
        if (CONFIG_ADDR, new_addr) in self._fmmu_entities_map:
            self._fmmu_entities_map[(AUTO_INCR_ADDR, self._config_addr_map[new_addr])] = self._fmmu_entities_map[(CONFIG_ADDR, new_addr)]
            # Maybe we should also remove the old mapping in this case


    # Updates the FMMU for the given slave in self._fmmu_entities_map.
    # Assumes, that memory_update contains an memory address in the address
    # space of the FMMU.
    # slave should be an address of the form (<ADDR_KIND>, <address>).
    def update_FMMU(self, slave, mem_update):
        if slave[0] == AUTO_INCR_ADDR:
            slave_addr_resolved = slave
        if slave[0] == BROADCAST_ADDR:
            slave_addr_resolved = slave
        elif slave[0] == CONFIG_ADDR and slave in self._config_addr_map:
            slave_addr_resolved = (AUTO_INCR_ADDR, self._config_addr_map[slave[1]])
        elif slave[0] == CONFIG_ADDR:
            slave_addr_resolved = slave
        elif slave[0] == LOGICAL_ADDR:
            raise AssertionError
            # We got a FMMU update for an unknown logical address.
        else:
            print(slave)
            raise AssertionError
            # We have an unexpected address type

        # If this is the first FMMU change for this slave, insert empty FMMU map:
        if not slave_addr_resolved in self._fmmu_entities_map:
            self._fmmu_entities_map[slave_addr_resolved] = {}

        # Group the mem_addr, value pairs to mem_offset, [values] pairs:
        groups = [] # Contains (<group_offset>, <group_data>)
        group_offset = FMMU_OFFSET
        while group_offset < FMMU_END:
            if group_offset in mem_update:
                group = []
                i = group_offset
                while i in mem_update:
                    group.append(mem_update[group_offset])
                    i += 1
                groups.append((group_offset, group))
                group_offset = i
            else:
                group_offset += 1

        i = 0
        while i < len(groups):
            update_offset = groups[i][0] # Offset of first byte in update_data to FMMU_OFFSET
            update_data = groups[i][1]
            i += 1
            # Determine offset of the changed FMMU entity:
            entity_offset = FMMU_OFFSET
            while entity_offset + FMMU_ENTITY_LENGTH <= update_offset:
                entity_offset += 1
            entity_end = entity_offset + FMMU_ENTITY_LENGTH
            # If the update_data is longer than the entity, we work on
            # remaining data in a following run of the while loop:
            if entity_end < update_offset + len(update_data):
                update_data_len = entity_end - update_offset
                groups.append((entity_end, update_data[update_data_len:]))
                update_data = update_data[:update_data_len]

            # Save FMMU update for one updated memory area:
            update_entity_offset = update_offset - entity_offset
            if entity_offset in self._fmmu_entities_map[slave_addr_resolved]:
                self._fmmu_entities_map[slave_addr_resolved][entity_offset].update(update_data, update_entity_offset)
            else:
                self._fmmu_entities_map[slave_addr_resolved][entity_offset] = FMMUEntity(data=update_data, offset=update_entity_offset)


    # Returns the auto-increment address or if that is not known the configured
    # address of the slave and the memory offset corresponding to the given
    # logical address and the FMMUs saved in self._fmmu_entities_map.
    # The returned value has the form ((<ADDR_KIND>, <slave_addr>), <memory_address>).
    # If the given logical address cannot be mapped to a slave, None is
    # returned.
    def match_logic_addr(self, addr):
        for slave_addr, fmmu_map in self._fmmu_entities_map.items():
            for fmmu_entity in fmmu_map.values():
                if addr >= fmmu_entity.logic_start_addr() and addr < fmmu_entity.logic_start_addr() + fmmu_entity.mapping_length():
                    phys_addr = fmmu_entity.phys_start_addr() + (addr - fmmu_entity.logic_start_addr())
                    return (slave_addr, phys_addr)
        return None
