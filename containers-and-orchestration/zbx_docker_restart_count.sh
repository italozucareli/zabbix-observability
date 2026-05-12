#!/bin/bash
docker inspect -f "{{.RestartCount}}" $1