#!/bin/bash
cat /proc/loadavg | awk '{print $4}' | cut -d/ -f2