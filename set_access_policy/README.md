Set Access Policy
=========

A role for creating or updating an access policy

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide the following values for role to succeed

```
  required
  set_access_policy_name:

  set_access_policy_file:
  OR
  set_access_policy_content:

  optional
  set_access_policy_category: (Default: OIDC)
  set_access_policy_type: (Default: JavaScript)
```

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

With this playbook you can create or update an access policy

```
    - hosts: servers
      connection: local
      roles:
        - role: start_config
        - role: set_access_policy
          set_access_policy_name: "Policy1"
          set_access_policy_file: "/path/to/access_policy.js"
```

License
-------

Apache
