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
from ibmsecurity.user.isamuser import ISAMUser

logger = logging.getLogger(sys.argv[0])


def main():
    module = AnsibleModule(
        argument_spec=dict(
            log=dict(default='INFO', choices=['DEBUG', 'INFO', 'ERROR', 'CRITICAL']),
            appliance=dict(required=True),
            lmi_port=dict(required=False, default=443, type='int'),
            username=dict(required=False),
            password=dict(required=True, no_log=True),
            isamuser=dict(required=False),
            isampwd=dict(required=True, no_log=True),
            isamdomain=dict(required=False, default='Default'),
            commands=dict(required=True, type='list'),
            adminProxyProtocol=dict(required=False, default='https', choices=['http','https']),
            adminProxyHostname=dict(required=False),
            adminProxyPort=dict(required=False, default=443, type='int'),
            adminProxyApplianceShortName=dict(required=False, default=False, type='bool'),
            omitAdminProxy=dict(required=False, default=False, type='bool')
        ),
        supports_check_mode=False
    )

    module.debug('Started isamadmin module')

    # Process all Arguments
    logLevel = module.params['log']
    appliance = module.params['appliance']
    lmi_port = module.params['lmi_port']
    username = module.params['username']
    password = module.params['password']
    isamuser = module.params['isamuser']
    isampwd = module.params['isampwd']
    isamdomain = module.params['isamdomain']
    commands = module.params['commands']
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
        isam_server = ISAMApplianceAdminProxy(adminProxyHostname=adminProxyHostname, user=u, hostname=appliance,
                                              adminProxyProtocol=adminProxyProtocol, adminProxyPort=adminProxyPort,
                                              adminProxyApplianceShortName=adminProxyApplianceShortName)

    if isamuser == '' or isamuser is None:
        iu = ISAMUser(password=isampwd)
    else:
        iu = ISAMUser(username=isamuser, password=isampwd)

    try:
        import ibmsecurity.isam.web.runtime.pdadmin

        startd = datetime.datetime.now()

        ret_obj = ibmsecurity.isam.web.runtime.pdadmin.execute(isamAppliance=isam_server, isamUser=iu,
                                                               admin_domain=isamdomain, commands=commands)

        endd = datetime.datetime.now()
        delta = endd - startd

        ret_obj['stdout'] = strlog.getvalue()
        ret_obj['stdout_lines'] = strlog.getvalue().split()
        ret_obj['start'] = str(startd)
        ret_obj['end'] = str(endd)
        ret_obj['delta'] = str(delta)
        ret_obj[
            'cmd'] = "ibmsecurity.isam.config_fed_dir.runtime.pdadmin.execute(isamAppliance=isam_server, isamUser=iu, commands=" + str(
            commands) + ")"
        ret_obj['ansible_facts'] = isam_server.facts

        module.exit_json(**ret_obj)

    except ImportError:
        module.fail_json(name='pdadmin', msg='Error> Unable to import pdadmin module!', log=strlog.getvalue())
    except AttributeError:
        module.fail_json(name='pdadmin', msg='Error> Error finding execute function of pdadmin module',
                         log=strlog.getvalue())
    except TypeError:
        module.fail_json(name='pdadmin', msg='Error> pdadmin has wrong set of arguments or there is a bug in code!',
                         log=strlog.getvalue())
    except IBMError as e:
        module.fail_json(name='pdadmin', msg=str(e), log=strlog.getvalue())


if __name__ == '__main__':
    main()
