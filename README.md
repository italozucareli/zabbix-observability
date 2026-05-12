# 👁️ Zabbix Enterprise Observability & Automation Toolkit

A comprehensive, SRE-grade repository of over 200 advanced scripts, Master Items, Low-Level Discovery (LLD) rules, and Event-Driven Automation webhooks designed to elevate Zabbix from a simple monitoring tool into a complete IT Operations Management (ITOM) platform.

This toolkit focuses on **Bulk Data Collection** (via REST APIs and native JSON payloads) and **Closed-Loop Automation** (ITSM ticketing, auto-remediation, and ChatOps).

---

## 🏗️ Architecture & Philosophy

To ensure scalability in mission-critical environments, these scripts adopt the following principles:
*   **Zero-Overhead Polling:** Scripts make a single, bulk call to an equipment or API, returning a complete JSON payload. Zabbix processes this internally via LLD and Dependent Items, bypassing the need for hundreds of individual connections.
*   **Dynamic Discovery:** Reduces manual configuration. VPNs, BGP peers, Kubernetes pods, Docker Swarm services, and UPS phases are discovered dynamically.
*   **Event-Driven Automation:** Monitoring is only half the battle. This toolkit includes scripts that run as Zabbix Actions to automatically open/resolve ServiceNow incidents, trigger Ansible AWX playbooks, or alert PagerDuty.

---

## 📂 Repository Structure & Scripts

### ☁️ `cloud-infrastructure/`
Scripts for monitoring public clouds and managed services.
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
Advanced metrics for Docker, Docker Swarm, and Kubernetes Control Plane & Governance.
*   `docker_container_lld.py` - Docker container discovery and stats via socket.
*   `docker_container_state.sh` - Counts exited or crashed Docker containers.
*   `k8s_node_ready.py` - Checks Kubernetes nodes ready status.
*   `k8s_pod_status_lld.sh` - LLD for Kubernetes pods and restart counts.
*   `zbx_docker_cpu_usage.sh` - Gets CPU usage % for a specific container.
*   `zbx_docker_health_status.sh` - Docker internal healthcheck status.
*   `zbx_docker_mem_usage.sh` - Gets memory usage for a specific container.
*   `zbx_docker_restart_count.sh` - Tracks specific container restart counts.
*   `zbx_k8s_admission_webhooks.py` - LLD for validating/mutating webhook configurations.
*   `zbx_k8s_api_latency.py` - Synthetic micro-transaction to measure K8s API Control Plane latency.
*   `zbx_k8s_apiservice_health.py` - Health check for aggregated API services (e.g., metrics-server).
*   `zbx_k8s_apiserver_metrics.py` - Aggregates 5xx HTTP errors directly from the kube-apiserver `/metrics`.
*   `zbx_k8s_coredns_changes.py` - Tracks CoreDNS ConfigMap hash changes to prevent silent DNS outages.
*   `zbx_k8s_crd_versions.py` - Audits CRDs for deprecated API versions (e.g., v1beta1).
*   `zbx_k8s_cronjob_status.py` - LLD for CronJobs, tracking active executions and suspended states.
*   `zbx_k8s_csr_pending.py` - Counts Certificate Signing Requests (CSRs) pending manual approval.
*   `zbx_k8s_daemonset_misscheduled.py` - Detects DaemonSets trying to run on nodes with mismatched Taints.
*   `zbx_k8s_daemonset_ready.sh` - Kubernetes DaemonSet readiness monitor.
*   `zbx_k8s_deployment_replicas.sh` - Kubernetes Deployment replica availability %.
*   `zbx_k8s_deployment_sync.py` - Identifies stuck Deployments by comparing generation vs observedGeneration.
*   `zbx_k8s_endpoints_capacity.py` - Monitors Services approaching the 1000 endpoints limit.
*   `zbx_k8s_evicted_pods.py` - Counts pods stuck in the Evicted state, tracking cluster garbage.
*   `zbx_k8s_helm_secrets.py` - Decodes Helm v3 Secrets to discover and monitor release deployment statuses.
*   `zbx_k8s_hpa_events.py` - Aggregates horizontal scaling events (scale up/down) frequency over time.
*   `zbx_k8s_hpa_status.py` - LLD for Horizontal Pod Autoscalers, tracking current vs desired vs max replicas.
*   `zbx_k8s_ingress_classes.py` - Discovers and monitors active Ingress Classes (nginx, alb, traefik).
*   `zbx_k8s_ingress_status.sh` - Validates K8s Ingress provisioned IPs.
*   `zbx_k8s_ingress_tls_expiry.py` - Directly parses kubernetes.io/tls Secrets to calculate SSL expiration days.
*   `zbx_k8s_job_failures.py` - Discovers Batch Jobs and alerts on silent task failures.
*   `zbx_k8s_kubelet_versions.py` - Audits node Kubelet versions to detect failed cluster upgrades.
*   `zbx_k8s_limit_ranges.py` - Checks if Namespaces enforce default CPU/Memory LimitRanges.
*   `zbx_k8s_namespace_governance.py` - Audits Namespaces for mandatory compliance annotations/labels.
*   `zbx_k8s_node_conditions.py` - Monitors silent Node conditions like MemoryPressure and DiskPressure.
*   `zbx_k8s_node_cpu_alloc.sh` - Kubernetes node CPU allocation percentage.
*   `zbx_k8s_node_taints.py` - Tracks NoSchedule/NoExecute Taints applied to cluster nodes.
*   `zbx_k8s_oomkilled_pods.py` - Scans all pods to detect containers terminated due to OOMKilled errors.
*   `zbx_k8s_pdb_status.py` - Monitors Pod Disruption Budgets (PDBs) to ensure safe node draining.
*   `zbx_k8s_pod_restarts.sh` - Total restarts across all containers in a pod.
*   `zbx_k8s_priority_classes.py` - Discovers custom Priority Classes and their relative scheduling weights.
*   `zbx_k8s_pv_status.py` - LLD for Persistent Volumes (PVs), alerting on Failed or Released phases.
*   `zbx_k8s_pvc_usage.sh` - K8s Persistent Volume Claim disk usage %.
*   `zbx_k8s_replicaset_orphans.py` - Counts orphaned or outdated ReplicaSets consuming etcd resources.
*   `zbx_k8s_resource_quotas.py` - Monitors ResourceQuota utilization (CPU/RAM limits) per Namespace.
*   `zbx_k8s_service_nodeports.py` - Discovers reserved physical NodePorts to prevent port collisions.
*   `zbx_k8s_statefulset_revisions.py` - Detects StatefulSet updates that are stuck mid-rollout.
*   `zbx_k8s_storage_classes.py` - Discovers available StorageClasses and their underlying provisioners.
*   `zbx_k8s_warning_events.py` - Aggregates and categorizes cluster-wide Warning events.
*   `zbx_swarm_cluster_health.py` - Master Item tracking Docker Swarm Control Plane health and Raft consensus quorum.
*   `zbx_swarm_dangling_images.sh` - Identifies untagged/orphaned images causing silent disk leaks on workers.
*   `zbx_swarm_dangling_volumes.sh` - Identifies unattached local volumes left behind by removed services.
*   `zbx_swarm_global_tasks_health.sh` - Counts failing `global` mode services not running the required 1 task per node.
*   `zbx_swarm_manager_leader.sh` - Identifies if the polled Manager node is the active Raft Leader.
*   `zbx_swarm_networks_lld.py` - LLD for Swarm overlay networks, discovering multi-host networking scopes.
*   `zbx_swarm_node_drift_lld.py` - LLD for cluster nodes tracking Docker Engine versions to detect version drift.
*   `zbx_swarm_node_labels_lld.py` - Discovers assigned Node Labels, ensuring placement constraints function properly.
*   `zbx_swarm_nodes_lld.py` - LLD for Swarm nodes, tracking Ready status and Active availability.
*   `zbx_swarm_pending_tasks.sh` - Counts tasks stuck in 'Pending', alerting on cluster resource starvation.
*   `zbx_swarm_published_ports_lld.py` - LLD mapping Swarm Services to their exposed external ingress ports.
*   `zbx_swarm_quorum_health.sh` - Verifies Raft Manager Quorum health (Total vs Reachable).
*   `zbx_swarm_rejected_tasks.sh` - Counts 'Rejected' tasks indicating port collisions or volume mount failures.
*   `zbx_swarm_secrets_configs_audit.sh` - Returns counts of Swarm Secrets and Configs to monitor bloat.
*   `zbx_swarm_service_tasks_failed.sh` - Counts historical task failures (CrashLoops) for a specific Swarm service.
*   `zbx_swarm_services_lld.py` - Master Item LLD that discovers Stacks and Services, returning Running vs Desired replicas.
*   `zbx_swarm_worker_local_tasks_lld.py` - SRE Bridge: Runs on any Worker to map local containers to their parent Swarm Service Name.

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
Deep monitoring for Datacenter Power Infrastructure, UPS (Nobreaks), ATS, and PDUs.
*   `zbx_apc_ats_redundancy.sh` - Alerts if an ATS loses its backup power source redundancy.
*   `zbx_apc_ats_source_status.sh` - Checks synchronization and active power source on APC ATS units.
*   `zbx_apc_humidity_temp.sh` - Consolidated JSON payload for rack temp/humidity via APC probes.
*   `zbx_apc_nmc_api_master.py` - Reads native REST API data from modern APC NMC v3 cards via HTTPS.
*   `zbx_apcupsd_events_parser.sh` - Parses `/var/log/apcupsd.events` to trigger alerts on critical power events.
*   `zbx_apcupsd_master.py` - Master Item to convert all `apcaccess` output into a structured JSON payload.
*   `zbx_delta_ups_battery_health.sh` - Specific Delta UPS MIB monitor for predictive battery replacement.
*   `zbx_eaton_xups_health.sh` - Uses proprietary Eaton XUPS-MIB to track deep hardware states.
*   `zbx_nut_active_alarms.sh` - Extracts the exact real-time alarm string broadcasted by the NUT daemon.
*   `zbx_nut_ups_discovery.py` - LLD script to dynamically discover UPS units managed by NUT.
*   `zbx_nut_ups_stats.py` - Master Item to extract metrics from a specific NUT-managed UPS.
*   `zbx_sms_ups_avr_state.sh` - Monitors Automatic Voltage Regulator (AVR) Boost/Buck states for SMS hardware.
*   `zbx_snmp_generator_status.sh` - Tracks if the UPS dry contacts identify the backup generator as the active source.
*   `zbx_snmp_pdu_bank_status_lld.sh` - LLD for internal PDU banks/breakers to monitor segmented power cuts.
*   `zbx_snmp_pdu_outlets_lld.sh` - LLD for discovering Smart PDU outlets and server power port states.
*   `zbx_snmp_pdu_power_draw.sh` - Consolidates the total amperage drawn across an entire managed PDU.
*   `zbx_snmp_rfc1628_health.sh` - Universal SNMP UPS monitor (RFC 1628) for Battery Status, Charge %, and Minutes Remaining.
*   `zbx_snmp_ups_alarms_lld.sh` - SNMP LLD to discover and track active hardware/environmental alarms.
*   `zbx_snmp_ups_audible_alarm.sh` - Monitors if the UPS physical audible alarm (beeper) is currently sounding.
*   `zbx_snmp_ups_bad_battery_count.sh` - Counts the number of defective battery cartridges in modular UPS systems.
*   `zbx_snmp_ups_battery_current.sh` - Tracks battery bus Amperage to detect active charge or discharge states.
*   `zbx_snmp_ups_battery_temp.sh` - Monitors internal battery temperature (Celsius) to prevent thermal runaway.
*   `zbx_snmp_ups_battery_voltage.sh` - Reads DC bus voltage to ensure the charger is applying the correct float voltage.
*   `zbx_snmp_ups_bypass_voltage.sh` - Health check on the raw bypass line voltage.
*   `zbx_snmp_ups_efficiency.sh` - Calculates or reads the internal power efficiency percentage of the UPS inverter.
*   `zbx_snmp_ups_env_probes_lld.sh` - Discovers external environmental probes attached to the UPS.
*   `zbx_snmp_ups_fan_status_lld.sh` - LLD to monitor individual cooling fan statuses to prevent overheating.
*   `zbx_snmp_ups_load_capacity.sh` - Extracts the current inverter load percentage for capacity planning.
*   `zbx_snmp_ups_output_current.sh` - Tracks the exact Amperage being pulled by the servers.
*   `zbx_snmp_ups_phases_lld.sh` - LLD for 3-Phase UPS systems, discovering L1/L2/L3.
*   `zbx_snmp_ups_power_quality.sh` - Consolidates I/O Voltage and Frequency to detect grid anomalies.
*   `zbx_snmp_ups_real_power.sh` - Reads the True Power (Watts) currently being consumed.
*   `zbx_snmp_ups_selftest.sh` - Checks the status and completion results of automated battery self-tests.
*   `zbx_snmp_ups_test_date.sh` - Parses the exact date/timestamp of the last deep hardware diagnostic.
*   `zbx_ups_battery_lifecycle.sh` - Tracks battery age in months based on installation date.
*   `zbx_ups_energy_meter.sh` - Extracts total accumulated kWh meter to calculate PUE.
*   `zbx_vertiv_ups_alarms.sh` - Vertiv/Liebert specific MIB monitor for critical active conditions.

### 🌐 `network-and-routing/`
*   `check_bgp_peers.sh` - BGP peer established state via SNMP.
*   `check_ospf_neighbors.sh` - OSPF neighbor full state via SNMP.
*   `cisco_board_pro_status.py` - Cisco endpoint standby status via xAPI.
*   `cisco_meraki_devices_lld.py` - LLD for Cisco Meraki devices via API.
*   `interface_errors_rate.sh` - Linux interface RX errors parser.
*   `mikrotik_bgp_peer_lld.sh` - LLD for MikroTik BGP peers via REST API.
*   `mtr_zabbix_bridge.py` - Advanced path observability and packet loss via MTR.
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
*   `zbx_linux_open_files.sh` - Total open file descriptors in the OS.
*   `zbx_linux_process_threads.sh` - Total OS threads count.
*   `zbx_linux_swap_io.sh` - Swap memory I/O paging metrics.
*   `zbx_linux_uptime_seconds.sh` - Exact system uptime in seconds.
*   `zbx_tcp_socket_states.sh` - TCP socket states counter (ESTABLISHED, TIME_WAIT).

### 🛡️ `security-and-vpn/`
*   `active_ssh_sessions.sh` - Active SSH user sessions count.
*   `check_open_ports.sh` - Validates if a specific local port is listening.
*   `failed_ssh_logins.sh` - Brute-force SSH failed logins counter.
*   `file_checksum_monitor.sh` - SHA256 critical file checksum monitor.
*   `openvpn_sessions_lld.py` - LLD for connected OpenVPN users and bandwidth.
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
*   `http_status_code.sh` - HTTP status code monitor (e.g., 200, 404).
*   `mail_queue_size.sh` - Postfix mail queue size counter.
*   `nginx_upstream_lld.sh` - LLD for Nginx upstream backend status.
*   `ssl_sni_discovery_lld.sh` - LLD for SSL certificates via Nginx SNI configs.
*   `web_string_match.sh` - Verifies if a specific string exists on a web page.
*   `zbx_m365_service_health.py` - Microsoft 365 services health status via Graph API.
*   `zbx_ssl_ocsp_chain.py` - SSL OCSP revocation and certificate chain validation.

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
Event-driven automation, ChatOps, and ITSM ticketing integrations to connect Zabbix with your workflows.
*   `zbx_awx_remediation.py` - Triggers Ansible Tower/AWX Job Templates for auto-remediation.
*   `zbx_glpi_ticket.py` - Automatically opens and categorizes Helpdesk tickets in GLPI via REST API.
*   `zbx_jira_ticket.py` - Opens Jira Service Management issues, mapping Zabbix tags to Jira labels.
*   `zbx_msteams_adaptive.py` - Pushes modern, color-coded alerts to Microsoft Teams using Adaptive Cards.
*   `zbx_netbox_sync.py` - Pulls active devices from NetBox and auto-registers them as hosts in Zabbix.
*   `zbx_opsgenie_heartbeat.py` - Pushes a continuous heartbeat to Opsgenie; if Zabbix dies, it alerts the on-call team.
*   `zbx_pagerduty_alert.py` - Routes critical Zabbix events to PagerDuty via API v2 for on-call escalation.
*   `zbx_rundeck_webhook.py` - Fires Rundeck runbooks automatically based on specific Zabbix trigger severities.
*   `zbx_servicenow_add_worknote.py` - Injects real-time diagnostic logs into an open SNOW Incident via Work Notes.
*   `zbx_servicenow_change_request.py` - Opens a Standard Change Request before Zabbix executes an auto-remediation.
*   `zbx_servicenow_check_approval.py` - Pauses auto-remediation actions until a manager approves the tied SNOW Change.
*   `zbx_servicenow_check_maintenance.py` - Queries SNOW CMDB to suppress alerts if the host is in an approved Change window.
*   `zbx_servicenow_cmdb_sync.py` - Registers newly discovered Zabbix hosts directly into SNOW CMDB tables.
*   `zbx_servicenow_create_outage.py` - Links critical triggers to Business Services, creating Outage records for SLA.
*   `zbx_servicenow_create_problem.py` - Opens a Problem ticket for root-cause analysis when Zabbix detects flapping.
*   `zbx_servicenow_enrich_tags.py` - Queries SNOW to dynamically map affected downstream Business Services into Zabbix tags.
*   `zbx_servicenow_escalate_incident.py` - Escalates open SNOW incidents if a Zabbix trigger remains active for hours.
*   `zbx_servicenow_event.py` - Sends native ITOM Events instead of Incidents, allowing SNOW to handle correlation.
*   `zbx_servicenow_get_oncall.py` - Queries SNOW On-Call Scheduling API to route notifications to the active shift engineer.
*   `zbx_servicenow_incident.py` - Creates ServiceNow Incidents (INC), mapping Zabbix severity to SNOW urgency.
*   `zbx_servicenow_kb_link.py` - Searches the SNOW KB using trigger keywords and injects the article link into the incident.
*   `zbx_servicenow_major_incident.py` - Interacts with MIM module to promote catastrophic alerts into War Room Major Incidents.
*   `zbx_servicenow_order_ritm.py` - Automatically orders Service Catalog Items (RITM) via API for automated provisioning.
*   `zbx_servicenow_pause_sla.py` - Puts an incident to 'On Hold (Awaiting Vendor)' to pause SLA clocks when ISPs fail.
*   `zbx_servicenow_resolve.py` - Automatically updates and resolves SNOW Incidents when Zabbix recovery operations trigger.
*   `zbx_servicenow_sctask.py` - Opens non-urgent Service Catalog Tasks (SCTASK) for preventative maintenance.
*   `zbx_servicenow_secops_vuln.py` - Integrates with SNOW SecOps to open Vulnerable Items (VIT) for CVEs/security flaws.
*   `zbx_servicenow_sys_attachment.py` - Uploads diagnostic logs directly into a SNOW incident via the Attachment API.
*   `zbx_servicenow_warranty_lld.py` - Discovers hardware assets in SNOW and imports warranty dates into Zabbix for predictive replacement.
*   `zbx_statuspage_updater.py` - Integrates with Atlassian Statuspage to automatically switch a component to "Degraded".

---

## 🚀 Quick Start Guide & Deployment Instructions

Because this repository covers both **Data Collection** (Polling) and **Closed-Loop Automation** (Alerting/ITSM), the deployment methods vary based on the script's purpose.

### 1. Prerequisites
Ensure your Zabbix Server/Proxy or Agent has the necessary dependencies installed:
*   `jq` (for JSON parsing in Bash scripts)
*   `python3` and `pip` packages: `requests`, `boto3`, `pyVim`, `pycurl`
*   `snmpget` / `snmpwalk` (Net-SNMP tools for Power & Network scripts)
*   `apcupsd` or `nut` (for specific local UPS monitoring)
*   `docker` cli access (Agent must be in the `docker` group for Swarm/Container scripts)

### 2. Data Collection: Zabbix Agent (UserParameters)
Use this method for local OS, Docker Swarm, and Database metrics.
1.  Copy the script to the monitored host (e.g., `/etc/zabbix/scripts/`).
2.  Make the script executable:

        chmod +x /etc/zabbix/scripts/script_name.sh

3.  Add the UserParameter to your `zabbix_agentd.conf`:

        UserParameter=custom.metric.name[*], /etc/zabbix/scripts/script_name.sh $1 $2

4.  Restart the Zabbix Agent. Create an item of type **Zabbix agent** with the key `custom.metric.name[arg1]`.

### 3. Data Collection: External Checks (Server/Proxy API Polling)
Use this method for REST APIs (K8s, ServiceNow CMDB pulls, Cloud providers, Modern APC NMC3).
1.  Copy the script to the `ExternalScripts` path on your Zabbix Server/Proxy (usually `/usr/lib/zabbix/externalscripts/`).
2.  Make the script executable:

        chmod +x /usr/lib/zabbix/externalscripts/script_name.py

3.  In the Zabbix UI, create an item of type **External check**.
4.  In the **Key** field, reference the script and pass macros as arguments: `script_name.py["{$API_URL}","{$API_TOKEN}"]`.

### 4. Zabbix Frontend: Master Items & LLD (JSON Parsing)
For scripts that return large JSON payloads (Bulk Data Collection):
1.  Create the **Master Item** (External Check or Agent) and set the **Type of information** to `Text`.
2.  Create a **Discovery Rule** (Type: `Dependent item`), pointing to the Master Item.
3.  Configure **LLD macros** mapping the JSON keys (e.g., `{#SERVICE_NAME}` ➔ `$.name`).
4.  Create **Item prototypes** (Type: `Dependent item` pointing to the Master Item).
5.  In the Item Prototype, add a **JSONPath Preprocessing** step to extract the specific metric (e.g., `$.data[?(@.name == "{#SERVICE_NAME}")].status.first()`).

### 5. Event-Driven Automation: AlertScripts & Webhooks (ITSM/Integrations)
Scripts in the `integrations-and-itsm/` directory DO NOT collect data. They act upon it.
1.  Copy the script to the `AlertScriptsPath` on your Zabbix Server (usually `/usr/lib/zabbix/alertscripts/`).
2.  Make the script executable (`chmod +x`).
3.  In the Zabbix UI, go to **Administration > Media types** and create a new media type.
4.  Set Type to **Script**, enter the script name, and define the parameters that will be passed to it (e.g., `{HOST.NAME}`, `{EVENT.SEVERITY}`, `{EVENT.ID}`).
5.  Go to **Configuration > Actions > Trigger actions** and create an action that triggers this Media Type when an event occurs.

### 💡 Security Best Practices
*   **Never hardcode passwords:** Always pass API tokens (ServiceNow, AWS, K8s) as arguments using Zabbix **Secret Macros** (`{$SECRET_TOKEN}`). This masks the values in the frontend.
*   **Sudo Privileges:** If a local script requires root (e.g., `smartctl`, `lsblk`), use `visudo` specifically for the `zabbix` user: `zabbix ALL=(ALL) NOPASSWD: /usr/sbin/smartctl`. Do not run the entire agent as root.
*   **API Rate Limiting:** When polling cloud providers or SaaS APIs, adjust update intervals carefully (e.g., `5m` or `10m`) to avoid HTTP 429 throttling limits.