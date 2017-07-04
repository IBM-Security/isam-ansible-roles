# Role Name
=========

Use this Role to create a new keystore on the ISAM Appliance.

## Requirements
----------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

## Role Variables
----------------

## Dependencies
----------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

## Example Playbook
----------------

Here is an example of how to use this role:

    - name: Create sample keystore
      hosts: primary_master
      connection: local
      roles:
        - start_config
        - role: create_keystore
          create_keystore_name: 'sample_db'

## License
----------------

Apache

## Author Information
----------------

Dries Eestermans (dries.eestermans@is4u.be)