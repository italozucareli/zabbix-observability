#!/bin/bash
mongosh --quiet --eval "db.serverStatus().connections.current"