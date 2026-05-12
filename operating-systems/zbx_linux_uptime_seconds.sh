#!/bin/bash
cat /proc/uptime | awk '{print $1}' | cut -d. -f1