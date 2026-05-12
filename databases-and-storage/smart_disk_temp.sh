#!/bin/bash
# Uso: ./smart_disk_temp.sh sda (Requer sudo no zabbix_agentd.conf: zabbix ALL=(ALL) NOPASSWD: /usr/sbin/smartctl)
sudo smartctl -A /dev/$1 | grep -i "Temperature_Celsius" | awk '{print $10}'