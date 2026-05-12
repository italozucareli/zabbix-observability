#!/bin/bash
psql -U postgres -t -c "SELECT sum(size) FROM pg_ls_waldir();" | tr -d ' '