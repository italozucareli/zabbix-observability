#!/usr/bin/env python3
import subprocess, json, argparse, tempfile, os

def run_mtr_and_send(target, zabbix_server, hostname):
    cmd = ["mtr", "--report", "--json", "-c", "10", target]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        mtr_data = json.loads(result.stdout)
    except Exception as e:
        print(f"Erro: {e}")
        return

    sender_data = []
    for hop in mtr_data.get('report', {}).get('hubs', []):
        hop_num = hop.get('count')
        loss = hop.get('Loss%')
        avg_latency = hop.get('Avg')
        
        sender_data.append(f'- net.hop.loss[{hop_num},{target}] {loss}')
        sender_data.append(f'- net.hop.latency[{hop_num},{target}] {avg_latency}')

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp.write("\n".join(sender_data))
        tmp_name = tmp.name

    sender_cmd = ["zabbix_sender", "-z", zabbix_server, "-s", hostname, "-i", tmp_name]
    subprocess.run(sender_cmd, capture_output=True)
    os.unlink(tmp_name)
    print(f"Enviado para {target}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", required=True)
    parser.add_argument("-z", "--zabbix", required=True)
    parser.add_argument("-s", "--host", required=True)
    args = parser.parse_args()
    run_mtr_and_send(args.target, args.zabbix, args.host)