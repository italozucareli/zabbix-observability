#!/usr/bin/env python3
import pycurl, json, sys
from io import BytesIO

def check_api_health(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.TIMEOUT, 15)
    c.setopt(c.SSL_VERIFYPEER, 0)
    c.setopt(c.SSL_VERIFYHOST, 0)
    
    metrics = {"status": 0, "http_code": 0, "timing": {}}
    try:
        c.perform()
        metrics["status"] = 1
        metrics["http_code"] = c.getinfo(pycurl.HTTP_CODE)
        
        t_namelookup = c.getinfo(pycurl.NAMELOOKUP_TIME)
        t_connect = c.getinfo(pycurl.CONNECT_TIME)
        t_appconnect = c.getinfo(pycurl.APPCONNECT_TIME)
        t_pretransfer = c.getinfo(pycurl.PRETRANSFER_TIME)
        t_total = c.getinfo(pycurl.TOTAL_TIME)
        
        metrics["timing"]["dns_resolution"] = round(t_namelookup * 1000, 2)
        metrics["timing"]["tcp_connection"] = round((t_connect - t_namelookup) * 1000, 2)
        if t_appconnect > 0:
            metrics["timing"]["tls_handshake"] = round((t_appconnect - t_connect) * 1000, 2)
        metrics["timing"]["time_to_first_byte"] = round(t_pretransfer * 1000, 2)
        metrics["timing"]["total_time"] = round(t_total * 1000, 2)
    except pycurl.error as e:
        metrics["error_msg"] = str(e)
    finally:
        c.close()
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    check_api_health(sys.argv[1])