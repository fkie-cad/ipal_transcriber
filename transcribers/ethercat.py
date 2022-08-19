from transcriber.messages import IpalMessage, Activity
from transcribers.transcriber import Transcriber
import transcriber.settings as settings


AUTO_INCR_ADDR = 0
PHYS_ADDR = 1


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
    # Maps physical addresses to auto-increment addresses
    # Both addresses should be strings.
    _physical_addr_map = {}

    @classmethod
    def state_identifier(cls, msg, key):
        # TODO: add state_identifier
        pass

    def matches_protocol(self, pkt):
        return "ECAT" in pkt or "EtherCat" in pkt


    def parse_packet(self, pkt):
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
            # (AUTO_INCR_ADDR, <value>) or a physical address of the form
            # (PHYS_ADDR, <value>). <value> should be a hex string.
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
                        self._physical_addr_map[new_addr] = slave[1]
                    elif slave[0] == PHYS_ADDR:
                        self._physical_addr_map[new_addr] = self._physical_addr_map[slave[1]]
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
                    elif slave[0] == PHYS_ADDR:
                        if slave[1] in self._physical_addr_map:
                            slave_mem_addr = "aic_" + self._physical_addr_map[slave[1]] + "/" + mem_addr_str
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
