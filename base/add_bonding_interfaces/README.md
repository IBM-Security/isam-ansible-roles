Bonding interface
=========

this role is a test to first lookup the uuid of the interface in a role.

This role does not require changes to the python code; as did an earlier version.

TODO: Does not currently include vlanId (not sure if that is even relevant for bonding interfaces)

Requirements
------------

The other roles that also use the "interfaces" object , need to be modified that they use specific items instead of 
 isamapi: "{{ {} | combine(item.0) | combine(item.1) }}", instead it needs to be like this:
 
 isamapi:
      label: "{{ item.0.label }}"
      address: "{{ item.1.address }}"
      maskOrPrefix: "{{ item.1.maskOrPrefix }}"
      allowManagement: "{{ item.1.allowManagement }}"
      enabled: "{{ item.1.enabled | default(False) }}"

Role Variables
--------------

This role configures interfaces for Bonding (slave and master)>
This depends on bondingMode being set to slave or one of the other modes.
If bondingMode is set to slave; bondedTo is also required.

interfaces:
  - label      :  '1.3'
    name: "Bonding Master"
    bondingMode: '802.3ad'
    comment    : 'Your comment is my command'
  - label        :  '1.4'
    name: "Bonding Slave"
    bondingMode: 'slave'
    bondedTo: '1.3'
    comment: "I am the slave"

The notation of interfaces can be combined with the other roles (add_interfaces)

Dependencies
------------

IBM ISAM Security

Example Playbook
----------------

- hosts: "all"
  connection: local
  gather_facts: no
  tasks:
    - name: Add network bonding for configured interface
      tags: ["bonding"]
      vars:
        interfaces:
        - label: '1.3'
          name: "Bonding Master"
          bondingMode: '802.3ad'
          comment: 'MASTER'
          addresses:
          - address:            "192.168.42.100"
            maskOrPrefix:       "255.255.255.0"
            allowManagement:    false
            enabled:            true
        - label: '1.4'
          name: "Bonding Slave"
          bondingMode: 'slave'
          bondedTo: '1.3'
          comment: "SLAVE NR. 1"
      include_role:
       name: base/add_bonding_interfaces

License
-------

BSD

Author Information
------------------

tom.bosmans@be.ibm.com

