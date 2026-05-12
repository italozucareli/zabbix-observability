#!/bin/bash
# Conta quantos containers pararam com erro ou normalmente (estado exited)
# Retorna um número (0 é o ideal)
COUNT=$(docker ps -qa -f status=exited | wc -l)
echo $COUNT