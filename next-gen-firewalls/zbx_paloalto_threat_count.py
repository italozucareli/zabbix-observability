#!/usr/bin/env python3
import requests, json, sys
import xml.etree.ElementTree as ET

PAN_HOST, PAN_KEY = sys.argv[1], sys.argv[2]
# Usa a API de relatório para ameaças recentes (Últimos 15 min)
url = f"https://{PAN_HOST}/api/?type=report&reporttype=dynamic&reportname=threats-last-15-mins&key={PAN_KEY}"

try:
    # Nota: Execução de relatórios via API no PAN pode exigir polling de job_id, mas para simplificar, usamos uma query REST compatível se configurada no PAN-OS.
    # Exemplo genérico de payload de retorno.
    resp = requests.get(url, verify=False)
    root = ET.fromstring(resp.content)
    # Exemplo extraído da árvore XML
    threats = len(root.findall('.//entry'))
    print(json.dumps({"threats_detected_15m": threats}))
except Exception as e: print(json.dumps({"error": str(e)}))