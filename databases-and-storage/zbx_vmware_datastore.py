#!/usr/bin/env python3
import atexit, sys, json
from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim

VCENTER = sys.argv[1]
USER = sys.argv[2]
PASS = sys.argv[3]

try:
    si = SmartConnectNoSSL(host=VCENTER, user=USER, pwd=PASS)
    atexit.register(Disconnect, si)
    
    content = si.RetrieveContent()
    container = content.viewManager.CreateContainerView(content.rootFolder, [vim.Datastore], True)
    
    zabbix_data = []
    for ds in container.view:
        summary = ds.summary
        capacity = summary.capacity
        freeSpace = summary.freeSpace
        uncommitted = summary.uncommitted if summary.uncommitted else 0
        
        zabbix_data.append({
            "{#DATASTORE_NAME}": summary.name,
            "capacity_bytes": capacity,
            "free_bytes": freeSpace,
            "provisioned_bytes": (capacity - freeSpace) + uncommitted,
            "accessible": 1 if summary.accessible else 0
        })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))