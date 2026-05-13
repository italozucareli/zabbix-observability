# 👁️ Zabbix Enterprise Observability & Automation Toolkit

A comprehensive, SRE-grade repository of over 380 advanced scripts, Master Items, Low-Level Discovery (LLD) rules, and Event-Driven Automation webhooks designed to elevate Zabbix from a simple monitoring tool into a complete IT Operations Management (ITOM) platform.

This toolkit bridges the gap between bare-metal infrastructure, Cloud, Application Performance Monitoring (APM), Security (SecOps), FinOps, and ITSM.

---

## 🏗️ Architecture & Philosophy

To ensure scalability in mission-critical environments, these scripts adopt the following principles:
*   **Zero-Overhead Polling:** Scripts make a single, bulk call to an equipment or API, returning a complete JSON payload. Zabbix processes this internally via LLD and Dependent Items.
*   **Dynamic Discovery:** Reduces manual configuration. VPNs, BGP peers, Kubernetes pods, Docker Swarm services, and API limits are discovered dynamically.
*   **Event-Driven Automation:** Monitoring is only half the battle. This toolkit includes Action Webhooks to automatically open ServiceNow incidents, draw Grafana annotations, or trigger Ansible AWX playbooks.
*   **Domain-Driven Telemetry:** Segregated by technology domain (APM, SIEM, SecOps, Networking) for clean RBAC and repository management.

---

## 📂 Repository Structure & Complete Script Index

### ☁️ `cloud-infrastructure/`
*   `zbx_aws_billing_lld.py` - AWS monthly billing discovery via Boto3.
*   `zbx_aws_ec2_status.sh` - AWS EC2 instance state discovery.
*   `zbx_aws_rds_cpu.sh` - AWS RDS CPU utilization monitor.
*   `zbx_aws_route53_health.sh` - AWS Route53 health check status.
*   `zbx_aws_s3_size.sh` - AWS S3 bucket size tracker.
*   `zbx_azure_blob_size.sh` - Azure Storage Account capacity monitor.
*   `zbx_azure_vm_status.sh` - Azure VM power state discovery.
*   `zbx_cloudflare_pool_health.sh` - Cloudflare Load Balancer pools health.
*   `zbx_do_droplet_status.sh` - DigitalOcean Droplet status discovery.
*   `zbx_gcp_cloudsql_cpu.sh` - GCP Cloud SQL CPU utilization.
*   `zbx_gcp_compute_status.sh` - GCP Compute instance status discovery.

### 🐳 `containers-and-orchestration/`
**Docker & Swarm:**
*   `docker_container_lld.py` - Docker container discovery and stats via socket.
*   `docker_container_state.sh` - Counts exited or crashed Docker containers.
*   `zbx_docker_cpu_usage.sh` - Gets CPU usage % for a specific container.
*   `zbx_docker_health_status.sh` - Docker internal healthcheck status.
*   `zbx_docker_mem_usage.sh` - Gets memory usage for a specific container.
*   `zbx_docker_restart_count.sh` - Tracks specific container restart counts.
*   `zbx_swarm_cluster_health.py` - Master Item tracking Docker Swarm Control Plane.
*   `zbx_swarm_dangling_images.sh` - Identifies untagged/orphaned images.
*   `zbx_swarm_dangling_volumes.sh` - Identifies unattached local volumes.
*   `zbx_swarm_global_tasks_health.sh` - Counts failing `global` mode services.
*   `zbx_swarm_manager_leader.sh` - Identifies if the node is the active Raft Leader.
*   `zbx_swarm_networks_lld.py` - LLD for Swarm overlay networks.
*   `zbx_swarm_node_drift_lld.py` - LLD tracking Docker Engine versions to detect drift.
*   `zbx_swarm_node_labels_lld.py` - Discovers assigned Node Labels.
*   `zbx_swarm_nodes_lld.py` - LLD for Swarm nodes (Ready/Active).
*   `zbx_swarm_pending_tasks.sh` - Counts tasks stuck in 'Pending'.
*   `zbx_swarm_published_ports_lld.py` - LLD mapping Swarm Services to external ports.
*   `zbx_swarm_quorum_health.sh` - Verifies Raft Manager Quorum health.
*   `zbx_swarm_rejected_tasks.sh` - Counts 'Rejected' tasks.
*   `zbx_swarm_secrets_configs_audit.sh` - Returns counts of Swarm Secrets and Configs.
*   `zbx_swarm_service_tasks_failed.sh` - Counts historical task failures.
*   `zbx_swarm_services_lld.py` - Master Item LLD that discovers Stacks and Services.
*   `zbx_swarm_worker_local_tasks_lld.py` - Maps local containers to parent Swarm Service.

**Kubernetes:**
*   `k8s_node_ready.py` - Checks Kubernetes nodes ready status.
*   `k8s_pod_status_lld.sh` - LLD for Kubernetes pods and restart counts.
*   `zbx_k8s_admission_webhooks.py` - LLD for validating/mutating webhook configurations.
*   `zbx_k8s_api_latency.py` - Synthetic micro-transaction to measure K8s API latency.
*   `zbx_k8s_apiservice_health.py` - Health check for aggregated API services.
*   `zbx_k8s_apiserver_metrics.py` - Aggregates 5xx HTTP errors directly from kube-apiserver.
*   `zbx_k8s_coredns_changes.py` - Tracks CoreDNS ConfigMap hash changes.
*   `zbx_k8s_crd_versions.py` - Audits CRDs for deprecated API versions.
*   `zbx_k8s_cronjob_status.py` - LLD for CronJobs, tracking active executions.
*   `zbx_k8s_csr_pending.py` - Counts Certificate Signing Requests pending approval.
*   `zbx_k8s_daemonset_misscheduled.py` - Detects DaemonSets on nodes with mismatched Taints.
*   `zbx_k8s_daemonset_ready.sh` - Kubernetes DaemonSet readiness monitor.
*   `zbx_k8s_deployment_replicas.sh` - Kubernetes Deployment replica availability.
*   `zbx_k8s_deployment_sync.py` - Identifies stuck Deployments.
*   `zbx_k8s_endpoints_capacity.py` - Monitors Services approaching the 1000 endpoints limit.
*   `zbx_k8s_evicted_pods.py` - Counts pods stuck in the Evicted state.
*   `zbx_k8s_helm_secrets.py` - Decodes Helm Secrets to monitor deployment statuses.
*   `zbx_k8s_hpa_events.py` - Aggregates horizontal scaling events.
*   `zbx_k8s_hpa_status.py` - LLD for Horizontal Pod Autoscalers (current vs desired).
*   `zbx_k8s_ingress_classes.py` - Discovers and monitors active Ingress Classes.
*   `zbx_k8s_ingress_status.sh` - Validates K8s Ingress provisioned IPs.
*   `zbx_k8s_ingress_tls_expiry.py` - Calculates SSL expiration days directly from Secrets.
*   `zbx_k8s_job_failures.py` - Discovers Batch Jobs and alerts on failures.
*   `zbx_k8s_kubelet_versions.py` - Audits node Kubelet versions to detect failed upgrades.
*   `zbx_k8s_limit_ranges.py` - Checks if Namespaces enforce LimitRanges.
*   `zbx_k8s_namespace_governance.py` - Audits Namespaces for mandatory compliance labels.
*   `zbx_k8s_node_conditions.py` - Monitors silent Node conditions (MemoryPressure).
*   `zbx_k8s_node_cpu_alloc.sh` - Kubernetes node CPU allocation percentage.
*   `zbx_k8s_node_taints.py` - Tracks NoSchedule/NoExecute Taints applied to nodes.
*   `zbx_k8s_oomkilled_pods.py` - Scans all pods to detect OOMKilled containers.
*   `zbx_k8s_pdb_status.py` - Monitors Pod Disruption Budgets (PDBs).
*   `zbx_k8s_pod_restarts.sh` - Total restarts across all containers in a pod.
*   `zbx_k8s_priority_classes.py` - Discovers custom Priority Classes.
*   `zbx_k8s_pv_status.py` - LLD for Persistent Volumes (PVs).
*   `zbx_k8s_pvc_usage.sh` - K8s Persistent Volume Claim disk usage.
*   `zbx_k8s_replicaset_orphans.py` - Counts orphaned ReplicaSets.
*   `zbx_k8s_resource_quotas.py` - Monitors ResourceQuota utilization.
*   `zbx_k8s_service_nodeports.py` - Discovers reserved physical NodePorts.
*   `zbx_k8s_statefulset_revisions.py` - Detects StatefulSet updates stuck mid-rollout.
*   `zbx_k8s_storage_classes.py` - Discovers available StorageClasses.
*   `zbx_k8s_warning_events.py` - Aggregates cluster-wide Warning events.

### 🗄️ `databases-and-storage/`
*   `check_table_locks.sh` - Identifies MySQL waiting table locks.
*   `db_connection_pool.sh` - Counts active connections in PostgreSQL.
*   `elasticsearch_cluster_lld.sh` - LLD for ElasticSearch indices health/size.
*   `kafka_consumer_lag_lld.sh` - Kafka consumer group lag LLD.
*   `lvm_volumes_lld.sh` - LLD for LVM logical volume utilization.
*   `mysql_long_queries.sh` - Counts MySQL queries running over 60s.
*   `pg_database_discovery_lld.sh` - LLD for PostgreSQL databases and sizes.
*   `pg_replication_lag.sh` - PostgreSQL replication lag in seconds.
*   `rabbitmq_queues_lld.sh` - LLD for RabbitMQ queues and unacknowledged messages.
*   `raid_array_status.sh` - Software RAID (mdadm) array status monitor.
*   `redis_keyspace_lld.sh` - LLD for Redis databases and key counts.
*   `smart_disk_discovery_lld.sh` - LLD for physical disks via `lsblk`.
*   `smart_disk_temp.sh` - S.M.A.R.T. physical disk temperature monitor.
*   `zbx_mongo_connections.sh` - Current MongoDB active connections.
*   `zbx_mongo_replica_lag.sh` - MongoDB secondary replica lag monitor.
*   `zbx_mysql_buffer_pool.sh` - MySQL InnoDB buffer pool hit ratio.
*   `zbx_mysql_connections.sh` - MySQL active connections percentage.
*   `zbx_mysql_slow_queries.sh` - MySQL absolute slow queries counter.
*   `zbx_pg_active_locks.sh` - PostgreSQL transactions stuck on deadlocks.
*   `zbx_pg_cache_hit_ratio.sh` - PostgreSQL memory cache hit ratio %.
*   `zbx_pg_wal_size.sh` - PostgreSQL WAL directory size in bytes.
*   `zbx_redis_evicted_keys.sh` - Redis evicted keys counter (OOM tracking).
*   `zbx_redis_memory_fragmentation.sh` - Redis memory fragmentation ratio.
*   `zbx_timescaledb_chunks.sh` - TimescaleDB chunks audit.
*   `zbx_vmware_datastore.py` - VMware vSphere Datastore capacity via pyVim.
*   `zfs_pool_health_lld.sh` - LLD for ZFS pool health and capacity.

### ⚡ `power-and-environment/`
*   `zbx_apc_ats_redundancy.sh` - Alerts if an ATS loses backup power source redundancy.
*   `zbx_apc_ats_source_status.sh` - Checks synchronization and active power source on APC ATS.
*   `zbx_apc_humidity_temp.sh` - Consolidated JSON payload for rack temp/humidity.
*   `zbx_apc_nmc_api_master.py` - Reads native REST API data from modern APC NMC v3.
*   `zbx_apcupsd_events_parser.sh` - Parses `/var/log/apcupsd.events` for critical events.
*   `zbx_apcupsd_master.py` - Master Item converting `apcaccess` output into JSON.
*   `zbx_delta_ups_battery_health.sh` - Specific Delta UPS MIB monitor.
*   `zbx_eaton_xups_health.sh` - Uses proprietary Eaton XUPS-MIB for hardware states.
*   `zbx_nut_active_alarms.sh` - Extracts the real-time alarm string broadcasted by NUT.
*   `zbx_nut_ups_discovery.py` - LLD script to dynamically discover UPS units managed by NUT.
*   `zbx_nut_ups_stats.py` - Master Item to extract metrics from a NUT-managed UPS.
*   `zbx_sms_ups_avr_state.sh` - Monitors Automatic Voltage Regulator (AVR) Boost/Buck states.
*   `zbx_snmp_generator_status.sh` - Tracks if dry contacts identify the backup generator.
*   `zbx_snmp_pdu_bank_status_lld.sh` - LLD for internal PDU banks/breakers.
*   `zbx_snmp_pdu_outlets_lld.sh` - LLD for discovering Smart PDU outlets.
*   `zbx_snmp_pdu_power_draw.sh` - Consolidates total amperage drawn across a PDU.
*   `zbx_snmp_rfc1628_health.sh` - Universal SNMP UPS monitor (RFC 1628).
*   `zbx_snmp_ups_alarms_lld.sh` - SNMP LLD to discover and track active hardware alarms.
*   `zbx_snmp_ups_audible_alarm.sh` - Monitors if the UPS physical audible alarm is sounding.
*   `zbx_snmp_ups_bad_battery_count.sh` - Counts defective battery cartridges.
*   `zbx_snmp_ups_battery_current.sh` - Tracks battery bus Amperage.
*   `zbx_snmp_ups_battery_temp.sh` - Monitors internal battery temperature (Celsius).
*   `zbx_snmp_ups_battery_voltage.sh` - Reads DC bus voltage.
*   `zbx_snmp_ups_bypass_voltage.sh` - Health check on the raw bypass line voltage.
*   `zbx_snmp_ups_efficiency.sh` - Calculates internal power efficiency percentage.
*   `zbx_snmp_ups_env_probes_lld.sh` - Discovers external environmental probes.
*   `zbx_snmp_ups_fan_status_lld.sh` - LLD to monitor individual cooling fan statuses.
*   `zbx_snmp_ups_load_capacity.sh` - Extracts current inverter load percentage.
*   `zbx_snmp_ups_output_current.sh` - Tracks exact Amperage being pulled by servers.
*   `zbx_snmp_ups_phases_lld.sh` - LLD for 3-Phase UPS systems.
*   `zbx_snmp_ups_power_quality.sh` - Consolidates I/O Voltage and Frequency.
*   `zbx_snmp_ups_real_power.sh` - Reads True Power (Watts) consumed.
*   `zbx_snmp_ups_selftest.sh` - Checks status of automated battery self-tests.
*   `zbx_snmp_ups_test_date.sh` - Parses timestamp of the last deep hardware diagnostic.
*   `zbx_ups_battery_lifecycle.sh` - Tracks battery age in months for predictive replacement.
*   `zbx_ups_energy_meter.sh` - Extracts total accumulated kWh meter.
*   `zbx_vertiv_ups_alarms.sh` - Vertiv/Liebert specific MIB monitor.

### 🌐 `network-and-routing/`
*   `check_bgp_peers.sh` - BGP peer established state via SNMP.
*   `check_ospf_neighbors.sh` - OSPF neighbor full state via SNMP.
*   `cisco_board_pro_status.py` - Cisco endpoint standby status via xAPI.
*   `cisco_meraki_devices_lld.py` - LLD for Cisco Meraki devices via API.
*   `interface_errors_rate.sh` - Linux interface RX errors parser.
*   `mikrotik_bgp_peer_lld.sh` - LLD for MikroTik BGP peers via REST API.
*   `mtr_zabbix_bridge.py` - Advanced path observability via MTR.
*   `network_interfaces_lld.sh` - Native Linux network interfaces discovery.
*   `nexus_advanced_telemetry.py` - Cisco Nexus BGP/Interface LLD via NX-API.
*   `nexus_env_health.py` - Cisco Nexus CPU/Memory health via NX-API.
*   `stp_topology_change.sh` - Spanning Tree topology change counter.
*   `zbx_cisco_aci_health.py` - Cisco ACI Fabric faults LLD.
*   `zbx_fortigate_sdwan.sh` - FortiGate SD-WAN SLA metrics (Latency/Jitter/Loss).

### 💻 `operating-systems/`
*   `check_cpu_iowait.sh` - Linux CPU iowait bottleneck percentage.
*   `check_disk_inodes.sh` - Linux disk inode utilization percentage.
*   `check_ntp_sync.sh` - NTP time synchronization status.
*   `check_oom_killer.sh` - OOM Killer intervention counter.
*   `check_pending_reboot.ps1` - Windows pending reboot registry check.
*   `check_zombie_procs.sh` - Linux zombie processes count.
*   `iis_app_pools_lld.ps1` - Windows IIS Application Pools discovery.
*   `systemd_services_lld.sh` - Linux enabled systemd services discovery.
*   `win_event_critical.ps1` - Windows critical event log counter.
*   `zbx_linux_context_switches.sh` - Linux CPU context switches rate.
*   `zbx_linux_deleted_open_files.sh` - Tracks deleted files holding disk space.
*   `zbx_linux_disk_io.sh` - Advanced Linux disk I/O metrics LLD.
*   `zbx_linux_entropy_avail.sh` - Available kernel cryptographic entropy.
*   `zbx_linux_inode_usage_max.sh` - Highest inode usage among mount points.
*   `zbx_linux_network_drops.sh` - Linux kernel network RX packet drops.
*   `zbx_linux_oom_score.sh` - Highest OOM score among running processes.
*   `zbx_linux_open_files.sh` - Total open file descriptors.
*   `zbx_linux_process_threads.sh` - Total OS threads count.
*   `zbx_linux_swap_io.sh` - Swap memory I/O paging metrics.
*   `zbx_linux_uptime_seconds.sh` - Exact system uptime in seconds.
*   `zbx_tcp_socket_states.sh` - TCP socket states counter (ESTABLISHED, TIME_WAIT).

### 🛡️ `security-and-vpn/`
*   `active_ssh_sessions.sh` - Active SSH user sessions count.
*   `check_open_ports.sh` - Validates if a specific local port is listening.
*   `failed_ssh_logins.sh` - Brute-force SSH failed logins counter.
*   `file_checksum_monitor.sh` - SHA256 critical file checksum monitor.
*   `openvpn_sessions_lld.py` - LLD for connected OpenVPN users.
*   `strongswan_ipsec_lld.sh` - LLD for StrongSwan IPsec tunnels.
*   `vpn_ipsec_tunnel.sh` - IPsec VPN tunnel up/down status via ICMP.
*   `zbx_paloalto_gp_users.py` - Palo Alto GlobalProtect active users count.

### 🕸️ `web-api-dns/`
*   `advanced_api_monitor.py` - Deep HTTP transaction lifecycle timing analyzer.
*   `api_json_value.py` - Extracts specific JSON values from REST APIs.
*   `check_domain_expiry.sh` - Domain registration expiration days.
*   `check_ssl_expiry.sh` - SSL certificate expiration days.
*   `dns_resolution_time.sh` - DNS resolution time in milliseconds.
*   `haproxy_backend_lld.sh` - LLD for HAProxy backend servers status.
*   `http_status_code.sh` - HTTP status code monitor.
*   `mail_queue_size.sh` - Postfix mail queue size counter.
*   `nginx_upstream_lld.sh` - LLD for Nginx upstream backend status.
*   `ssl_sni_discovery_lld.sh` - LLD for SSL certificates via Nginx SNI configs.
*   `web_string_match.sh` - Verifies if a specific string exists on a web page.
*   `zbx_m365_service_health.py` - Microsoft 365 services health status via Graph API.
*   `zbx_ssl_ocsp_chain.py` - SSL OCSP revocation and chain validation.

### 🏛️ `zabbix-meta-monitoring/`
*   `zbx_alerter_processes.sh` - Active Zabbix alerter processes count.
*   `zbx_db_config_bloat.sh` - Audit for unsupported items and disabled hosts.
*   `zbx_db_connections_active.sh` - Active DB connections from Zabbix Server.
*   `zbx_db_size_growth.sh` - Zabbix database total size in bytes.
*   `zbx_ha_cluster_status.sh` - Zabbix High Availability cluster nodes status.
*   `zbx_housekeeper_deleted.sh` - Records deleted by the last Housekeeper run.
*   `zbx_lld_queue_delay.sh` - LLD items waiting in the preprocessing queue.
*   `zbx_nvps_rate.sh` - New Values Per Second (NVPS) real-time rate.
*   `zbx_pg_dead_tuples.sh` - PostgreSQL dead tuples and bloat percentage.
*   `zbx_poller_busy_max.sh` - Highest poller utilization percentage.
*   `zbx_preprocessing_queue.sh` - Values queued for preprocessing.
*   `zbx_proxy_sync_delay.sh` - Zabbix Proxy sync delay in seconds via DB.
*   `zbx_queue_profiler.py` - Granular Zabbix queue delay extraction via API.
*   `zbx_server_log_parser.py` - Critical errors aggregator for Zabbix server log.
*   `zbx_trapper_sockets.sh` - Audit of TCP sockets stuck in Zabbix Trapper.
*   `zbx_unsupported_items_count.sh` - Total count of unsupported Zabbix items.
*   `zbx_value_cache_hits.sh` - Zabbix Value Cache hit counter.

### 🤝 `integrations-and-itsm/`
*   `zbx_awx_remediation.py` - Triggers Ansible Tower/AWX Job Templates.
*   `zbx_glpi_ticket.py` - Automatically opens and categorizes tickets in GLPI.
*   `zbx_jira_ticket.py` - Opens Jira Service Management issues.
*   `zbx_msteams_adaptive.py` - Pushes alerts to Microsoft Teams using Adaptive Cards.
*   `zbx_netbox_sync.py` - Auto-registers NetBox devices as Zabbix hosts.
*   `zbx_opsgenie_heartbeat.py` - Pushes a continuous heartbeat to Opsgenie.
*   `zbx_pagerduty_alert.py` - Routes critical events to PagerDuty via API v2.
*   `zbx_rundeck_webhook.py` - Fires Rundeck runbooks automatically.
*   `zbx_servicenow_add_worknote.py` - Injects real-time diagnostic logs into SNOW Incidents.
*   `zbx_servicenow_change_request.py` - Opens a Pre-approved Standard Change Request.
*   `zbx_servicenow_check_approval.py` - Pauses auto-remediation until a manager approves the SNOW Change.
*   `zbx_servicenow_check_maintenance.py` - Queries SNOW CMDB to suppress alerts during Change windows.
*   `zbx_servicenow_cmdb_sync.py` - Registers discovered Zabbix hosts into SNOW CMDB tables.
*   `zbx_servicenow_create_outage.py` - Creates Outage records for SLA calculations.
*   `zbx_servicenow_create_problem.py` - Opens a Problem ticket for root-cause analysis.
*   `zbx_servicenow_enrich_tags.py` - Dynamically maps SNOW Business Services into Zabbix tags.
*   `zbx_servicenow_escalate_incident.py` - Escalates SNOW incidents if a trigger remains active.
*   `zbx_servicenow_event.py` - Sends native ITOM Events allowing SNOW to handle correlation.
*   `zbx_servicenow_get_oncall.py` - Queries SNOW On-Call Scheduling API to route notifications.
*   `zbx_servicenow_incident.py` - Creates legacy ServiceNow Incidents (INC).
*   `zbx_servicenow_kb_link.py` - Searches SNOW KB and injects the article link into the incident.
*   `zbx_servicenow_major_incident.py` - Interacts with MIM module to promote War Room Major Incidents.
*   `zbx_servicenow_order_ritm.py` - Automatically orders Service Catalog Items (RITM) via API.
*   `zbx_servicenow_pause_sla.py` - Puts an incident to 'On Hold' to pause SLA clocks.
*   `zbx_servicenow_resolve.py` - Automatically updates and resolves SNOW Incidents upon recovery.
*   `zbx_servicenow_sctask.py` - Opens non-urgent Service Catalog Tasks (SCTASK).
*   `zbx_servicenow_secops_vuln.py` - Opens Vulnerable Items (VIT) for CVEs/security flaws.
*   `zbx_servicenow_sys_attachment.py` - Uploads diagnostic logs directly via the Attachment API.
*   `zbx_servicenow_warranty_lld.py` - Discovers hardware assets and imports warranty dates into Zabbix.
*   `zbx_statuspage_updater.py` - Updates Atlassian Statuspage components to "Degraded".

### 🚀 `apm-and-performance/` (AppDynamics)
*   `zbx_appdynamics_active_violations.py` - Polls AppDynamics for active Health Rule violations.
*   `zbx_appdynamics_alert_handler.py` - Translates AppDynamics webhooks into Zabbix Trapper alerts.
*   `zbx_appdynamics_app_export.py` - Generates MD5 hash of app config to track Config Drift.
*   `zbx_appdynamics_bt_lld.py` - LLD for Business Transactions (BTs).
*   `zbx_appdynamics_db_agent_lld.py` - Discovers DB Visibility Agents.
*   `zbx_appdynamics_exceptions_monitor.py` - Tracks absolute counts of code Exceptions.
*   `zbx_appdynamics_health_rules_lld.py` - Discovers and tracks AppDynamics Health Rules.
*   `zbx_appdynamics_information_points_lld.py` - LLD for custom Information Points.
*   `zbx_appdynamics_jmx_metrics.py` - Extracts JMX Heap/GC data directly from AppDynamics.
*   `zbx_appdynamics_license_usage.py` - Monitors AppDynamics license unit consumption.
*   `zbx_appdynamics_machine_agent_lld.py` - Discovers Machine Agents across the controller.
*   `zbx_appdynamics_metrics_master.py` - Polls core "Golden Signals" (Response Time, CPM, Errors).
*   `zbx_appdynamics_nodes_lld.py` - Discovers Application Tiers and Nodes.
*   `zbx_appdynamics_policy_violations.py` - Aggregates policy violations.
*   `zbx_appdynamics_push_event.py` - Pushes Zabbix infrastructure triggers into AppDynamics as Custom Events.
*   `zbx_appdynamics_service_endpoints_lld.py` - Mapped granular API routes/endpoints.
*   `zbx_appdynamics_synthetics_lld.py` - LLD for EUM Synthetic Jobs.
*   `zbx_appdynamics_tier_health.py` - Isolates Golden Signals for a specific Tier/Microservice.

### 🧠 `dynatrace-integration/`
*   `zbx_dynatrace_active_problems.py` - Polls Davis AI for open infrastructure/application problems.
*   `zbx_dynatrace_activegate_lld.py` - Discovers and monitors routing ActiveGates.
*   `zbx_dynatrace_app_apdex.py` - Returns the Apdex user experience score for Web/Mobile apps.
*   `zbx_dynatrace_appsec_vulnerabilities.py` - Counts active Critical/High runtime vulnerabilities.
*   `zbx_dynatrace_custom_metric_ingest.py` - Injects custom Zabbix metrics directly into Dynatrace.
*   `zbx_dynatrace_db_service_health.py` - Tracks SQL response times from monitored DB Services.
*   `zbx_dynatrace_ddu_consumption.py` - FinOps: Tracks Davis Data Units (DDU) consumption.
*   `zbx_dynatrace_host_cpu_steal.py` - Extracts Cloud VM CPU Steal Time percentage.
*   `zbx_dynatrace_log_errors_monitor.py` - Executes DQL to count log exceptions in Log Management v2.
*   `zbx_dynatrace_network_retransmissions.py` - Extracts OS-level TCP retransmission rates.
*   `zbx_dynatrace_oneagent_health_lld.py` - Audits Host OneAgents to ensure monitoring is active.
*   `zbx_dynatrace_process_group_health.py` - Verifies active instances within a Process Group.
*   `zbx_dynatrace_process_group_lld.py` - Discovers clustered Process Groups.
*   `zbx_dynatrace_push_deployment.py` - Injects CI/CD Custom Deployment events into the timeline.
*   `zbx_dynatrace_push_event.py` - Pushes critical Zabbix alerts into Dynatrace for root-cause correlation.
*   `zbx_dynatrace_rum_live_sessions.py` - Returns the exact number of active human RUM sessions.
*   `zbx_dynatrace_service_golden_signals.py` - Queries the API v2 for a service's Golden Signals.
*   `zbx_dynatrace_slo_status.py` - Monitors SLI compliance percentage and remaining Error Budgets.
*   `zbx_dynatrace_synthetic_health.py` - Collects success rate and duration of Synthetic tests.
*   `zbx_dynatrace_synthetic_monitors_lld.py` - Discovers Synthetic Browser and HTTP monitors.

### 🪵 `log-analytics-and-siem/` (Splunk)
*   `zbx_splunk_apps_lld.py` - Audits all installed Splunk Apps and Add-ons.
*   `zbx_splunk_daemon_cpu.py` - Tracks native resource utilization of `splunkd`.
*   `zbx_splunk_datamodel_acceleration.py` - Ensures Data Models are accelerating properly.
*   `zbx_splunk_datamodels_lld.py` - LLD for Splunk Data Models.
*   `zbx_splunk_deployment_clients_lld.py` - Discovers Universal Forwarders attached to Deployment Server.
*   `zbx_splunk_deployment_server_total.py` - Tracks total active phoning-home forwarders.
*   `zbx_splunk_hec_alert.py` - Webhook: Pushes native Zabbix Alerts into Splunk via HEC.
*   `zbx_splunk_hec_metric.py` - Webhook: Pushes performance metrics into Splunk Metric Indexes.
*   `zbx_splunk_hec_token_status.py` - Audits HEC tokens to ensure they are enabled.
*   `zbx_splunk_hec_tokens_lld.py` - Discovers configured HTTP Event Collectors.
*   `zbx_splunk_index_event_count.py` - Tracks absolute number of events ingested per index.
*   `zbx_splunk_index_size.py` - Monitors Splunk index disk size growth.
*   `zbx_splunk_indexes_lld.py` - LLD for active data indexes.
*   `zbx_splunk_indexer_cluster_status.py` - Verifies Indexer Cluster Replication/Search factors.
*   `zbx_splunk_kvstore_health.py` - Checks the status of the internal MongoDB (KV Store).
*   `zbx_splunk_license_capacity.py` - Returns total purchased ingestion capacity in GB.
*   `zbx_splunk_license_usage.py` - Tracks daily Splunk license consumption percentage.
*   `zbx_splunk_license_warnings.py` - Counts active soft-limit license warnings.
*   `zbx_splunk_orphan_searches.py` - Discovers scheduled searches left behind by disabled users.
*   `zbx_splunk_peer_status.py` - Checks connection status of distributed search peers.
*   `zbx_splunk_roles_total.py` - Audits the total number of RBAC roles.
*   `zbx_splunk_search_concurrency.py` - Monitors active historical searches to prevent exhaustion.
*   `zbx_splunk_search_job_status.py` - Checks the dispatch state of a remote search job.
*   `zbx_splunk_search_peers_lld.py` - LLD for Search Head distributed peers.
*   `zbx_splunk_shc_status.py` - Evaluates health and Captaincy of a Search Head Cluster.
*   `zbx_splunk_system_messages.py` - Extracts critical GUI bulletin warnings.
*   `zbx_splunk_tcp_inputs.py` - Counts active raw TCP listening ports.
*   `zbx_splunk_trigger_saved_search.py` - Triggers a Saved Search programmatically from Zabbix.
*   `zbx_splunk_user_status.py` - Detects if a Splunk user account is locked out.
*   `zbx_splunk_users_lld.py` - Discovers all local authentication users.

### 🐶 `datadog-integration/`
*   `zbx_datadog_active_downtimes.py` - Tracks global count of active maintenance downtimes.
*   `zbx_datadog_active_incidents.py` - Monitors active incidents in Datadog Incident Management.
*   `zbx_datadog_active_monitors.py` - Returns absolute counts of monitors in 'Alert' or 'Warn'.
*   `zbx_datadog_apm_services_lld.py` - Discovers APM Service dependencies.
*   `zbx_datadog_create_incident.py` - Automates the creation of a Datadog Incident.
*   `zbx_datadog_custom_metric_query.py` - Universal Query: Executes any native Datadog query.
*   `zbx_datadog_dashboards_lld.py` - LLD for existing Datadog dashboards.
*   `zbx_datadog_host_mute_status.py` - Checks if a Datadog agent host is muted to mirror downtimes.
*   `zbx_datadog_hosts_lld.py` - Discovers all hosts monitored by the Datadog Agent.
*   `zbx_datadog_log_index_retention.py` - Audits Log Management indexes retention policies.
*   `zbx_datadog_log_indexes_lld.py` - LLD for discovering customized Log Indexes.
*   `zbx_datadog_mute_monitor.py` - Temporarily mutes a Datadog monitor before a Zabbix reboot.
*   `zbx_datadog_push_event.py` - Pushes native Zabbix alerts into the Datadog Event stream.
*   `zbx_datadog_push_metric.py` - Forwards physical/custom metrics into Datadog.
*   `zbx_datadog_rum_apps_lld.py` - LLD for RUM web and mobile applications.
*   `zbx_datadog_service_level_objectives_lld.py` - LLD for configured Service Level Objectives (SLOs).
*   `zbx_datadog_slo_status.py` - Polls SLI compliance percentage and Error Budget.
*   `zbx_datadog_synthetic_health.py` - Checks execution status of a Datadog Synthetic test.
*   `zbx_datadog_synthetics_lld.py` - LLD for Synthetic API and Browser tests.
*   `zbx_datadog_usage_summary.py` - FinOps: Monitors daily billed usage metrics preventing overruns.

### 📈 `grafana-integration/`
*   `zbx_grafana_admin_count.py` - Audits the Grafana user base for Server Admin privileges.
*   `zbx_grafana_admin_stats.py` - Collects absolute global metrics (Dashboards, Users, Alerts).
*   `zbx_grafana_alert_rules_lld.py` - LLD for Grafana Unified Alerting (GUA) rules.
*   `zbx_grafana_alert_status.py` - Polls the state (Normal, Pending, Firing) of a Grafana Alert.
*   `zbx_grafana_alert_templates_lld.py` - Audits configured HTML/Text notification templates.
*   `zbx_grafana_annotation_clear.py` - Clears a Grafana annotation when the Zabbix trigger resolves.
*   `zbx_grafana_annotation_push.py` - Injects Zabbix alerts as vertical red-line annotations.
*   `zbx_grafana_auth_saml_status.py` - Verifies SAML/SSO authentication status.
*   `zbx_grafana_contact_points_lld.py` - Discovers configured Alertmanager Contact Points.
*   `zbx_grafana_correlations_health.py` - Checks active status of trace-to-log correlations.
*   `zbx_grafana_correlations_lld.py` - Discovers configured Trace-to-Log correlations.
*   `zbx_grafana_create_silence.py` - Tells Grafana to silence specific host alerts during maintenance.
*   `zbx_grafana_dashboard_backup.py` - Extracts the pure JSON model of a dashboard for internal Zabbix backup.
*   `zbx_grafana_dashboard_permissions.py` - Security: Alerts if a dashboard grants "Edit" to "Viewers".
*   `zbx_grafana_dashboard_tags_lld.py` - Discovers dashboard tagging usage for taxonomy.
*   `zbx_grafana_dashboard_versions.py` - Audits revision history to track database bloat.
*   `zbx_grafana_dashboards_lld.py` - LLD for all provisioned and UI-created dashboards.
*   `zbx_grafana_datasource_health.py` - Checks if a mapped Datasource is reachable.
*   `zbx_grafana_datasource_permissions.py` - Enterprise: Audits custom permissions tied to data sources.
*   `zbx_grafana_datasources_lld.py` - LLD for all configured data sources.
*   `zbx_grafana_db_size.py` - Monitors SQLite database size.
*   `zbx_grafana_folder_permissions.py` - Security: Detects permission leaks in restricted folders.
*   `zbx_grafana_folders_lld.py` - LLD for Grafana folder hierarchies.
*   `zbx_grafana_global_quotas.py` - Returns global server limitations (max users/orgs).
*   `zbx_grafana_health.py` - `/api/health` polling.
*   `zbx_grafana_legacy_apikeys_lld.py` - Security: Discovers deprecated legacy API Keys.
*   `zbx_grafana_library_panels_lld.py` - Discovers reusable Library Panels.
*   `zbx_grafana_mute_timings_lld.py` - Discovers configured Mute Timings in Alerting.
*   `zbx_grafana_org_quotas.py` - Audits target limitations specific to a tenant.
*   `zbx_grafana_org_users_count.py` - Tracks exact user count assigned to an organization.
*   `zbx_grafana_orgs_lld.py` - LLD for Multi-tenancy Organizations.
*   `zbx_grafana_playlists_lld.py` - Discovers NOC Playlists.
*   `zbx_grafana_plugin_updates.py` - Audits plugins for available updates.
*   `zbx_grafana_plugins_lld.py` - LLD for installed Grafana plugins.
*   `zbx_grafana_preferences.py` - Audits global organization preferences (Home Dashboard).
*   `zbx_grafana_public_dashboards_lld.py` - Security: Audits publicly exposed dashboards.
*   `zbx_grafana_report_status.py` - Checks execution status of scheduled PDF reports.
*   `zbx_grafana_reports_lld.py` - LLD for Scheduled Reports.
*   `zbx_grafana_sa_tokens_count.py` - Counts active Bearer Tokens on Service Accounts.
*   `zbx_grafana_server_settings_audit.py` - Ensures `allow_sign_up` is strictly disabled.
*   `zbx_grafana_service_accounts_lld.py` - Discovers Grafana Service Accounts.
*   `zbx_grafana_short_urls_lld.py` - Discovers shortened URLs generated by Grafana Share.
*   `zbx_grafana_silences_lld.py` - Audits active silences in Grafana Alertmanager.
*   `zbx_grafana_snapshots_lld.py` - Audits public and local dashboard snapshots.
*   `zbx_grafana_sso_sync_status.py` - Checks LDAP/SAML sync status.
*   `zbx_grafana_team_lld.py` - Discovers configured Grafana Teams.
*   `zbx_grafana_team_members_count.py` - Calculates the user count of a specific Grafana Team.
*   `zbx_grafana_user_quotas.py` - Audits limitations applied to individual users.
*   `zbx_grafana_user_stars.py` - Checks if critical NOC dashboards are actively "starred".
*   `zbx_grafana_users_lld.py` - LLD for local users for authentication tracking.

### 🐙 `devsecops-and-cicd/` (GitHub)
*   `zbx_github_api_ratelimit.py` - Monitors the organization's core API rate limits.
*   `zbx_github_billing_minutes.py` - Tracks paid CI/CD execution minutes to govern FinOps thresholds.
*   `zbx_github_billing_storage.py` - Tracks GitHub Packages and LFS storage capacity billing.
*   `zbx_github_dependabot_alerts.py` - SecOps: Counts active, unpatched vulnerabilities.
*   `zbx_github_repo_size.py` - Audits the physical size of tracked repositories.
*   `zbx_github_runner_status.py` - Ensures self-hosted CI/CD runners remain online.
*   `zbx_github_runners_lld.py` - LLD for automatically discovering deployed self-hosted runners.
*   `zbx_github_stale_prs.py` - Agile metrics: Counts abandoned Pull Requests.
*   `zbx_github_traffic_clones.py` - SecOps anomaly detection: Alerts on unusual clone traffic spikes.
*   `zbx_github_workflow_failures.py` - Critical Pipeline Monitor: Alerts if production workflow fails.

### 🗝️ `security-and-secrets/` (HashiCorp Vault)
*   `zbx_vault_audit_log_health.py` - Ensures at least one audit device is functional.
*   `zbx_vault_auth_methods_lld.py` - Discovers configured authentication engines.
*   `zbx_vault_ha_leader.py` - Identifies the 'Active' master and 'Standby' replicas.
*   `zbx_vault_license_status.py` - Tracks Vault Enterprise license expiration.
*   `zbx_vault_metrics_memory.py` - Extracts Prometheus-formatted telemetry for memory consumption.
*   `zbx_vault_pki_cert_expiry_lld.py` - LLD for internal PKI Engine certificates to track expirations.
*   `zbx_vault_seal_status.py` - Alerts if a Vault node enters a 'Sealed' state.
*   `zbx_vault_secret_engines_lld.py` - Discovers mounted secrets engines dynamically.
*   `zbx_vault_step_down_action.py` - Webhook: Forces a problematic node to drop leadership.
*   `zbx_vault_token_accessors_count.py` - Monitors active token counts to detect sprawl/leaks.

### ⚖️ `application-delivery-controllers/` (F5 BIG-IP)
*   `zbx_f5_cert_expiry_lld.py` - LLD for SSL certificates, calculating remaining validity days.
*   `zbx_f5_config_sync.py` - Checks Active/Standby synchronization status.
*   `zbx_f5_failover_status.py` - Audits High Availability unit state (ACTIVE or STANDBY).
*   `zbx_f5_pool_members_health.py` - Compares total pool members against active members.
*   `zbx_f5_pools_lld.py` - Discovers configured Server Pools and routing partitions.
*   `zbx_f5_virtual_servers_lld.py` - LLD for Virtual Servers (VIPs) and IP addresses.
*   `zbx_f5_vs_status.py` - Retrieves the precise Availability State of critical Virtual Servers.

### 🛡️ `next-gen-firewalls/` (Palo Alto Networks)
*   `zbx_paloalto_bgp_peers_lld.py` - Discovers dynamic BGP peer statuses across Virtual Routers.
*   `zbx_paloalto_ha_state.py` - Monitors Local and Peer High Availability status.
*   `zbx_paloalto_pending_commits.py` - Configuration Audit: Alerts on uncommitted rule changes.
*   `zbx_paloalto_session_utilization.py` - Calculates the percentage of the global session table utilized.
*   `zbx_paloalto_threat_count.py` - Pulls recent threat detection events for SOC visualization.
*   `zbx_paloalto_wildfire_status.py` - Ensures continuous connectivity to the WildFire cloud engine.

---

## 🚀 Quick Start & Deployment Guide

Because this repository bridges multiple operational domains, the deployment strategy changes depending on whether Zabbix is **collecting data (Polling)** or **executing an action (Webhooks)**.

### 1. Prerequisites
Ensure the environment executing the scripts (Zabbix Server, Proxy, or Agent) has the required dependencies:
*   `python3` and `pip` packages: `requests`, `boto3`, `pyVim`
*   `jq` (for JSON parsing in bash scripts)
*   `snmpget` / `snmpwalk` (for legacy hardware monitoring)

### 2. Local OS/Hardware Metrics: Zabbix Agent (UserParameters)
Used for scripts that must run directly on the target machine (e.g., Docker, Linux OS, local SQLite sizes).

1. Copy the script to the monitored host (e.g., `/etc/zabbix/scripts/`).
2. Make the script executable: 
        
        chmod +x /etc/zabbix/scripts/script_name.sh
        
3. Add the UserParameter to `zabbix_agentd.conf` (or `zabbix_agent2.conf`):
        
        UserParameter=custom.metric.name[*], /etc/zabbix/scripts/script_name.sh $1 $2
        
4. **Restart the Zabbix Agent service.** (Crucial: UserParameters only load on startup).
5. In the Zabbix UI, create an item of type **Zabbix agent**.

### 3. API Polling & Integrations: External Checks
Used for SaaS platforms, Clouds, and APIs where installing an agent is impossible (e.g., Datadog, Splunk, GitHub, F5, Palo Alto). **These scripts run from the Zabbix Server or Zabbix Proxy.**

1. Copy the script to your `ExternalScripts` path (default: `/usr/lib/zabbix/externalscripts/`).
2. Ensure the file is owned by the `zabbix` user and executable:
        
        chown zabbix:zabbix /usr/lib/zabbix/externalscripts/script_name.py
        chmod +x /usr/lib/zabbix/externalscripts/script_name.py
        
3. *(No service restart required).*
4. In the Zabbix UI, create an item of type **External check**.
5. In the **Key** field, reference the script and pass macros: `script_name.py["{$API_URL}","{$API_TOKEN}"]`.

### 4. Bulk Data Processing: Master Items & LLD
For scripts that return large JSON payloads (e.g., AWS Billing, Kubernetes Pods, Grafana Dashboards).

1. Create the **Master Item** (External Check) and set the **Type of information** to `Text`.
2. Create a **Discovery Rule** (Type: `Dependent item`), pointing to the Master Item.
3. Configure **LLD macros** mapping the JSON keys (e.g., `{#DASHBOARD_ID}` ➔ `$.uid`).
4. Create **Item prototypes** (Type: `Dependent item` pointing to the Master Item).
5. In the Item Prototype, add a **JSONPath Preprocessing** step to extract the specific metric.

### 5. Event-Driven Automation: Webhooks & AlertScripts
Scripts inside categories like `integrations-and-itsm/` act upon events (Pushing annotations to Grafana, opening ServiceNow tickets, muting Datadog).

1. Copy the script to your `AlertScriptsPath` on the Zabbix Server (default: `/usr/lib/zabbix/alertscripts/`).
2. Make the script executable (`chmod +x`).
3. In the Zabbix UI, go to **Administration > Media types** and create a new media type.
4. Set Type to **Script**, enter the script name, and define the parameters that will be passed to it from the event (e.g., `{HOST.NAME}`, `{EVENT.SEVERITY}`, `{EVENT.ID}`).
5. Go to **Configuration > Actions > Trigger actions** and create an action that triggers this Media Type when a problem occurs.

### 🔐 Security & Operations Best Practices
*   **Secret Macros:** Never hardcode Bearer tokens, GitHub Personal Access Tokens (PATs), or API keys in the scripts. Pass them as arguments using Zabbix **Secret Text Macros** (`{$SECRET_TOKEN}`).
*   **Sudoers:** If a local bash script requires root (e.g., `lsblk`, `smartctl`), use `visudo` to grant specific permissions to the `zabbix` user: `zabbix ALL=(ALL) NOPASSWD: /usr/sbin/smartctl`. **Never run the Zabbix Agent as root.**
*   **API Throttling:** When polling heavily rate-limited APIs (like GitHub or SaaS APMs), adjust update intervals to `5m` or `15m` to prevent 429 Too Many Requests errors. Use Master Items to fetch all data in a single API call.