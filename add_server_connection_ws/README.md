Role Name
=========

Use this Role to Add a Web Service Server Connection to the ISAM Appliance.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide the name, connection, description, locked flag, and the connection manager for the new LDAP server connection
```
  ws_server_connection_name: "LDAP Connection"
  ws_server_connection_connection: {"url": "https://someserver:443/someWebServiceURI", "user": "aUser", "password": "secret", "ssl": true, "sslTruststore": "trust.kdb", "sslAuthKey": "client_key"}
  ws_server_connection_description: "This is a connection to an LDAP server"
  ws_server_connection_locked: false
  ws_server_connection_connection_manager: {"connectTimeout": 300}
```

The role automatically takes a snapshot before adding the LDAP server connection, override as needed:
`add_server_connection_ws_comment: "Automated Snapshot Before Adding LDAP Server Connection"`

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: add_server_connection_ws
           ws_server_connection_name: "LDAP Connection"
           ws_server_connection_connection: {"url": "https://someserver:443/someWebServiceURI", "user": "aUser", "password": "secret", "ssl": true, "sslTruststore": "trust.kdb", "sslAuthKey": "client_key"}
           ws_server_connection_description: "This is a connection to a Web Service"
           ws_server_connection_locked: false
           ws_server_connection_connection_manager: {"connectTimeout": 300}


License
-------

Apache

Author Information
------------------

IFC, based on Ryan Dunn's original implementation of LDAP Server connection
