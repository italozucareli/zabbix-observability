#!/bin/bash
zabbix_server -R diaginfo=historycache | grep "poller" | awk '{print $NF}' | sort -nr | head -1