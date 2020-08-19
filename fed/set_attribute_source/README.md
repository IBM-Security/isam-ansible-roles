Role Name
=========

Use this Role to Set One or More Attribute Sources to the ISAM Appliance.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide the name, type, and value for the attribute sources. Also provide properties if the type is ldap
```
  attribute_sources:
    - attribute_source_name: "Attribute Source 1"
      attribute_source_type: "ldap"
      attribute_source_value: "Value 1"
      attribute_source_properties:
        - {"key": "serverConnection", "value": "Server Connection"}
        - {"key": "scope", "value": "subtree"}
        - {"key": "selector", "value": "attr"}
        - {"key": "searchFilter", "value": "attr=*"}
        - {"key": "baseDN", "value": "secAuthority=Default"}
    - attribute_source_name: "Attribute Source 2"
      attribute_source_type: "value"
      attribute_source_value: "Value 2"
```

The role takes a snapshot before adding attribute sources, override as needed, if
add_attribute_source_snapshot: True
(default False)
`add_attribute_source_comment: "Automated Snapshot Before Adding Attribute Sources"`

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: add_attribute_source
           attribute_sources:
             - attribute_source_name: "Attribute Source 1"
               attribute_source_type: "ldap"
               attribute_source_value: "Value 1"
               attribute_source_properties:
                 - {"key": "serverConnection", "value": "Server Connection"}
                 - {"key": "scope", "value": "subtree"}
                 - {"key": "selector", "value": "attr"}
                 - {"key": "searchFilter", "value": "attr=*"}
                 - {"key": "baseDN", "value": "secAuthority=Default"}
             - attribute_source_name: "Attribute Source 2"
               attribute_source_type: "value"
               attribute_source_value: "Value 2"

License
-------

Apache

Author Information
------------------
Based on work by : Ryan Dunn (rdunn1121@gmail.com)
Tom Bosmans: tom.bosmans@be.ibm.com