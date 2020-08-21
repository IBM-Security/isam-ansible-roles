# IBM Sample Code

This repository contains Ansible Custom Modules and Roles for automating ISAM Appliance tasks. Custom Modules provide the
interface to python idempotent functions in ibmsecurity package. Handlers are coded into the roles to ensure changes are
committed (deployed) and relevant processes restarted.

## Requirements

Python v2.7.10 or v3.7.0 and above is required for this package.

The following Python Packages are required (including their dependencies):
1. ibmsecurity
2. ansible

Appliances need to have an ip address defined for their LMI. This may mean that appliances have had their initial setup
done with license acceptance.

## Get Started
Use ansible-galaxy to install the roles like so:
`ansible-galaxy install git+https://github.com/ibm-security/isam-ansible-roles.git --roles-path <dest dir>`

Using the `--roles-path` option allows installation to a desired location. This avoids the need to write to system
directory.

Use the following setting in ansible.cfg to set the location of the installed roles:
```
[defaults]
roles_path = <dest dir>
```

## Versioning

git tag will be used to indicate version numbers. The version numbers will be based on date. For example: "2017.03.20.0"

It is the date when the package is released with a sequence number at the end to handle when there are
multiple releases in one day (expected to be uncommon).

## Features

The `start_config` role is a requirement for every playbok. It contains the custom modules and all handlers. All other
roles have a dependency on it and `start_config` will get automatically invoked as needed.This repository contains a small selection of roles - users are encouraged to add more as needed.

### Custom Modules
_”Modules (also referred to as “task plugins” or “library plugins”) are the ones that do the actual work in ansible,
they are what gets executed in each playbook task. But you can also run a single one using the ‘ansible’ command.”_
http://docs.ansible.com/ansible/modules_intro.html

Ansible custom modules provide the glue to seamless invoke python functions to execute REST API calls against ISAM
appliances. There are three custom modules. Each allows a different set of parameters to be passed.

isam - this module is for all calls to ISAM appliances except PDAdmin calls.

isamadmin - this module is for making PDAdmin calls. Check mode execution is not supported.

isamcompare - this module allows one to compare a feature of one appliance with another. This is read only call where
the JSON data from one appliance is comapared against another.

### Handlers
After a change happens, ansible can be set to execute "handlers" to commit changes and/or restart processes. Handlers
are just other tasks. Handlers execute based on the sequence in which they are listed. See `start_config` role for
details.

### Roles
“Roles in Ansible build on the idea of include files and combine them to form clean, reusable abstractions – they allow
you to focus more on the big picture and only dive down into the details when needed.”
http://docs.ansible.com/ansible/playbooks_roles.html

Using roles allows one to concentrate on describing the business needs in a playbook. The actual call to the python
function and the need to deploy and restart processes is taken care of isnide the role.

## Naming of Roles and variables
Roles start with a verb like "set" or "add" followed by a name that describes either the task or the python function
being called. This depends on whether the role contains a single tasks or a combination of tasks.

Preference should be given to using "set" roles versus ones that do an "add" or "update". This allows for the role to
either do an add or an update as the situation demands.

# License

The contents of this repository are open-source under the Apache 2.0 licence.

```
Copyright 2017 International Business Machines

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

Ansible is a trademark of Red Hat, Inc.
