#!/bin/bash
mysql -e "SHOW GLOBAL STATUS LIKE 'Slow_queries';" | awk 'NR==2 {print $2}'