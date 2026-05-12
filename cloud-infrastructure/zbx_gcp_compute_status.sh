#!/bin/bash
gcloud compute instances list --format="json" | jq '{data: [ .[] | {"{#INSTANCE_NAME}": .name, "status": .status} ]}'