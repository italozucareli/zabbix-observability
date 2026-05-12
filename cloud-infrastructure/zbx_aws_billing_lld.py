#!/usr/bin/env python3
import boto3, json, datetime

client = boto3.client('ce', region_name='us-east-1')
start = datetime.date.today().replace(day=1).strftime('%Y-%m-%d')
end = datetime.date.today().strftime('%Y-%m-%d')

if start == end:
    print(json.dumps({"data": []}))
    exit(0)

try:
    response = client.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': end},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )
    
    zabbix_data = []
    for group in response['ResultsByTime'][0]['Groups']:
        service = group['Keys'][0]
        cost = round(float(group['Metrics']['UnblendedCost']['Amount']), 2)
        if cost > 0.01:
            zabbix_data.append({
                "{#AWS_SERVICE}": service,
                "cost_usd": cost
            })
    print(json.dumps({"data": zabbix_data}))
except Exception as e:
    print(json.dumps({"error": str(e)}))