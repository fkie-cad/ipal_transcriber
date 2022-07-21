from transcriber.messages import IpalMessage, Activity
from transcribers.transcriber import Transcriber
import transcriber.settings as settings


class EtherCatTranscriber(Transcriber):
    _name = "ethercat"

    @classmethod
    def state_identifier(cls, msg, key):
        # TODO: add state_identifier
        pass

    def matches_protocol(self, pkt):
        return "ECAT" in pkt

    def parse_packet(self, pkt):
        res = []
        data = {}
        src = pkt["eth"].src
        dest = pkt["eth"].dst

        ecatf_layers = pkt.get_multiple_layers("ecatf")
        ecat_layers = pkt.get_multiple_layers("ecat")

        for i in range(len(ecatf_layers)):
            ecatf = ecatf_layers[i]
            ecat = ecat_layers[i]

            cmd = ecat.cmd
            msg_length = int(ecatf.length, 16) - 2

            sub_frs = list(filter(lambda x: "sub" in x, ecat.field_names))
            sub_cmds = list(filter(lambda x: "cmd" in x, sub_frs))
            sub_idx = list(filter(lambda x: "idx" in x, sub_frs))
            sub_adp = list(filter(lambda x: "adp" in x, sub_frs))
            sub_ado = list(filter(lambda x: "ado" in x, sub_frs))
            sub_lad = list(filter(lambda x: "lad" in x, sub_frs))
            sub_cnt = list(filter(lambda x: "cnt" in x, sub_frs))
            sub_data = list(filter(lambda x: "data" in x, sub_frs))
            print()

            sub_names = filter(lambda x: "sub" in x, ecat.field_names)

            #print(sub_cmds)
            #print(sub_idx)
            #print(sub_adp)
            #print(sub_ado)
            #print(sub_lad)
            #print(sub_cnt)
            #print(sub_data)

          
            for item in sub_data:
                data[item] = ecat.get(item)
                   
                
                
            
           

            


            m = IpalMessage(
                id=self._id_counter.get_next_id(),
                src=src,
                dest=dest,
                timestamp=float(pkt.sniff_time.timestamp()),
                protocol=self._name,
                #flow=flow,
                length=msg_length,
                data=data,
                type=cmd,
            )
            res.append(m)
            
            
        
        return res

    def match_response(self, requests, response):
        remove_from_queue = []
        return remove_from_queue
