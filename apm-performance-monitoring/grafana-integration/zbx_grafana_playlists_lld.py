#!/usr/bin/env python3
import requests, json, sys
URL, TOKEN = sys.argv[1], sys.argv[2]
try:
    resp = requests.get(f"{URL}/api/playlists", headers={"Authorization": f"Bearer {TOKEN}"}, verify=False).json()
    zbx_data = [{"{#PLAYLIST_NAME}": p['name'], "{#PLAYLIST_UID}": p['uid']} for p in resp]
    print(json.dumps({"data": zbx_data}))
except Exception as e: print(json.dumps({"error": str(e)}))