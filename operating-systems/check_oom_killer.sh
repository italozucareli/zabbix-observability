#!/bin/bash
# Retorna a quantidade de processos mortos por falta de memória (zera no reboot)
dmesg | grep -i "killed process" | wc -l