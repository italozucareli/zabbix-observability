#!/bin/bash
redis-cli info memory | grep "mem_fragmentation_ratio" | cut -d: -f2 | tr -d '\r'