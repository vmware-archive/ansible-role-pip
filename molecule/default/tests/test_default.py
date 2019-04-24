# Copyright © 2017 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0 OR GPL-3.0-only
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_command(Command):
    assert Command('pip --version').rc == 0
