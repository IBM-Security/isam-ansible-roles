# Role Name

Use this Role to set a description for a keystore on the ISAM Appliance.

## Requirements

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

## Role Variables

The following values are required:
* set_keystore_desc_keystore
* set_keystore_desc_description

## Dependencies

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

## Example Playbook

Here is an example on how to use this role:

    - name: Set description for sample keystore
      hosts: primary_master
      connection: local
      roles:
        - start_config
        - role: set_keystore_desc
          set_keystore_desc_keystore: 'keystore id'
          set_keystore_desc_description: 'Description of Sample keystore'

## License

Apache

## Author Information

Dries Eestermans (dries.eestermans@is4u.be)
