#!/bin/bash
cat /proc/[0-9]*/oom_score 2>/dev/null | sort -nr | head -1