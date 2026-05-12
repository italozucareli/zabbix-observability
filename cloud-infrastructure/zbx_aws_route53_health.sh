#!/bin/bash
aws route53 get-health-check-status --health-check-id $1 --query 'HealthCheckObservations[0].StatusReport.Status' --output text