Role Name
=========

Use this Role to configure cluster for an ISAM Appliance.

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
         - role: set_cluster_config
           set_cluster_config_primary_master: '192.168.198.100'

License
-------

Apache

Author Information
------------------

IBM
