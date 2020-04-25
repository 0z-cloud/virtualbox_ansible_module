# Ansible virtualbox cloud management module

Implements features for management your VirtualBox instances, standalone hypervisors and groups of hosts via ansible. 

## Basic test call


```
- name: test vbox module
  hosts: localhost
  tasks:

  - name: Run the vbox module for success
    virtualbox:
      node_ip: '172.16.77.19'
      username: vbox
      password: '#SDtBnJuUBeQa4GJq!Zhw8EVLQatsk'
    register: test_success_out
  
  - name: Debug the test_success_out
    debug:
      msg: '{{ test_success_out }}'
```
