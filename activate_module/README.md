Role Name
=========

Use this Role to Activate Modules with the ISAM Appliance.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide valid module identifiers - they can be one of wga, mga or federation
`activate_module_id: 'wga'`

Provide the activation code for corresponding version of ISAM. The activation code can be read from the activation files downloaded from
IBM Passport Advantage.
`activate_module_code: 'xxxx-xxxx-xxxx...'`

The role automatically takes a snapshot before activating a module, override as needed:
`activate_module_comment: "Automated Snapshot Before Activating {{ activate_module_id }}"`

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: activate_module
           activate_module_id: 'wga'
           activate_module_code: 'xxxx-xxxx-xxxx-xxxx'

License
-------

Apache

Author Information
------------------

IBM
