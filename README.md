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
- hosts: supervio
  sudo: True
  connection: local
  roles:
    - pip
  vars:
    - update_package_cache: True
```

## License

TBD

## Author Information

This role was created in 2015 by [Tom Hite / VMware](http://www.vmware.com/).
