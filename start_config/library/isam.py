#!/usr/bin/python

import logging
import logging.config
import sys
import importlib
from ansible.module_utils.basic import AnsibleModule
from io import StringIO
import datetime

from ibmsecurity.appliance.isamappliance import ISAMAppliance
from ibmsecurity.appliance.isamappliance_adminproxy import ISAMApplianceAdminProxy
from ibmsecurity.appliance.ibmappliance import IBMError
from ibmsecurity.user.applianceuser import ApplianceUser

logger = logging.getLogger(sys.argv[0])
try:
    basestring
except NameError:
    basestring = (str, bytes)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            log=dict(required=False, default='INFO', choices=['DEBUG', 'INFO', 'ERROR', 'CRITICAL']),
            appliance=dict(required=True),
            lmi_port=dict(required=False, default=443, type='int'),
            action=dict(required=True),
            force=dict(required=False, default=False, type='bool'),
            username=dict(required=False),
            password=dict(required=True, no_log=True),
            isamapi=dict(required=False, type='dict'),
            adminProxyProtocol=dict(required=False, default='https', choices=['http','https']),
            adminProxyHostname=dict(required=False),
            adminProxyPort=dict(required=False, default=443, type='int'),
            adminProxyApplianceShortName=dict(required=False, default=False, type='bool'),
            omitAdminProxy=dict(required=False, default=False, type='bool')
        ),
        supports_check_mode=True
    )

    module.debug('Started isam module')

    # Process all Arguments
    logLevel = module.params['log']
    force = module.params['force']
    action = module.params['action']
    appliance = module.params['appliance']
    lmi_port = module.params['lmi_port']
    username = module.params['username']
    password = module.params['password']
    adminProxyProtocol = module.params['adminProxyProtocol']
    adminProxyHostname = module.params['adminProxyHostname']
    adminProxyPort = module.params['adminProxyPort']
    adminProxyApplianceShortName = module.params['adminProxyApplianceShortName']
    omitAdminProxy = module.params['omitAdminProxy']

    # Setup logging for format, set log level and redirect to string
    strlog = StringIO()
    DEFAULT_LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s] [PID:%(process)d TID:%(thread)d] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': logLevel,
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'stream': strlog
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': logLevel,
                'propagate': True
            },
            'requests.packages.urllib3.connectionpool': {
                'handlers': ['default'],
                'level': 'ERROR',
                'propagate': True
            }
        }
    }
    logging.config.dictConfig(DEFAULT_LOGGING)

    # Create appliance object to be used for all calls
    if username == '' or username is None:
        u = ApplianceUser(password=password)
    else:
        u = ApplianceUser(username=username, password=password)

    # Create appliance object to be used for all calls
    # if adminProxy hostname is set, use the ISAMApplianceAdminProxy
    if adminProxyHostname == '' or adminProxyHostname is None or omitAdminProxy:
        isam_server = ISAMAppliance(hostname=appliance, user=u, lmi_port=lmi_port)
    else:
        isam_server = ISAMApplianceAdminProxy(adminProxyHostname=adminProxyHostname, user=u, hostname=appliance, adminProxyProtocol=adminProxyProtocol, adminProxyPort=adminProxyPort, adminProxyApplianceShortName=adminProxyApplianceShortName)

    # Create options string to pass to action method
    options = 'isamAppliance=isam_server, force=' + str(force)
    if module.check_mode is True:
        options = options + ', check_mode=True'
    if isinstance(module.params['isamapi'], dict):
        for key, value in module.params['isamapi'].items():
            if isinstance(value, basestring):
                options = options + ', ' + key + '="' + value + '"'
            else:
                options = options + ', ' + key + '=' + str(value)
    module.debug('Option to be passed to action: ' + options)

    # Dynamically process the action to be invoked
    # Simple check to restrict calls to just "isam" ones for safety
    if action.startswith('ibmsecurity.isam.'):
        try:
            module_name, method_name = action.rsplit('.', 1)
            module.debug('Action method to be imported from module: ' + module_name)
            module.debug('Action method name is: ' + method_name)
            mod = importlib.import_module(module_name)
            func_ptr = getattr(mod, method_name)  # Convert action to actual function pointer
            func_call = 'func_ptr(' + options + ')'

            startd = datetime.datetime.now()

            # Execute requested 'action'
            ret_obj = eval(func_call)

            endd = datetime.datetime.now()
            delta = endd - startd

            ret_obj['stdout'] = strlog.getvalue()
            ret_obj['stdout_lines'] = strlog.getvalue().split()
            ret_obj['start'] = str(startd)
            ret_obj['end'] = str(endd)
            ret_obj['delta'] = str(delta)
            ret_obj['cmd'] = action + "(" + options + ")"
            ret_obj['ansible_facts'] = isam_server.facts

            module.exit_json(**ret_obj)

        except ImportError:
            module.fail_json(name=action, msg='Error> action belongs to a module that is not found!',
                             log=strlog.getvalue())
        except AttributeError:
            module.fail_json(name=action, msg='Error> invalid action was specified, method not found in module!',
                             log=strlog.getvalue())
        except TypeError:
            module.fail_json(name=action,
                             msg='Error> action does not have the right set of arguments or there is a code bug! Options: ' + options,
                             log=strlog.getvalue())
        except IBMError as e:
            module.fail_json(name=action, msg=str(e), log=strlog.getvalue())
    else:
        module.fail_json(name=action, msg='Error> invalid action specified, needs to be isam!',
                         log=strlog.getvalue())


if __name__ == '__main__':
    main()
