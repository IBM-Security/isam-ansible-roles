This role is an enhancement of the role externalize_hvdb_db2, but supports both DB2 and Oracle.

**Example variables:**
vars.yml
externalize_hvdb_hvdb_address: oracle.server.com
externalize_hvdb_hvdb_db_name: oraservicename
externalize_hvdb_hvdb_user: "hvdb"
externalize_hvdb_hvdb_password: "{{ vault_oracle_hvdb_pwd }}"
externalize_hvdb_cfgdb_embedded:  True
externalize_hvdb_dsc_client_grace_period:      600
externalize_hvdb_dsc_external_clients: False
externalize_hvdb_dsc_maximum_session_lifetime: 3600
externalize_hvdb_dsc_worker_threads: 64
externalize_hvdb_first_port      : 2020
externalize_hvdb_hvdb_db_secure  : False
externalize_hvdb_hvdb_db_type    : "oracle"
externalize_hvdb_hvdb_driver_type: "thin"
externalize_hvdb_hvdb_embedded   :  False
externalize_hvdb_primary_master  :  "127.0.0.1"
externalize_hvdb_hvdb_port: "1521"
externalize_hvdb_oracle_connection_string: 'jdbc:oracle:thin:@//oracle.server.com:1521/oraservicename'

**Example playbook:**
`
- hosts: "all"
  connection: local
  gather_facts: no
  tasks:
    - name: Configure external runtime database for oracle
      tags: ["oracle"]
      include_role:
        name: base/externalize_hvdb
      when: externalize_hvdb_hvdb_address is defined
 `

**Enabling tracing**
The LMI Trace does not work (up to ISAM 9.0.6), but these parameters set the corresponding settings per technote

debug_oracle_enable_lmi_trace: false
debug_oracle_enable_runtime_trace: false