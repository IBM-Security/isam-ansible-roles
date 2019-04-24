Bonding interface
=========

this role supplies tasks for creating the master bonding interface and the slave(s)

Requirements
------------


Role Variables
--------------

This depends on bondingMode being set to slave or one of the other modes.
If bondingMode is set to slave; bondedTo is also required.

interfaces:
  - label      :  '1.3'
    name: "Bonding Master"
    bondingMode: '802.3ad'
    comment    : 'Added by TB'
  - label        :  '1.4'
    name: "Bonding Slave"
    bondingMode: 'slave'
    bondedTo: '1.3'
    comment: "I am the slave"

Dependencies
------------

IBM ISAM Security

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

- hosts: "all"
  connection: local
  gather_facts: no
  tasks:
    - name: Add network bonding for configured interface
      tags: ["bonding"]
      include_role:
       name: base/bonding_interfaces

License
-------

BSD

Author Information
------------------

tom.bosmans@be.ibm.com

