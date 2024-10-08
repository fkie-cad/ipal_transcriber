import transcriber.settings as settings
from transcriber.messages import IpalMessage
from transcribers.transcriber import Transcriber

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

    def __init__(self, data=None, offset=0):
        if data is None:
            data = []
        self.update(data, offset)

    def update(self, data, offset):
        i = 0
        while i < len(data):
            self.raw[offset + i] = data[i]
            i += 1

    def logic_start_addr(self):
        return (
            self.raw[3] + (self.raw[2] << 8) + (self.raw[1] << 16) + (self.raw[0] << 24)
        )

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
        0x0A: "LRD",
        0x0B: "LWR",
        0x0C: "LRW",
        0x0D: "ARMW",
        0x0E: "FRMW",
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
        0x0A: "interrogate",
        0x0B: "command",
        0x0C: "command",
        0x0D: "command",
        0x0E: "command",
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

    # Used for debugging output:
    _pkt_count = 0

    @classmethod
    def state_identifier(cls, msg, key):
        return key

    def matches_protocol(self, pkt):
        return "ECAT" in pkt or "EtherCat" in pkt

    def parse_packet(self, pkt):  # noqa: C901
        self._pkt_count += 1
        res = []

        src = pkt["eth"].src
        dest = pkt["eth"].dst

        # Not good error handling, but these assumptions should hold for our pcaps:
        assert pkt.get_multiple_layers("eth")[0].type == "0x88a4"
        assert pkt["ecatf"].type == "0x0001"

        #
        # Iterate over PDUs
        #

        assert len(pkt.get_multiple_layers("ecat")) == 1
        pdu_layer = pkt.get_multiple_layers("ecat")[0]
        pdu_count = 1
        data_field_indices = (
            {}
        )  # Stores the index for the next PDU with a field of a given name.
        while hasattr(pdu_layer, f"sub{str(pdu_count)}_cmd"):
            pdu_prefix = f"sub{str(pdu_count)}_"
            command_value = int(pdu_layer.get_field(f"{pdu_prefix}cmd"), 16)

            # Parse addresses
            adr = None
            adp = None
            ado = None
            if command_value in [0x0A, 0x0B, 0x0C]:
                adr = int(pdu_layer.get_field(f"{pdu_prefix}lad"), 16)
            else:
                adp = int(pdu_layer.get_field(f"{pdu_prefix}adp"), 16)
                ado = int(pdu_layer.get_field(f"{pdu_prefix}ado"), 16)

            #
            # Get or reconstruct data fields:
            #
            if command_value in [0x00, 0x01, 0x04, 0x07, 0x0A]:
                # For read PDUs we don't need the data.
                data_array = []

            elif ado == 0x130:
                pass  # First address of "special" PDUs
                # TODO: fix special case
                data_array = []

            elif ado == 0x101:
                if pdu_count > 1 or pdu_layer.get_field("sub2_cmd") is not None:
                    # DEBUG
                    settings.logger.debug(
                        f"Multiple special PDUs for case ado == 0x101 in packet {str(self._pkt_count)}! Better implementation needed."
                    )
                    # TODO: We should do this the same way as we did for
                    # reg_physaddr, because that supports multiple PDUs of same
                    # type in one packet.
                data_array = [int(pdu_layer._all_fields["ecat.reg.dlcrtl2"], 16)]

            elif ado == 0x130:
                if pdu_count > 1 or pdu_layer.get_field("sub2_cmd") is not None:
                    # DEBUG
                    settings.logger.debug(
                        f"Multiple special PDUs for case ado == 0x130 in packet {str(self._pkt_count)}! Better implementation needed."
                    )
                    # TODO: We should do this the same way as we did for
                    # reg_physaddr, because that supports multiple PDUs of same
                    # type in one packet.
                alstatus_data = pdu_layer._all_fields["ecat.get.alstatus"]
                assert alstatus_data == 6
                data_array = [int(alstatus_data[4:6], 16), int(alstatus_data[2:4], 16)]

            elif ado is not None and 0x300 <= ado <= 0x307:
                data_array = []
                reg_offset = ado - 0x300

                if reg_offset % 2 == 1:
                    field_name = f"ecat.reg.crc{str((reg_offset - 1) / 2)}.rx"
                    if field_name not in data_field_indices:
                        data_field_indices[field_name] = 0
                    data_array.append(
                        int(
                            pdu_layer.get_field(field_name)
                            .fields[data_field_indices[field_name]]
                            .raw_value,
                            16,
                        )
                    )
                    data_field_indices[field_name] += 1
                    port = (reg_offset + 1) / 2
                else:
                    port = reg_offset / 2

                while port < 4 and f"ecat.reg.crc{str(port)}" in pdu_layer._all_fields:
                    field_name = f"ecat.reg.crc{str(port)}.frame"
                    if field_name not in data_field_indices:
                        data_field_indices[field_name] = 0
                    data_array.append(
                        int(
                            pdu_layer.get_field(field_name)
                            .fields[data_field_indices[field_name]]
                            .raw_value,
                            16,
                        )
                    )
                    data_field_indices[field_name] += 1

                    field_name = f"ecat.reg.crc{str(port)}.rx"
                    if field_name not in data_field_indices:
                        data_field_indices[field_name] = 0
                    data_array.append(
                        int(
                            pdu_layer.get_field(field_name)
                            .fields[data_field_indices[field_name]]
                            .raw_value,
                            16,
                        )
                    )
                    data_field_indices[field_name] += 1

            elif ado == 0x0102:
                if pdu_count > 1 or pdu_layer.get_field("sub2_cmd") is not None:
                    # DEBUG
                    settings.logger.debug(
                        f"Multiple special PDUs for case ado == 0x102 in packet {str(self._pkt_count)}! Better implementation needed."
                    )
                    # TODO: We should do this the same way as we did for
                    # reg_physaddr, because that supports multiple PDUs of same
                    # type in one packet.
                assert pdu_layer.get_field("ecat.subframe.length") == "1"
                data_array = [int(pdu_layer.get_field("ecat.reg.dlctrl3"), 16)]

            elif ado == 0x0010:
                # We assume, that 0x10 and 0x11 are allways changed together, so the len field should be set to 2.
                if "reg_physaddr" not in data_field_indices:
                    data_field_indices["reg_physaddr"] = 0
                field = pdu_layer.get_field("reg_physaddr").fields[
                    data_field_indices["reg_physaddr"]
                ]
                data_field_indices["reg_physaddr"] += 1
                data_array = [field.hex_value >> 8, field.hex_value & 0xFF]

            elif ado == 0x0502:
                # We assume, that ADO 0x502 to 0x508 are allways changed together, so the len field should be set to 6.
                if "" not in data_field_indices:
                    data_field_indices["reg_physaddr"] = 0
                field = pdu_layer.get_field("reg_physaddr").fields[
                    data_field_indices["reg_physaddr"]
                ]
                data_field_indices["reg_physaddr"] += 1
                data_array = [field.hex_value >> 8, field.hex_value & 0xFF]

            elif ado == 0x800:
                # We assume, that ADO 0x502 to 0x508 are allways changed together, so the len field should be set to 6.
                if "" not in data_field_indices:
                    data_field_indices["syncman"] = 0
                field = pdu_layer.get_field("syncman").fields[
                    data_field_indices["syncman"]
                ]
                data_field_indices["syncman"] += 1
                data_array = list(bytes.fromhex(field.raw_value))

            else:
                data_str = pdu_layer.get_field(f"{pdu_prefix}data")
                if data_str:
                    data_array = self.data_string_to_bytes(data_str)
                else:
                    # DEBUG
                    settings.logger.debug(
                        f"Missing data attribute for PDU {str(self._pkt_count)},{str(pdu_count)}"
                    )
                    settings.logger.debug("ado", ado)
                    settings.logger.debug("sub_ado", pdu_layer.get_field("sub1_ado"))
                    settings.logger.debug("cmd_value", command_value)
                    data_array = []

            # Calculate value of msg.length
            pdu_length = 12 + len(data_array)

            #
            # Parse data
            #

            # We first parse the data to the following format:
            # parsed_data is a dict, that maps slave_addr to another dict D.
            # D maps memory addresses of this slave to their new values.
            # slave_addr is either an auto-increment address of the form
            # (AUTO_INCR_ADDR, <value>) or a config address of the form
            # (CONFIG_ADDR, <value>). <value> should be a hex string.
            # The memory addresses should be given as integers.
            # EXCEPTION: If slave_addr is of the form (LOGICAL_ADDR, <addr>)
            # parsed_data[<slave_addr>] is the updated memory value at the given
            # address as an int, because logical addresses combine the slave and
            # the memory address.
            parsed_data = {}

            # For NOP or reading PDUs we store no data:
            if command_value in [
                0x00,
                0x01,
                0x04,
                0x07,
                0x0A,
            ]:  # NOP, APRD, FPRD, BRD, LRD
                pass

            # Data should be set in the same way for WR and RW. We only look
            # at writes anyway.
            elif command_value in [0x02, 0x03]:  # APWR, APRW
                memory_map = {}
                offset = ado
                for i in range(len(data_array)):
                    memory_map[offset + i] = data_array[i]
                parsed_data[(AUTO_INCR_ADDR, f"{adp:#06x}")] = memory_map

            elif command_value in [0x05, 0x06]:  # FPWR, FPRW
                memory_map = {}
                offset = ado
                for i in range(len(data_array)):
                    memory_map[offset + i] = data_array[i]
                parsed_data[(CONFIG_ADDR, f"{adp:#06x}")] = memory_map

            elif command_value in [0x08, 0x09]:  # BWR, BRW
                memory_map = {}
                offset = ado
                for i in range(len(data_array)):
                    memory_map[offset + i] = data_array[i]
                parsed_data[(BROADCAST_ADDR, "*")] = memory_map

            elif command_value in [0x0B, 0x0C]:  # LWR, LRW
                i = 0
                while i < len(data_array):
                    addr = self.match_logic_addr(adr + i)
                    if addr is None:
                        parsed_data[(LOGICAL_ADDR, f"{adr:#010x}")] = data_array[i]
                    else:
                        if not addr[0] in parsed_data:
                            parsed_data[addr[0]] = {}
                        parsed_data[addr[0]][addr[1]] = data_array[i]
                    i += 1

            elif command_value == 0x0D:  # ARMW
                assert False, "Do we even have these in our Pcaps?"
            elif command_value == 0x0E:  # FRMW
                assert False, "Do we even have these in our Pcaps?"
            else:
                assert False, "Unknown condition"

            #
            # Update the address maps
            #
            # We do not look at mem_updates to logical addresses, because we
            # don't know the memory address it should be mapped to.
            for slave, mem_update in filter(
                lambda x: x[0][0] != LOGICAL_ADDR, parsed_data.items()
            ):
                # 0x10 and 0x11 contain the configured address.
                assert (0x10 in mem_update and 0x11 in mem_update) or (
                    0x10 not in mem_update and 0x11 not in mem_update
                )
                if 0x10 in mem_update:
                    self.update_config_addr(slave, mem_update)

                # 0x600 to 0x6ff contain the FMMUs with logic memory maps.
                if any(map(lambda a: 0x600 <= a <= 0x6FF, mem_update.keys())):
                    self.update_FMMU(slave, mem_update)

            #
            # Construct the data attribute of the IPAL message from parsed_data
            #
            data = {}
            for slave, mem_update in parsed_data.items():
                if slave[0] == LOGICAL_ADDR:
                    slave_mem_addr = f"log_{slave[1]}"
                    assert type(mem_update) is int
                    data[slave_mem_addr] = mem_update
                    continue

                for mem_addr_int, value in mem_update.items():
                    # Convert int to hex str:
                    mem_addr_str = f"{mem_addr_int:#06x}"

                    if slave[0] == AUTO_INCR_ADDR:
                        slave_mem_addr = f"aic_{slave[1]}/{mem_addr_str}"
                    elif slave[0] == CONFIG_ADDR:
                        if slave[1] in self._config_addr_map:
                            slave_mem_addr = (
                                f"aic_{self._config_addr_map[slave[1]]}/{mem_addr_str}"
                            )
                        else:
                            slave_mem_addr = f"phy_{slave[1]}/{mem_addr_str}"

                    elif slave[0] == BROADCAST_ADDR:
                        slave_mem_addr = f"*/{mem_addr_str}"

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

            pdu_count += 1

        return res

    def match_response(self, requests, response):
        remove_from_queue = []
        return remove_from_queue

    def get_ado_adp_address(self, i, ecat):
        ado = ecat.get(f"sub{str(i + 1)}_ado")
        adp = ecat.get(f"sub{str(i + 1)}_adp")
        current_address = f"Ado: {str(ado)} Adp: {str(adp)}"
        return current_address

    @staticmethod
    def data_string_to_bytes(string_data):
        res = []
        for b in string_data.split(":"):
            res.append(int(b, 16))
        return res

    # Updates the saved configured address for the given slave in the
    # config_addr -> auto_incr_addr mapping (self._config_addr_map).
    # Assumes, that memory_update contains a memory address in the address
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
            settings.logger.warning(
                "Changed (Reset?) configured address with boadcast."
            )
            self._config_addr_map = {}
        elif slave[0] == LOGICAL_ADDR:
            raise AssertionError
            # We got a configured address update for an unknown logical address.

        else:
            raise AssertionError
            # We have an unexpected address type

        # Update FMMU map:
        if (CONFIG_ADDR, new_addr) in self._fmmu_entities_map:
            self._fmmu_entities_map[
                (AUTO_INCR_ADDR, self._config_addr_map[new_addr])
            ] = self._fmmu_entities_map[(CONFIG_ADDR, new_addr)]
            # Maybe we should also remove the old mapping in this case

    # Updates the FMMU for the given slave in self._fmmu_entities_map.
    # Assumes, that memory_update contains a memory address in the address
    # space of the FMMU.
    # slave should be an address of the form (<ADDR_KIND>, <address>).
    def update_FMMU(self, slave, mem_update):
        if slave[0] == AUTO_INCR_ADDR:
            slave_addr_resolved = slave
        elif slave[0] == BROADCAST_ADDR:
            slave_addr_resolved = slave
        elif slave[0] == CONFIG_ADDR and slave in self._config_addr_map:
            slave_addr_resolved = (AUTO_INCR_ADDR, self._config_addr_map[slave[1]])
        elif slave[0] == CONFIG_ADDR:
            slave_addr_resolved = slave
        elif slave[0] == LOGICAL_ADDR:
            raise AssertionError
            # We got a FMMU update for an unknown logical address.
        else:
            settings.logger.error(slave)
            raise AssertionError
            # We have an unexpected address type

        # If this is the first FMMU change for this slave, insert empty FMMU map:
        if slave_addr_resolved not in self._fmmu_entities_map:
            self._fmmu_entities_map[slave_addr_resolved] = {}

        # Group the mem_addr, value pairs to mem_offset, [values] pairs:
        groups = []  # Contains (<group_offset>, <group_data>)
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
            update_offset = groups[i][
                0
            ]  # Offset of first byte in update_data to FMMU_OFFSET
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
                self._fmmu_entities_map[slave_addr_resolved][entity_offset].update(
                    update_data, update_entity_offset
                )
            else:
                self._fmmu_entities_map[slave_addr_resolved][entity_offset] = (
                    FMMUEntity(data=update_data, offset=update_entity_offset)
                )

    # Returns the auto-increment address or if that is not known the configured
    # address of the slave and the memory offset corresponding to the given
    # logical address and the FMMUs saved in self._fmmu_entities_map.
    # The returned value has the form ((<ADDR_KIND>, <slave_addr>), <memory_address>).
    # If the given logical address cannot be mapped to a slave, None is
    # returned.
    def match_logic_addr(self, addr):
        for slave_addr, fmmu_map in self._fmmu_entities_map.items():
            for fmmu_entity in fmmu_map.values():
                if (
                    fmmu_entity.logic_start_addr()
                    <= addr
                    < fmmu_entity.logic_start_addr() + fmmu_entity.mapping_length()
                ):
                    phys_addr = fmmu_entity.phys_start_addr() + (
                        addr - fmmu_entity.logic_start_addr()
                    )
                    return slave_addr, phys_addr
        return None
