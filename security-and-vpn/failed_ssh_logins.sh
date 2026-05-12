#!/bin/bash
# Conta bloqueios de senha no auth.log
grep "Failed password" /var/log/auth.log | wc -l