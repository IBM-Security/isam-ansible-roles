
start_config
=========

This role contains the ISAM Ansible module files under the *library* subdirectory, and notification handlers that can be used by all other roles. Always reference this role before other ISAM Ansible roles.

This role also takes care of the first steps set up of an ISAM appliance, set up FIPS configuration for LMI, and change the default password. It is to be run once only.

Requirements
------------

An ISAM appliance needs to be bootstrapped with LMI interface up and running.

Role Variables
--------------

The variables for this role can be passed via role directly, or inventory file, or playbook vars/main.yml.

All required variables are defined in *defaults/main.yml* file except for the *inventory_hostname*.

Required variables must be provided:

**inventory_hostname**: hostname or IP address of the LMI interface
**password**: LMI admin password to be set

Variables with default values set, define them only if you want to change the default values:

**lmi_port**: TCP port for LMI interface, default is 443
**username**: LMI admin user name, default is admin
**log_level**: one of DEBUG, INFO, ERROR, FATAL, default is INFO
**force**: true or false, default is false
**FIPS_cfg**: FIPS configuration in JSON object, default is {fipsEnabled:true/false, tlsv10Enabled:false, tlsv11Enabled:true}
**lmi_session_timeout**: LMI session timeout, default is 720 seconds
**start_config_wait_time**: Wait time for ISAM appliance to restart, default is 600 seconds.

Dependencies
------------

None


Example Playbook
----------------

A sample playbook *test.yml* has been placed under *tests/* subdirectory.

    - hosts: servers
      roles:
         - { role: start_config, inventory_hostname: 192.168.42.111, password: Passw0rd  }

After verifying the other variables set in *host_vars/localhost.yml*,  you may run it with ansible-playbook directly:

```
ansible-playbook -i inventory test.yml
```

License
-------

Apache


Author Information
------------------

IBM
