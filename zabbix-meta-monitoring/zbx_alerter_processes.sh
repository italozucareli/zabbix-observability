#!/bin/bash
ps aux | grep "zabbix_server: alerter" | grep -v grep | wc -l