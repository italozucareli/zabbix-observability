#!/bin/bash
IP=$1
COMM=$2

# APC upsBasicBatteryLastReplaceDate (formato mm/dd/yy)
DATE_STR=$(snmpget -v2c -c "$COMM" -Oqv "$IP" 1.3.6.1.4.1.318.1.1.1.2.1.3.0 2>/dev/null | tr -d '"')

if [ -n "$DATE_STR" ]; then
    # Converte mm/dd/yy para timestamp no bash
    INSTALL_SEC=$(date -d "${DATE_STR:0:2}/${DATE_STR:3:2}/20${DATE_STR:6:2}" +%s 2>/dev/null)
    NOW_SEC=$(date +%s)
    
    if [ -n "$INSTALL_SEC" ]; then
        MONTHS_AGE=$(( (NOW_SEC - INSTALL_SEC) / 2592000 ))
        echo "{\"battery_age_months\": $MONTHS_AGE}"
    else
        echo "{\"error\": \"Falha no parse da data\"}"
    fi
else
    echo "{\"error\": \"Data nao preenchida no painel do UPS\"}"
fi