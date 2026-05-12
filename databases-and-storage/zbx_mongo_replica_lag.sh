#!/bin/bash
mongosh --quiet --eval "rs.printSecondaryReplicationInfo()" | grep "behind the primary" | awk '{print $1}' | head -1