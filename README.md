# 👁️ Zabbix Enterprise Observability Toolkit

A comprehensive repository of advanced scripts, Master Items, and Low-Level Discovery (LLD) rules designed to elevate Zabbix monitoring to Site Reliability Engineering (SRE) and Enterprise Implementation standards. 

This toolkit focuses on bulk data collection via APIs, native OS parsing, and JSON payloads, minimizing Zabbix Server polling overhead by avoiding basic one-by-one checks.

---

## 🏗️ Architecture & Philosophy

To ensure scalability in mission-critical environments, these scripts adopt the following principles:
*   **Master Items & JSON:** Scripts make a single call to the equipment or API, returning a complete JSON payload that Zabbix processes internally via LLD and Dependent Items.
*   **Dynamic Discovery:** Reduces manual configuration. IPsec tunnels, BGP peers, Docker containers, IIS pools, and cloud instances are discovered automatically.
*   **Zero-Overhead:** Relies on native OS tools (e.g., direct reading from `/proc` and `/sys` in Linux) to prevent overloading Zabbix pollers.

---

## 📂 Repository Structure & Scripts

The toolkit is divided into the following technological pillars:

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
Advanced metrics for Docker, Kubernetes Control Plane, Governance, and Orchestration.
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
*   `zbx_k8s_apiserver_metrics.py` - Aggregates 5xx HTTP errors directly from the kube-apiserver `/metrics` endpoint.
*   `zbx_k8s_coredns_changes.py` - Tracks CoreDNS ConfigMap hash changes to prevent silent DNS outages.
*   `zbx_k8s_crd_versions.py` - Audits Custom Resource Definitions (CRDs) for deprecated API versions (e.g., v1beta1).
*   `zbx_k8s_cronjob_status.py` - LLD for CronJobs, tracking active executions and suspended states.
*   `zbx_k8s_csr_pending.py` - Counts Certificate Signing Requests (CSRs) pending manual approval.
*   `zbx_k8s_daemonset_misscheduled.py` - Detects DaemonSets trying to run on nodes with mismatched Taints/Tolerations.
*   `zbx_k8s_daemonset_ready.sh` - Kubernetes DaemonSet readiness monitor.
*   `zbx_k8s_deployment_replicas.sh` - Kubernetes Deployment replica availability %.
*   `zbx_k8s_deployment_sync.py` - Identifies stuck Deployments by comparing generation vs observedGeneration.
*   `zbx_k8s_endpoints_capacity.py` - Monitors Services approaching the 1000 endpoints limit to prevent kube-proxy overload.
*   `zbx_k8s_evicted_pods.py` - Counts pods stuck in the Evicted state, tracking cluster garbage.
*   `zbx_k8s_helm_secrets.py` - Decodes Helm v3 Secrets to discover and monitor release deployment statuses.
*   `zbx_k8s_hpa_events.py` - Aggregates horizontal scaling events (scale up/down) frequency over time.
*   `zbx_k8s_hpa_status.py` - LLD for Horizontal Pod Autoscalers, tracking current vs desired vs max replicas.
*   `zbx_k8s_ingress_classes.py` - Discovers and monitors active Ingress Classes (nginx, alb, traefik).
*   `zbx_k8s_ingress_status.sh` - Validates K8s Ingress provisioned IPs.
*   `zbx_k8s_ingress_tls_expiry.py` - Directly parses kubernetes.io/tls Secrets to calculate SSL certificate expiration days.
*   `zbx_k8s_job_failures.py` - Discovers Batch Jobs and alerts on silent task failures.
*   `zbx_k8s_kubelet_versions.py` - Audits node Kubelet versions to detect failed cluster upgrades or version drift.
*   `zbx_k8s_limit_ranges.py` - Checks if Namespaces enforce default CPU/Memory LimitRanges.
*   `zbx_k8s_namespace_governance.py` - Audits Namespaces for mandatory compliance annotations/labels (e.g., billing-team).
*   `zbx_k8s_node_conditions.py` - Monitors silent Node conditions like MemoryPressure, DiskPressure, and PIDPressure.
*   `zbx_k8s_node_cpu_alloc.sh` - Kubernetes node CPU allocation percentage.
*   `zbx_k8s_node_taints.py` - Tracks NoSchedule/NoExecute Taints applied to cluster nodes.
*   `zbx_k8s_oomkilled_pods.py` - Scans all pods to detect and list containers terminated due to OOMKilled errors.
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
*   `zbx_k8s_warning_events.py` - Aggregates and categorizes cluster-wide Warning events (e.g., FailedScheduling).

### 🗄️ `databases-and-storage/`
Deep monitoring for RDBMS, NoSQL, and storage fabrics.
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
*   `zbx_timescaledb_chunks.sh` - TimescaleDB chunks audit for Zabbix databases.
*   `zbx_vmware_datastore.py` - VMware vSphere Datastore capacity via pyVim.
*   `zfs_pool_health_lld.sh` - LLD for ZFS pool health and capacity.

### 🌐 `network-and-routing/`
Network infrastructure, routing protocols, and SD-WAN.
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
Low-level health checks for Linux and Windows servers.
*   `check_cpu_iowait.sh` - Linux CPU iowait bottleneck percentage.
*   `check_disk_inodes.sh` - Linux disk inode utilization percentage.
*   `check_ntp_sync.sh` - NTP time synchronization status.
*   `check_oom_killer.sh` - OOM Killer intervention counter.
*   `check_pending_reboot.ps1` - Windows pending reboot registry check.
*   `check_zombie_procs.sh` - Linux zombie processes count.
*   `iis_app_pools_lld.ps1` - Windows IIS Application Pools discovery.
*   `systemd_services_lld.sh` - Linux enabled systemd services discovery.
*   `ups_battery_charge.sh` - UPS battery charge percentage via apcupsd.
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
Auditing, edge security, and VPN connections.
*   `active_ssh_sessions.sh` - Active SSH user sessions count.
*   `check_open_ports.sh` - Validates if a specific local port is listening.
*   `failed_ssh_logins.sh` - Brute-force SSH failed logins counter.
*   `file_checksum_monitor.sh` - SHA256 critical file checksum monitor.
*   `openvpn_sessions_lld.py` - LLD for connected OpenVPN users and bandwidth.
*   `strongswan_ipsec_lld.sh` - LLD for StrongSwan IPsec tunnels.
*   `vpn_ipsec_tunnel.sh` - IPsec VPN tunnel up/down status via ICMP.
*   `zbx_paloalto_gp_users.py` - Palo Alto GlobalProtect active users count.

### 🕸️ `web-api-dns/`
Digital experience, synthetics, and web services.
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
Meta-monitoring for the Zabbix infrastructure itself.
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

---

## 🚀 Quick Start Guide

These scripts are designed to be deployed as either **Zabbix Agent UserParameters** (local OS metrics) or **External Checks** (API polling from the Zabbix Server/Proxy).

### 1. Prerequisites
Ensure your Zabbix Server/Proxy or Agent has the necessary dependencies installed for the scripts you intend to use. Common dependencies include:
*   `jq` (for JSON parsing in Bash scripts)
*   `python3` and `pip` packages: `requests`, `boto3`, `pyVim`, `pycurl`
*   `aws-cli`, `gcloud`, or `az` CLI tools (for Cloud scripts)
*   `postgresql-client` or `mysql-client` (for Database scripts)

### 2. Deployment: UserParameters (Zabbix Agent)
Use this method for scripts that extract local OS, Container, or Database data.

1.  Copy the desired script to the monitored host (e.g., `/etc/zabbix/scripts/`).
2.  Make the script executable:

        chmod +x /etc/zabbix/scripts/script_name.sh

3.  Add the UserParameter to your `zabbix_agentd.conf` (or a file in `/etc/zabbix/zabbix_agentd.d/`):

        UserParameter=custom.metric.name[*], /etc/zabbix/scripts/script_name.sh $1 $2

4.  Restart the Zabbix Agent:

        systemctl restart zabbix-agent2

5.  In the Zabbix Frontend, create an item of type **Zabbix agent** with the key `custom.metric.name[arg1,arg2]`.

### 3. Deployment: External Checks (Zabbix Server / Proxy)
Use this method for scripts that query REST APIs, cloud providers, or remote network equipment (e.g., Meraki, AWS, M365).

1.  Copy the script to the `ExternalScripts` path defined in your `zabbix_server.conf` or `zabbix_proxy.conf` (usually `/usr/lib/zabbix/externalscripts/`).
2.  Make the script executable:

        chmod +x /usr/lib/zabbix/externalscripts/script_name.py

3.  Test the script execution manually using the `zabbix` OS user to ensure network connectivity and proper permissions before adding it to the UI.

### 4. Deployment: Zabbix Sender (Asynchronous Pushing)
Use this method for scripts that take longer to run (like the MTR network path trace) to prevent Zabbix poller timeouts.

1.  Ensure the `zabbix_sender` utility is installed on the host running the script.
2.  Place the script in a designated folder and schedule it via `cron`:

        */5 * * * * zabbix /path/to/script.sh

3.  Ensure the host is allowed to send data to the Zabbix Server/Proxy over TCP port `10051` (Trapper port).

### 5. Zabbix Frontend Configuration (Master Items & LLD)
Since this toolkit relies on Bulk Data Collection (returning one large JSON payload instead of multiple small queries), you must configure the frontend to parse the data properly.

#### 5.1. Create the Master Item
*   Navigate to **Data collection** > **Hosts** and click on your target host.
*   Go to **Items** and click **Create item**.
*   Set **Type** to `External check` (or `Zabbix agent`, depending on the script).
*   In the **Key** field, reference the script and its macros: `script_name.py["{$API_USER}","{$API_PASS}"]`.
*   **CRITICAL:** Set the **Type of information** to `Text`. This ensures Zabbix can ingest the entire JSON payload without cutting off characters.
*   Set the **Update interval** (e.g., `5m`).

#### 5.2. Create the Discovery Rule
*   Navigate to **Discovery rules** on the same host and click **Create discovery rule**.
*   Give it a name and set the **Type** to `Dependent item`.
*   In the **Master item** dropdown, select the item you created in Step 5.1.

#### 5.3. Configure LLD Macros
*   Inside your Discovery Rule, switch to the **LLD macros** tab.
*   Map the JSON keys to Zabbix macros. This teaches Zabbix how to read your payload. For example:
    *   `{#DOMAIN}` ➔ `$.domain`
    *   `{#STATUS}` ➔ `$.status`

#### 5.4. Create Item Prototypes
*   Inside the Discovery Rule, click on **Item prototypes** > **Create item prototype**.
*   Set the **Type** to `Dependent item` and point it to the Master Item again.
*   Use your LLD macros dynamically in the Name and Key (e.g., Name: `SSL Status of {#DOMAIN}`, Key: `ssl.status[{#DOMAIN}]`).
*   Set the **Type of information** to `Numeric (unsigned)` or `Float`.

#### 5.5. Apply JSONPath Preprocessing
*   Go to the **Preprocessing** tab of the Item Prototype.
*   Add a `JSONPath` step to extract the exact value needed for this specific prototype.
*   Example parameter: `$.data[?(@.domain == "{#DOMAIN}")].status.first()`

### 💡 Security Best Practices
*   **Never hardcode passwords:** Always pass API tokens and credentials as arguments using Zabbix **Secret Macros** (`{$SECRET_PASSWORD}`). This masks the values in the frontend.
*   **Sudo privileges:** If a script requires root access (e.g., `smartctl`, `lsblk`), configure `visudo` specifically for the `zabbix` user instead of running the entire agent as root:

        zabbix ALL=(ALL) NOPASSWD: /usr/sbin/smartctl

*   **API Rate Limiting:** When polling cloud providers (AWS, Azure) or SaaS platforms, adjust your update intervals carefully (e.g., `5m` or `10m`) to avoid API throttling and unexpected billing charges.
*   **Secure Vaults:** For highly compliant environments, integrate HashiCorp Vault or CyberArk with Zabbix 6.0+ to retrieve API tokens dynamically instead of storing them in Zabbix databases.