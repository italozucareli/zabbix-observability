#!/bin/bash
zabbix_server -R diaginfo=preprocessing | grep "queued:" | awk '{print $2}' | tr -d ','