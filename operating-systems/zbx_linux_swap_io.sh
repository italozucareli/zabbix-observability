#!/bin/bash
# Requer um argumento: 'in' ou 'out'
awk -v op="$1" '/^pswpin/ && op=="in" {print $2} /^pswpout/ && op=="out" {print $2}' /proc/vmstat