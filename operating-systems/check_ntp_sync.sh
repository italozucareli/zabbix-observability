#!/bin/bash
# Retorna 1 se estiver sincronizado, 0 se não estiver
chronyc tracking | grep -i "Leap status" | grep -q "Normal" && echo 1 || echo 0