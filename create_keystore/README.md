# Role Name

Use this Role to create a new keystore on the ISAM Appliance.

## Requirements

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

## Role Variables

The following variables are required:
* create_keystore_name

While the following variables are optional (with default values):
* create_keystore_type: 'kdb' or 'p11'

In case of 'p11', all the following values are required:
* create_keystore_token_label: null
* create_keystore_passcode: null
* create_keystore_hsm_type: null or 'ncipher' or 'safenet'
* create_keystore_ip: null

The following values are only valid in case of hsm_type 'ncipher':
* create_keystore_port: null
* create_keystore_kneti_hash: null
* create_keystore_esn: null

RFS details:
* create_keystore_use_rfs: False # Not used explicitly
* create_keystore_rfs: null # IP Address in case that use_rfs is True
* create_keystore_rfs_port: null
* create_keystore_rfs_auth: False

Only valid if use_rfs is False:
* create_keystore_update_zip: null
* create_keystore_safenet_pw: null

Not provided by Python API:
* create_keystore_secondary_ip: null
* create_keystore_secondary_port: null
* create_keystore_secondary_kneti_hash: null
* create_keystore_secondary_esn: null

## Dependencies

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

## Example Playbook

Here is an example of how to use this role:

    - name: Create sample keystore
      hosts: primary_master
      connection: local
      roles:
        - start_config
        - role: create_keystore
          create_keystore_name: 'sample_db'

## License

Apache

## Author Information

Dries Eestermans (dries.eestermans@is4u.be)