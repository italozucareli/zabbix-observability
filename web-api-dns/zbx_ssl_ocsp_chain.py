#!/usr/bin/env python3
import subprocess, json, sys, datetime

domain = sys.argv[1]
port = sys.argv[2] if len(sys.argv) > 2 else "443"

try:
    cmd = f"echo | openssl s_client -servername {domain} -connect {domain}:{port} -status 2>/dev/null"
    output = subprocess.check_output(cmd, shell=True, text=True)
    
    metrics = {
        "days_valid": 0,
        "ocsp_response": "unknown",
        "chain_ok": 1 if "Verify return code: 0 (ok)" in output else 0
    }
    
    if "OCSP Response Status: successful" in output:
        metrics["ocsp_response"] = "successful"
    elif "OCSP Response Status: revoked" in output:
        metrics["ocsp_response"] = "revoked"
        
    date_cmd = f"echo | openssl s_client -servername {domain} -connect {domain}:{port} 2>/dev/null | openssl x509 -noout -dates | grep notAfter"
    date_out = subprocess.check_output(date_cmd, shell=True, text=True).strip().split('=')[1]
    
    exp_date = datetime.datetime.strptime(date_out, '%b %d %H:%M:%S %Y %Z')
    days_left = (exp_date - datetime.datetime.now()).days
    metrics["days_valid"] = days_left
    
    print(json.dumps(metrics))
except Exception as e:
    print(json.dumps({"error": str(e)}))