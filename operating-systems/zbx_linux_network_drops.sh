#!/bin/bash
netstat -s | grep "packet receive errors" | awk '{print $1}'