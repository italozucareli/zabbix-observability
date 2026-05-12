#!/bin/bash
df -i | awk 'NR>1 {print $5}' | sed 's/%//' | sort -nr | head -1