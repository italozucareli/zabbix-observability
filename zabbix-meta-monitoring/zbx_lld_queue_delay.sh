#!/bin/bash
zabbix_server -R diaginfo=lld | grep "queued:" | awk '{print $2}' | tr -d ','