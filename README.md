# ansible-role-pip

[Ansible](https://github.com/ansible/ansible) role for manipulating
Python pip installation. This role removes packager installs and
instead uses easy_install so as to pick up more recent pip versions.

## Requirements

This role currently supports only Debian/Ubuntu distros.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    update_package_cache: True

Whether to update the aptitude, yum, pacman or other package cache before running any install tasks.

## Example playbook

```
---
- hosts: piphosts
  sudo: True
  connection: local
  roles:
    - pip
  vars:
    - update_package_cache: True
```

# License and Copyright
 
Copyright 2015 VMware, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Author Information

This role was created in 2015 by [Tom Hite / VMware](http://www.vmware.com/).
