
set_ldap_user_attr
=========

Set LDAP user attribute

Requirements
------------

python-ldap module is installed on the build system.

Role Variables
--------------

The variables for this role can be passed via role directly, or inventory file, or playbook vars/main.yml.

Required variables are:

**ldap_bind_dn**: Binding DN, for example "cn=root,secAuthority=default"

**ldap_bind_pw**: Binding password

**ldap_server_uri**: LDAP server URI, for example, "ldaps://192.168.42.101:636/"

**ldap_state**: LDAP attribute target state, valid options are:
```
  present: all given values will be added if they are missing
  absent: all given values will be removed if present.
  exact: the set of values will be forced to exactly those provided and no others.
```

**ldap_user_attributes**: This is a JSON object which contains 'dn' string and a JSON array 'attributes'. For example:
```
    - dn: "uid=testuser,dc=iswga"
      attributes:
      - { "name": "mail", "values": "testuser@mailinator.com" }
      - { "name": "displayName", "values": "Test User" }
```


Dependencies
------------

This role depends on the Ansible module ldap-attr which will be part of Ansible 2.3, not official released yet. We have included it under the /library directory. Once it is officially released by Ansible we will remove it from this role.

https://docs.ansible.com/ansible/ldap_attr_module.html

Example Playbook
----------------

A sample playbook *test.yml* has been placed under *tests/* subdirectory.

```
---
- name: modify LDAP user attributes
  hosts: localhost
  connection: local
  roles:
      - role: set_ldap_user_attr
        ldap_bind_dn: "cn=root,secAuthority=default"
        ldap_bind_pw: "passw0rd"
        ldap_server_uri: "ldaps://192.168.42.101:636/"
        ldap_state: "exact"
        ldap_user_attributes:
            - dn: "uid=testuser,dc=iswga"
              attributes:
                - { "name": "mail", "values": "testuser@mailinator.com" }
                - { "name": "displayName", "values": "Test User" }
```

You may run it with ansible-playbook directly:

```
ansible-playbook -i inventory test.yml
```

License
-------

Apache


Author Information
------------------

IBM
