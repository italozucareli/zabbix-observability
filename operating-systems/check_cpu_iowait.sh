#!/bin/bash
# Executa vmstat e pega a coluna 'wa' (iowait)
vmstat 1 2 | tail -1 | awk '{print $16}'