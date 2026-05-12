#!/bin/bash
# Uso: ./file_checksum_monitor.sh /etc/passwd
# No Zabbix, monitore se o valor retornado muda.
sha256sum "$1" | awk '{print $1}'