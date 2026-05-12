#!/bin/bash
zabbix_server -R diaginfo=valuecache | grep "hits:" | awk '{print $2}' | tr -d ','