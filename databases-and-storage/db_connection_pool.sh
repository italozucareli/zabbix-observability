#!/bin/bash
psql -U postgres -t -c "SELECT count(*) FROM pg_stat_activity WHERE state = 'active';" | tr -d ' '