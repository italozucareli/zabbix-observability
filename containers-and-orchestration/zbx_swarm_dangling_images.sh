#!/bin/bash
docker image ls -qf dangling=true 2>/dev/null | wc -l || echo 0