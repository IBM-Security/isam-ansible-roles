Role Name
=========

Use this Role to Add an LDAP Server Connection to the ISAM Appliance.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide the name, connection, description, locked flag, and the connection manager for the new LDAP server connection
```
  ldap_server_connection_name: "LDAP Connection"
  ldap_server_connection_connection: {"hostName": "ldap.int", "hostPort": "636", "bindDN": "cn=root", "bindPwd": "secret", "ssl": true, "sslTruststore": "trust.kdb", "sslAuthKey": "client_key"}
  ldap_server_connection_description: "This is a connection to an LDAP server"
  ldap_server_connection_locked: false
  ldap_server_connection_manager: {"connectTimeout": 300}
```

The role automatically takes a snapshot before adding the LDAP server connection, override as needed:
`add_server_connection_ldap_comment: "Automated Snapshot Before Adding LDAP Server Connection"`

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: add_server_connection_ldap
           ldap_server_connection_name: "LDAP Connection"
           ldap_server_connection_connection: {"hostName": "ldap.int", "hostPort": "636", "bindDN": "cn=root", "bindPwd": "secret", "ssl": true, "sslTruststore": "trust.kdb", "sslAuthKey": "client_key"}
           ldap_server_connection_description: "This is a connection to an LDAP server"
           ldap_server_connection_locked: false
           ldap_server_connection_manager: {"connectTimeout": 300}


License
-------

Apache

Author Information
------------------

Ryan Dunn (rdunn1121@gmail.com)
