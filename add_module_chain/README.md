Role Name
=========

Use this Role to Add A Module Chain to the ISAM Appliance.

Requirements
------------

start_config role is a required dependencies. It contains the Ansible Custom Modules and handlers.

Role Variables
--------------

Provide the name, chain template name, request type, description (optional), token type (optional), xPath (optional), sign responses flag (optional), signature key (optional), validate request flag (optional), validation key (optional), send validation confirmation flag (optional), issuer (optional), applies to (optional), and properties (optional) for the new module chain
```
  module_chain_name: Chain 1
  module_chain_template_name: Template 1
  module_chain_request_type: http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue
  module_chain_description: Description for Chain 1
  module_chain_token_type: *
  module_chain_sign_responses: true
  module_chain_signature_key: signing-key
  module_chain_validate_requests: true
  module_chain_validation_key: validation-key
  module_chain_send_validation_confirmation: false
  module_chain_issuer: http://some.issuer.com
  module_chain_applies_to: http://some.recipient.com
  module_chain_properties:
    self:
      - name: SelfPropertyName1
        value:
          - SelfPropertyValue1
    partner:
      - name: PartnerPropertyName1
        value:
          - PartnerPropertyValue1
```

The role automatically takes a snapshot before adding the module chain, override as needed:
`add_module_chain_comment: "Automated Snapshot Before Adding Module Chain"`

Dependencies
------------

start_config is a required role - since it contains the Ansible Custom Modules and Handlers.

Example Playbook
----------------

Here is an example of how to use this role:

    - hosts: servers
      connection: local
      roles:
         - role: add_module_chain
           module_chain_name: Chain 1
           module_chain_template_name: Template 1
           module_chain_request_type: http://docs.oasis-open.org/ws-sx/ws-trust/200512/Issue
           module_chain_description: Description for Chain 1
           module_chain_token_type: *
           module_chain_sign_responses: true
           module_chain_signature_key: signing-key
           module_chain_validate_request: true
           module_chain_validation_key: validation-key
           module_chain_send_validation_confirmation: false
           module_chain_issuer: http://some.issuer.com
           module_chain_applies_to: http://some.recipient.com
           module_chain_properties:
             self:
               - name: SelfPropertyName1
                 value:
                   - SelfPropertyValue1
             partner:
               - name: PartnerPropertyName1
                 value:
                   - PartnerPropertyValue1

License
-------

Apache

Author Information
------------------

Ryan Dunn (rdunn1121@gmail.com)
