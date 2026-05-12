#!/bin/bash
az vm list -d --query '[].{ "{#VM_NAME}": name, "powerState": powerState }' -o json | jq '{data: .}'