Role Name
=========

Use this Role to configure DSC for an ISAM Docker.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

All variables to this role are optional. They will take default values if not specified.

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: set_dsc_config
           set_dsc_config_worker_threads: 64
           set_dsc_config_max_session_lifetime: 3600
           set_dsc_config_client_grace: 600
           set_dsc_config_service_port: 443
           set_dsc_config_replication_port: 444
           set_dsc_config_servers:
             - ip: "isamdsc"
               service_port: 443
               replication_port: 444


License
-------

Apache

Author Information
------------------

IBM
