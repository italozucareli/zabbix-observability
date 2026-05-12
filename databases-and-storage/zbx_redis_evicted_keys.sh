#!/bin/bash
redis-cli info stats | grep "evicted_keys" | cut -d: -f2 | tr -d '\r'