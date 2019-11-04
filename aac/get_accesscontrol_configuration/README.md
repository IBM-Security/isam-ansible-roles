# Get the full access control configuration

Will download into a separate directory, a full dump of the AAC advanced access control configuration in yaml files.
These files can be used to configure the actual Ansible configuraiton.

The role creates a randomly named directory to store all files in; in the access_control_output_dir you define .
See defaults/main.yml for the default configuration.

It exports
- the Access control policies, in the xml format required to upload them.
- the Access control resources and attachments, in yaml format, ready to re-use in plays.

## Example playbook

- hosts: "all"
  connection: local
  gather_facts: yes
  tasks:
    - name: Export aac access control configuration in yaml files
      tags: ["infomap"]
      import_role:
        name: aac/get_accesscontrol_configuration
      vars:
        access_control_output_dir: "{{ inventory_dir }}"

### Prerequisites

start_config

```
access_control_output_dir: variable to set to the directory you want the output to be
```

## Versioning
1.0.0

## Authors

* **Tom Bosmans** - *Initial work* - [tombosmansibm](https://github.com/tombosmansibm/isam-ansible-roles)

## Acknowledgments

* Ram Sreerangam, for driving the ISAM Ansible automation

