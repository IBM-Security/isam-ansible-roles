Role Name
=========

Use this Role to Upload One or More LTPA key files to the ISAM Appliance.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide the option key and value for the runtime tuning parameters to set
```
  ltpa_keys:
    - ltpa_key_id: "LTPA Key 1"
      ltpa_key_keyfile: "ltpa-keyfile-1"
    - ltpa_key_id: "LTPA Key 2"
      ltpa_key_keyfile: "ltpa-keyfile-2"
```

The role automatically takes a snapshot before uploading the LTPA keys, override as needed:
`upload_ltpa_key_comment: "Automated Snapshot Before Uploading LTPA Keys"`

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: upload_ltpa_key
           ltpa_keys:
             - ltpa_key_id: "LTPA Key 1"
               ltpa_key_keyfile: "ltpa-keyfile-1"
             - ltpa_key_id: "LTPA Key 2"
               ltpa_key_keyfile: "ltpa-keyfile-2"

License
-------

Apache

Author Information
------------------

Ryan Dunn (rdunn1121@gmail.com)
