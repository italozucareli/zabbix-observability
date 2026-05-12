#!/bin/bash
# Conta quantas sessões ativas (pts) existem no momento
who | grep "pts/" | wc -l