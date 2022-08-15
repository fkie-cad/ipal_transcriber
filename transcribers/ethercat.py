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
        print(pkt)

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
            #print()

            sub_names = filter(lambda x: "sub" in x, ecat.field_names)

            #print(sub_cmds)
            #print(sub_idx)
            #print(sub_adp)
            #print(sub_ado)
            #print(sub_lad)
            #print(sub_cnt)
            #print(sub_data)
            
            #Address To Data Matching
            all_addresses = []
            for i,item in enumerate(sub_cmds):
                temp = "sub"
                match int(ecat.get(item),16):
                    case 4: #FPRD                        
                        all_addresses.append(self.get_ado_adp_address(i, ecat))

                    case 7: # BRD                                 
                        all_addresses.append(self.get_ado_adp_address(i, ecat))
                        
                    case 8: #BWR                                     
                        all_addresses.append(self.get_ado_adp_address(i, ecat))
                        
                    case 10: #LRD
                        s = f"{temp}{i+1}_lad"   
                        print(s)
                        print(temp + str(i +1) + "_lad")                                    
                        all_addresses.append(str(ecat.get(temp + str(i +1) + "_lad")))
                       
                    case 11: #LWR                                      
                        all_addresses.append(str(ecat.get(temp + str(i +1) + "_lad")))
                        
                    case 12: #LRW                 
                        all_addresses.append(str(ecat.get(temp + str(i +1) + "_lad")))
                      
            for i,sdata in enumerate(sub_data):
                data[all_addresses[i]] = ecat.get(sdata)
                   


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

    def get_ado_adp_address(self, i, ecat):
        ado = ecat.get("sub" + str(i +1) + "_ado")                       
        adp = ecat.get("sub" + str(i +1) + "_adp" )
        current_address = "Ado: " + str(ado) + " Adp: " + str(adp)
        return current_address

