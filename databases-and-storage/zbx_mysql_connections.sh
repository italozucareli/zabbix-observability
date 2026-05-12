#!/bin/bash
MAX=$(mysql -e "SHOW VARIABLES LIKE 'max_connections';" | awk 'NR==2 {print $2}')
USED=$(mysql -e "SHOW GLOBAL STATUS LIKE 'Threads_connected';" | awk 'NR==2 {print $2}')
echo | awk -v u="$USED" -v m="$MAX" '{printf "%.2f", (u/m)*100}'