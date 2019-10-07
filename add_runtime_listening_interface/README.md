Role Name
=========

Use this Role to Add One or More Runtime Listening Interfaces on the ISAM Appliance.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide the interface, port, and secure flag for each runtime listening interface to add
```
  runtime_listening_interfaces:
    - runtime_listening_interface_interface: local-interface
      runtime_listening_interface_port: 80
      runtime_listening_interface_secure: false
    - runtime_listening_interface_interface: local-interface
      runtime_listening_interface_port: 443
      runtime_listening_interface_secure: true
```

The role automatically takes a snapshot before adding runtime listening interfaces, override as needed:
`add_runtime_listening_interface_comment: "Automated Snapshot Before Adding Runtime Listening Interfaces"`

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: add_runtime_listening_interface
           runtime_listening_interfaces:
             - runtime_listening_interface_interface: local-interface
               runtime_listening_interface_port: 80
               runtime_listening_interface_secure: false
             - runtime_listening_interface_interface: local-interface
               runtime_listening_interface_port: 443
               runtime_listening_interface_secure: true

License
-------

Apache

Author Information
------------------

Ryan Dunn (rdunn1121@gmail.com)
