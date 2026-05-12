#!/bin/bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].{"{#INSTANCE_ID}":InstanceId, "{#STATE}":State.Name}' --output json | jq '{data: flatten}'