#!/bin/bash
cat /proc/sys/fs/file-nr | awk '{print $1}'