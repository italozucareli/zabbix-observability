#!/bin/bash
psql -U postgres -t -c "SELECT sum(blks_hit)*100/sum(blks_hit+blks_read) FROM pg_stat_database;" | tr -d ' '