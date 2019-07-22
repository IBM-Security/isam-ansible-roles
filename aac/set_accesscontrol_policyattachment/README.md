# Create policy attachments

This role links the policies to resources in ISAM (URI's).

You can use the role aac/get_accesscontrol_configuration to generate yaml -formatted output of existing policy
attachment configuration , to use here.

## Example playbook

- hosts: "all"
  connection: local
  gather_facts: yes
  tasks:
    - name       : Attach Access Control Policies to resources
      tags       : ["attachments","access-control-policy","resources"]
      import_role:
        name: aac/set_accesscontrol_policyattachment
      vars       :
        accesscontrol_policy_attachments:
          - cache: -1
            policies:
            -   name: totp_policy
                type: policy
            policyCombiningAlgorithm: denyOverrides
            resourceUri: /wps/myportal
            server: "{{ appliance_name }}-{{ 'wrp1' }}"
            type: reverse_proxy
          - cache: -1
            policies:
            -   name: totp_policy
                type: policy
            policyCombiningAlgorithm: denyOverrides
            resourceUri: /demo/mobile-demo/diag
            server: "{{ appliance_name }}-{{ 'wrp1' }}"
            type: reverse_proxy


### Prerequisites

start_config

```

```

## Versioning
1.0.0

## Authors

* **Tom Bosmans** - *Initial work* - [tombosmansibm](https://github.com/tombosmansibm/isam-ansible-roles)

## Acknowledgments

* Ram Sreerangam, for driving the ISAM Ansible automation

