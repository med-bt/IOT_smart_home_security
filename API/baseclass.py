from pydantic import BaseModel
class BaseClass(BaseModel):
    missed_bytes:int
    orig_pkts: int
    orig_ip_bytes: int
    resp_pkts: int
    resp_ip_bytes: int
    proto_icmp: int
    proto_tcp: int
    proto_udp:int
    service_Unknown: int
    service_dhcp: int
    service_dns: int
    service_ssh: int



#class Item(BaseModel):
 #   features: list  # Assurez-vous que cette définition correspond aux attentes de votre modèle
