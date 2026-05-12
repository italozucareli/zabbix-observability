#!/usr/bin/env python3
import requests, json, sys

WEBHOOK_URL = sys.argv[1] # Passado pela GUI do Zabbix
SUBJECT = sys.argv[2] # {EVENT.NAME}
MESSAGE = sys.argv[3] # Descrição detalhada
STATUS = sys.argv[4] # PROBLEM ou OK

# Define a cor da borda no Teams: Vermelho para Problema, Verde para Resolução
color = "FF0000" if STATUS == "PROBLEM" else "00FF00"

adaptive_card = {
    "type": "message",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "type": "AdaptiveCard",
                "version": "1.2",
                "body": [
                    {
                        "type": "TextBlock",
                        "text": f"[{STATUS}] {SUBJECT}",
                        "weight": "Bolder",
                        "size": "Medium",
                        "color": "Attention" if STATUS == "PROBLEM" else "Good"
                    },
                    {
                        "type": "TextBlock",
                        "text": MESSAGE,
                        "wrap": True
                    }
                ]
            }
        }
    ]
}

requests.post(WEBHOOK_URL, json=adaptive_card, headers={"Content-Type": "application/json"})