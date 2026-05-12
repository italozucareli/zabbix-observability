#!/bin/bash
grep "housekeeper deleted" /var/log/zabbix/zabbix_server.log | tail -1 | awk '{print $NF}'