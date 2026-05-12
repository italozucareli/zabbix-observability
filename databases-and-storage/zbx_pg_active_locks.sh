#!/bin/bash
psql -U postgres -t -c "SELECT count(*) FROM pg_locks WHERE granted = false;" | tr -d ' '