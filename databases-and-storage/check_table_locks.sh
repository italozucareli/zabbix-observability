#!/bin/bash
mysql -e "SHOW GLOBAL STATUS LIKE 'Table_locks_waited';" | awk 'NR==2 {print $2}'