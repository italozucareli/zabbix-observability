#!/bin/bash
ps aux | awk '{print $8}' | grep -c "Z"