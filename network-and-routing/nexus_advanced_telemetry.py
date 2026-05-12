#!/usr/bin/env python3
import requests, json, sys, argparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_nexus_telemetry(ip, user, password):
    url = f"https://{ip}/ins"
    headers = {'Content-Type': 'application/json-rpc'}
    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "show bgp ipv4 unicast summary", "version": 1}, "id": 1},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "show interface brief", "version": 1}, "id": 2}
    ]
    try:
        response = requests.post(url, auth=(user, password), headers=headers, json=payload, verify=False, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        zabbix_payload = {"bgp_peers": [], "interfaces": [], "telemetry": {}}

        bgp_data = data[0].get('result', {}).get('body', {}).get('TABLE_vrf', {}).get('ROW_vrf', {}).get('TABLE_af', {}).get('ROW_af', {}).get('TABLE_peer', {}).get('ROW_peer', [])
        if isinstance(bgp_data, dict): bgp_data = [bgp_data]
        
        for peer in bgp_data:
            state = peer.get('state', 'Unknown')
            zabbix_payload["bgp_peers"].append({
                "{#PEER_IP}": peer.get('peerid'),
                "{#PEER_ASN}": peer.get('peer_as'),
                "status": 1 if "Established" in state else 0,
                "msg_rcv": peer.get('msg_rcv', 0),
                "msg_sent": peer.get('msg_sent', 0)
            })

        intf_data = data[1].get('result', {}).get('body', {}).get('TABLE_interface', {}).get('ROW_interface', [])
        for intf in intf_data:
            zabbix_payload["interfaces"].append({
                "{#IF_NAME}": intf.get('interface'),
                "{#IF_STATE}": intf.get('state'),
                "speed": intf.get('speed', '0'),
                "mtu": intf.get('mtu', '1500')
            })
            
        print(json.dumps(zabbix_payload, indent=2))
        sys.exit(0)
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", required=True)
    parser.add_argument("-u", "--user", required=True)
    parser.add_argument("-p", "--password", required=True)
    args = parser.parse_args()
    get_nexus_telemetry(args.ip, args.user, args.password)