Role Name
=========

Use this Role to Add One or More Custom Management Authorization Roles to the ISAM Appliance.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide the name of the new management authorization roles
```
  mgmtazn_role_names:
    - Role 1
    - Role 2
```

The role automatically takes a snapshot before adding roles, override as needed:
`add_mgmtazn_role_comment: "Automated Snapshot Before Adding Management Authorization Roles"`

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: add_mgmtazn_role
           mgmtazn_role_name:
             - Role 1
             - Role 2

License
-------

Apache

Author Information
------------------

Ryan Dunn (rdunn1121@gmail.com)
