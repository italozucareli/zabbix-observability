#!/bin/bash
SECRETS=$(docker secret ls -q 2>/dev/null | wc -l || echo 0)
CONFIGS=$(docker config ls -q 2>/dev/null | wc -l || echo 0)

cat <<EOF
{
  "total_secrets": $SECRETS,
  "total_configs": $CONFIGS
}
EOF