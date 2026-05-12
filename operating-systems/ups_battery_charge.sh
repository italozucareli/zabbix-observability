#!/bin/bash
# Retorna a porcentagem de bateria restante
apcaccess -u | grep BCHARGE | awk '{print $3}'