#!/bin/bash
UPS=$1
ALARM=$(upsc "$UPS" ups.alarm 2>/dev/null)
if [ -n "$ALARM" ]; then echo "{\"active_alarm\": \"$ALARM\"}"; else echo "{\"active_alarm\": \"None\"}"; fi