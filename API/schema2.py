def seria(iot)-> dict:
    return {
        "id":str(iot["_id"]),
        #"ip": str(iot["ip"]),
        #"status": str(iot["status"]),
        "missed_bytes": int(iot["missed_bytes"]),
        "orig_pkts": int(iot["orig_pkts"]),
        "orig_ip_bytes": int(iot["orig_ip_bytes"]),
        "resp_pkts": int(iot["resp_pkts"]),
        "resp_ip_bytes": int(iot["resp_ip_bytes"]),
        "proto_icmp": int(iot["proto_icmp"]),
        "proto_tcp": int(iot["proto_tcp"]),
        "proto_udp": int(iot["proto_udp"]),
        "service_Unknown": int(iot["service_Unknown"]),
        "service_dhcp": int(iot["service_dhcp"]),
        "service_dns": int(iot["service_dns"]),
        "service_ssh": int(iot["service_ssh"])
    }
def list_deseri(iots)-> list:
    return [seria(iot) for iot in iots]