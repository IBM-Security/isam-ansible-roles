# Configure Access Control Policy

This role create Advanced access control policies, based on a policy xml file.
This xml file cannot contain whitespaces, it must have all xml on 1 single line.

To create such a file, it's best to use the aac/get_acccesscontrol_configuration, that will generate (among others)
the policy files of a configured system.

## Example playbook

- hosts: "all"
  connection: local
  gather_facts: yes
  tasks:
    - name: Create AAC Access Control policies
      tags: ["aac","access-control-policy","resources"]
      import_role:
       name: aac/set_accesscontrol_policies
      vars:
       accesscontrol_policies: 
        -  attributesrequired: false
           description: 'TOTP Policy'
           dialect: urn:oasis:names:tc:xacml:2.0:policy:schema:os
           name: totp_policy
           predefined: false
           policy_file: "files/mga/access_control_policies/TOTP.xml"

### Prerequisites

start_config

```
The policy file (policy_file) needs to exist , in the correct xacml format . 

```

## Versioning
1.0.0

## Authors

* **Tom Bosmans** - *Initial work* - [tombosmansibm](https://github.com/tombosmansibm/isam-ansible-roles)

## Acknowledgments

* Ram Sreerangam, for driving the ISAM Ansible automation

