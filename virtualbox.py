#!/usr/bin/python3
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.module_utils.basic import AnsibleModule
import importlib
import sys
import os

# from vboxapi_source import VirtualBoxManager


# sys.path.insert(0, 'web/VirtualBox_client.py')

# import web.VirtualBox_client

# from vbox_glue import *


#import ansible.module_utils.virtualbox.vbox_glue 
# from ansible.module_utils.vbox_glue import *

#from ansible.module_plugins.virtualbox.vboxapi import *

#from ansible.module_utils.cloud.virtualbox import *


#sys.path.insert(0, './vboxapi/VirtualBox_client.py')

# from vboxapi import *

#import VirtualBox_client

# from ansible.module_utils.cloud.virtualbox.vboxapi import *

# import sys
# import os
# import vapi
#from vbox_glue import *

# sys.path.insert(0, 'vbox_glue')

# import module_1
# from vbox_glue import *

# from vapi import *


#import vboxapi
#from vboxapi import VirtualBoxManager

# from sdk.VirtualBox_glue import *
# from sdk.VirtualBox_constants import *
# from web.VirtualBox_client import *
# from web.VirtualBox_types import *
# from web.VirtualBox_wrappers import *
# from xpcom.__init__ import *

# import weblib
# import xpcom

# from .vboxapi_source import VirtualBoxManager

#import vbox_api

# from vboxapi import VirtualBoxManager
# from vboxapi import PlatformWEBSERVICE
# import vboxapi

# sys.path.append(pathToFolderContainingScripts)  

working_directory = os.path.abspath(os.getcwd())

module_prefix_path_vbox_api = working_directory + '/VirtualBox_constants'
module_prefix_path_vbox_lib = working_directory + '/VirtualBox_client'
module_prefix_path_vbox_xpcom = working_directory + '/xpcom'

# sys.path.insert(0, module_prefix_path_vbox_api)

# print(sys.path)

# import vboxapi_source

# from vboxapi_source import *

# from (module_prefix_path_vbox_api) import *

# from vboxapi import VirtualBoxManager


# sys.path.insert(0, 'lib/VirtualBox_client.py')

# import sys

sys.path.append(module_prefix_path_vbox_api)

from VirtualBox_constants import *

sys.path.append(module_prefix_path_vbox_lib)

from VirtualBox_client import *
from VirtualBox_types import *
from VirtualBox_wrappers import *

sys.path.append(module_prefix_path_vbox_xpcom)

from xpcom import *

# import VirtualBox_client

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: virtualbox

short_description: VBox Cloud Api Adapter

version_added: "2.4"

description:
    - "This cloud vbox ansible adapter"

requirements:
  - requests

options:
    node_ip:
        description:
            - This is the node IP to send to the test module
        required: true
    username:
        description:
            - Control account api connection username
        required: true
    password:
        description:
            - Control account api connection password
        required: true
    api_port:
        description:
            - Control node api connection destination port 
        required: false

extends_documentation_fragment:
    - virtualbox

author:
    - Rostislav Grigoryev (@westsouthnight)
'''

EXAMPLES = '''
# Pass in a message
- name: Test connection to vbox server
  virtualbox:
    node_ip: 192.168.0.100
    username: vbox
    password: anypassword

# pass in a message and have changed true
- name: Test connection to vbox server done with a message and changed output
  virtualbox:
    node_ip: 192.168.0.100
    username: vbox
    password: anypassword

# fail the module
- name: Test connection to vbox server failure when running vbox the module
  virtualbox:
    node_ip: 192.168.0.100
    username: vbox
    password: anypassword
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
    returned: always
vbox_api_host:
    description: The output remote version show
    type: str
    returned: always
message:
    description: The output message
    type: str
    returned: always
list_machines:
    description: The output list of remote machines
    type: str
    returned: always
remote_version:
    description: The output remote version show
    type: str
    returned: always
machines_details:
    description: The output remote version show
    type: str
    returned: always
'''

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        node_ip=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        api_port=dict(type='str', required=False, default='18083'),
        name=dict(type='str', required=False),
        new=dict(type='bool', required=False, default=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)

    vbox_url='http://'+module.params['node_ip']+':'+module.params['api_port']

    # This code initializes VirtualBox manager with default style
    # and parameters
    # # # virtualBox_api_connection = vboxapi.connect(vbox_url, module.params['username'], module.params['password'])

    #virtualBoxManager = VirtualBoxManager(None, None)

    #virtualBoxManagerObject = vboxapi.VirtualBoxManager(None, None)

    #vbox_remote_version = virtualBox_api_connection.get_version()

    #vbox_remote_list_machines = virtualBox_api_connection.list_machines()


    # Alternatively, one can be more verbose, and initialize
    # glue with web service backend, and provide authentication
    # information
    #virtualBoxManagerObject = vboxapi.VirtualBoxManager("WEBSERVICE",{"url": vbox_url,"user":module.params['username'],:"password":module.params['password']})

    # # mgr = VirtualBoxManager(None, None)
    #vbox_api_call = virtualBoxManagerObject.getVirtualBox()

    result['original_message'] = 'ok'
    result['vbox_api_host'] = module.params['node_ip']
    result['message'] = 'vbox_url: '+vbox_url+' '+'Node IP: '+module.params['node_ip']+' '+'Username: '+module.params['username']+' '+'Password: '+module.params['password']+' '+'ApiPort: '+module.params['api_port']
    #result['list_machines'] = list(vbox_remote_list_machines)
    #result['remote_version'] = vbox_remote_version
    
    # list_of_machines = str(vbox_remote_list_machines).strip('[]')

    # machines_details = []

    # for virtual_machine in vbox_remote_list_machines:

    #     if virtual_machine not in '\'':

    #         vbox_remote_machine = virtualBox_api_connection.get_machine(virtual_machine)

    #         result['machines_details'] = result['machines_details'].extend(vbox_remote_machine)

    # result['machines_details'] = str(machines_details).strip('[]')

    #result['list_machines'] = 'vbox_remote_list_machines: '+ vbox_remote_list_machines.join(mylist)
    # name = "Linux"
    # mach = vbox.findMachine(name)
    # session = mgr.getSessionObject(vbox)
    # progress = mach.launchVMProcess(session, "gui", "")
    # progress.waitForCompletion(-1)
    # mgr.closeMachineSession(session)

    
    # vbox_remote_mgr = PlatformWEBSERVICE(None, None)
    # vbox_remote_mgr.user = module.params['username']
    # vbox_remote_mgr.password = module.params['username']
    # vbox_remote_mgr.url = vbox_url


    # vbox = mgr.vbox
    # name = "Linux"
    # mach = vbox.findMachine(name)
    # session = mgr.getSessionObject(vbox)
    # progress = mach.launchVMProcess(session, "gui", "")
    # progress.waitForCompletion(-1)
    # mgr.closeMachineSession(session)

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['name']:
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['node_ip'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()