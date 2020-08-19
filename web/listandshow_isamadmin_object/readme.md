listandshow_isamadmin_object
=========

This role runs list-and-show on a list of objects.


Requirements
------------
An ISAM appliance needs to be bootstrapped with LMI interface up and running.


Role Variables
--------------
admin_domain: Default
isam_objects:
  - "/"
admin_id: sec_master
admin_pwd: passw0rd

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| admin_id                | no      | sec_master   | name of your admin id              | sec_master default                         |
| admin_pwd               | yes      |         | none               | password for sec_master       |
| admin_domain            | no      | Default        | none               | Domain.  Mostly will be Default       |
| isam_objects            | no      | /        | list of the objects you want to listandshow               |        |

Dependencies
------------

start_config

Example Playbook
----------------

---
- hosts: "all"
  connection: local
  gather_facts: no
  tasks:
    - name: List and show objects
      tags: ["objects"]
      include_role:
        name: web/listandshow_isamadmin_object
      vars:
         isam_objects:
           - /
           - /WebSEAL
           - /WebSEAL/isam.domain.tld-default
 

License
-------

Apache

Author Information
------------------

IBM