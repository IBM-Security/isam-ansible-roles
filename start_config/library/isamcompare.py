#!/usr/bin/python

import logging
import logging.config
import sys
import importlib
from ansible.module_utils.basic import AnsibleModule
import datetime

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from ibmsecurity.appliance.isamappliance import ISAMAppliance
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
            action=dict(required=True),
            appliance1=dict(required=True),
            lmi_port1=dict(required=False, default=443, type='int'),
            username1=dict(required=False),
            password1=dict(required=True, no_log=True),
            appliance2=dict(required=True),
            lmi_port2=dict(required=False, default=443, type='int'),
            username2=dict(required=False),
            password2=dict(required=True, no_log=True),
            isamapi=dict(required=False, type='dict')
        ),
        supports_check_mode=False
    )

    module.debug('Started isamcompare module')

    # Process all Arguments
    logLevel = module.params['log']
    action = module.params['action']
    appliance1 = module.params['appliance1']
    lmi_port1 = module.params['lmi_port1']
    username1 = module.params['username1']
    password1 = module.params['password1']
    appliance2 = module.params['appliance2']
    lmi_port2 = module.params['lmi_port2']
    username2 = module.params['username2']
    password2 = module.params['password2']

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
    if username1 == '' or username1 is None:
        u1 = ApplianceUser(password=password1)
    else:
        u1 = ApplianceUser(username=username1, password=password1)
    isam_server1 = ISAMAppliance(hostname=appliance1, user=u1, lmi_port=lmi_port1)
    if username2 == '' or username2 is None:
        u2 = ApplianceUser(password=password2)
    else:
        u2 = ApplianceUser(username=username2, password=password2)
    isam_server2 = ISAMAppliance(hostname=appliance2, user=u2, lmi_port=lmi_port2)

    # Create options string to pass to action method
    options = 'isamAppliance1=isam_server1, isamAppliance2=isam_server2'
    if isinstance(module.params['isamapi'], dict):
        for key, value in module.params['isamapi'].items():
            if isinstance(value, basestring):
                options = options + ', ' + key + '="' + value + '"'
            else:
                options = options + ', ' + key + '=' + str(value)
    module.debug('Option to be passed to action: ' + options)

    # Dynamically process the module to be compared
    # Simple check to restrict calls to just "isam" ones for safety
    if action.startswith('ibmsecurity.isam.'):
        try:
            mod = importlib.import_module(action)
            method_name = 'compare'  # Standard function to be implemented in every module
            func_ptr = getattr(mod, method_name)  # Convert 'compare' to actual function pointer
            func_call = 'func_ptr(' + options + ')'

            startd = datetime.datetime.now()

            # Execute compare for given action
            ret_obj = eval(func_call)

            endd = datetime.datetime.now()
            delta = endd - startd

            ret_obj['stdout'] = strlog.getvalue()
            ret_obj['stdout_lines'] = strlog.getvalue().split()
            ret_obj['start'] = str(startd)
            ret_obj['end'] = str(endd)
            ret_obj['delta'] = str(delta)
            ret_obj['cmd'] = action + ".compare(" + options + ")"
            srv_facts = {}
            srv_facts['server1'] = isam_server1.facts
            srv_facts['server2'] = isam_server2.facts
            ret_obj['ansible_facts'] = srv_facts

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
