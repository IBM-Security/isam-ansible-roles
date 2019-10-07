Role Name
=========

Use this Role to Set One or More Advanced Tuning Parameters on the ISAM Appliance.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide the option key and value for the advanced tuning parameters to set
```
  advanced_tuning_parameters:
    - advanced_tuning_parameter_key: "Key 1"
      advanced_tuning_parameter_value: "Value 1"
    - advanced_tuning_parameter_key: "Key 2"
      advanced_tuning_parameter_value: "Value 2"
      advanced_tuning_parameter_comment: "Optional comment"
```

The role automatically takes a snapshot before setting advanced tuning parameters, override as needed:
`set_advanced_tuning_parameter_comment: "Automated Snapshot Before Setting Advanced Tuning Parameters"`

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: set_advanced_tuning_parameter
           advanced_tuning_parameters:
             - advanced_tuning_parameter_key: "Key 1"
               advanced_tuning_parameter_value: "Value 1"
             - advanced_tuning_parameter_key: "Key 2"
               advanced_tuning_parameter_value: "Value 2"
               advanced_tuning_parameter_comment: "Optional comment"

License
-------

Apache

Author Information
------------------

Ryan Dunn (rdunn1121@gmail.com)
