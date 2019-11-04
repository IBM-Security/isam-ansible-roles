Role Name
=========

Use this Role to add SAML or OIDC Federations to the ISAM Appliance.

Requirements
------------

Please activate "`federation`" module before using this role.

`start_config` role is a required dependencies. It contains the Ansible Custom Modules and handlers.

`upload_mapping_rule` - maybe required to load a mapping rule before creating the federation.

`search_mapping_rule` - maybe required to lookup a mapping rule to pass in the variable `identityMappingRuleReference`.


Role Variables
--------------

Provide valid values for the following variables, see example for details:
~~~~
add_federation_name:
add_federation_protocol:
add_federation_role:
add_federation_configuration:
add_federation_templateName:
~~~~

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:

    - role: upload_mapping_rule
      tags: ["mapping", "rule", "upload"]
      upload_mapping_rule_category       : "OIDC"
      upload_mapping_rule_name           : "OIDCIBMOP"
      upload_mapping_rule_upload_filename: "/home/python/rules/OIDCIBMOP.js"

    - role: search_mapping_rule
      tags: ["mapping", "rule", "search"]
      search_mapping_rule_name           : "OIDCIBMOP"

    - role: set_federation
      tags: ["federation", "add"]
      set_federation_name:         "IBMOP"
      set_federation_protocol:     "OIDC"
      set_federation_role:         "op"
      set_federation_templateName: ""
      set_federation_configuration:
        accessTokenLength: 40
        accessTokenLifetime: 7200
        attributeMapping:
          map: []
        authorizationCodeLength: 30
        authorizationCodeLifetime: 30
        authorizationGrantLifetime: 604800
        grantTypesSupported: ["authorization_code", "implicit"]
        idTokenLifetime: 7200
        identityMapping:
          activeDelegateId: "default-map"
          properties:
            identityMappingRuleReference: "{{ search_mapping_rule['data'] }}"
            ruleType: "JAVASCRIPT"
        issuerIdentifier: "https://ibm.com"
        refreshTokenLength: 50
        signatureAlgorithm: "HS256"

License
-------

Apache

Author Information
------------------

IBM
