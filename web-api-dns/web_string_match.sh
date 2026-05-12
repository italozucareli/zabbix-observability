#!/bin/bash
# Uso: ./web_string_match.sh https://meusite.com "PalavraChave"
# Retorna 1 se encontrou, 0 se falhou
curl -sL "$1" | grep -q "$2" && echo 1 || echo 0