#!/usr/bin/python
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2026 Nikita Mishagin
# Modified from cisco.ios to Eltex MES
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: mes_command
author: Peter Sprygada (@privateip)
short_description: Module to run commands on remote devices.
description:
  - Sends arbitrary commands to an ios node and returns the results read from the device.
    This module includes an argument that will cause the module to wait for a specific
    condition before returning or timing out if the condition is not met.
  - This module does not support running commands in configuration mode. Please use
    mes_config to configure MES devices.
version_added: 1.0.0
notes:
  - This module works with connection C(network_cli).
    See U(https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html)
options:
  commands:
    description:
      - List of commands to send to the remote ios device over the configured provider.
        The resulting output from the command is returned. If the I(wait_for) argument
        is provided, the module is not returned until the condition is satisfied or
        the number of retries has expired. If a command sent to the device requires
        answering a prompt, it is possible to pass a dict containing I(command), I(answer)
        and I(prompt). Common answers are 'y' or "\\r" (carriage return, must be double
        quotes). See examples.
    required: true
    type: list
    elements: raw
  wait_for:
    description:
      - List of conditions to evaluate against the output of the command. The task will
        wait for each condition to be true before moving forward. If the conditional
        is not true within the configured number of retries, the task fails. See examples.
    aliases:
      - waitfor
    type: list
    elements: str
  match:
    description:
      - The I(match) argument is used in conjunction with the I(wait_for) argument to
        specify the match policy.  Valid values are C(all) or C(any).  If the value
        is set to C(all) then all conditionals in the wait_for must be satisfied.  If
        the value is set to C(any) then only one of the values must be satisfied.
    default: all
    type: str
    choices:
      - any
      - all
  retries:
    description:
      - Specifies the number of retries a command should by tried before it is considered
        failed. The command is run on the target device every retry and evaluated against
        the I(wait_for) conditions.
    default: 9
    type: int
  interval:
    description:
      - Configures the interval in seconds to wait between retries of the command. If
        the command does not pass the specified conditions, the interval indicates how
        long to wait before trying the command again.
    default: 1
    type: int
"""

EXAMPLES = r"""
- name: Run show version on remote devices
  nikitamishagin.eltex_mes.mes_command:
    commands: show version

# output-

# ok: [sw1] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "show version"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": null
#         }
#     },
#     "stdout": [
#         "Active-image: flash://system/images/mes3300-663-8R4.ros\n  Version: 6.6.3.8 ... Time: 12:35:37"
#     ],
#     "stdout_lines": [
#         [
#             "Active-image: flash://system/images/mes3300-663-8R4.ros",
#             "  Version: 6.6.3.8",
#             "..."
#             "  Time: 12:35:37"
#         ]
#     ]
# }

- name: Run show system and check to see if output contains MES
  nikitamishagin.eltex_mes.mes_command:
    commands: show system
    wait_for: result[0] contains MES

# output-

# ok: [sw1] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "show system"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": [
#                 "result[0] contains MES"
#             ]
#         }
#     },
#     "stdout": [
#         "System Description:                       MES2324P AC 28-port 1G/10G Managed Switch with 24 POE+ ... OK"
#     ],
#     "stdout_lines": [
#         [
#             "System Description:                       MES2324P AC 28-port 1G/10G Managed Switch with 24 POE+ ports",
#             "System Up Time (days,hour:min:sec):       51,04:18:34",
#             "..."
#             " 1            43              OK"
#         ]
#     ]
# }

- name: Run multiple commands on remote nodes
  nikitamishagin.eltex_mes.mes_command:
    commands:
      - show version
      - show interfaces

# output-

# ok: [sw1] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "show version",
#                 "show interfaces"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": null
#         }
#     },
#     "stdout": [
#         "Active-image: flash://system/images/mes3300-663-8R4.ros\n  Version: 6.6.3.8 ... Time: 12:35:37",
#         "GigabitEthernet1/0/1 is down (not connected) ...      8: 0/0"
#     ],
#     "stdout_lines": [
#         [
#             "Active-image: flash://system/images/mes3300-663-8R4.ros",
#             "  Version: 6.6.3.8",
#             "..."
#             "  Time: 12:35:37"
#         ],
#         [
#             "GigabitEthernet1/0/1 is down (not connected)",
#             "   Interface index is 49",
#             "...",
#             "      8: 0/0"
#         ]
#     ]
# }

- name: Run multiple commands and evaluate the output
  nikitamishagin.eltex_mes.mes_command:
    commands:
      - show system
      - show interfaces
    wait_for:
      - result[0] contains MES
      - result[1] contains Loopback0

# output-
# failed play as result[1] contains Loopback0 is false

# fatal: [sw1]: FAILED! => {
#     "changed": false,
#     "failed_conditions": [
#         "result[1] contains Loopback0"
#     ],
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "show system",
#                 "show interfaces"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": [
#                 "result[0] contains MES",
#                 "result[1] contains Loopback0"
#             ]
#         }
#     },
#     "msg": "One or more conditional statements have not been satisfied"
# }

- name: Run commands that require answering a prompt
  nikitamishagin.eltex_mes.mes_command:
    commands:
      - command: write
        prompt: 'Overwrite file [startup-config].... (Y/N)[N] ?'
        answer: "y"

# output-

# ok: [sw1] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 {
#                     "answer": "y",
#                     "check_all": false,
#                     "command": "write",
#                     "newline": true,
#                     "output": null,
#                     "prompt": "Overwrite file [startup-config].... (Y/N)[N] ?",
#                     "sendonly": false
#                 }
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": null
#         }
#     },
#     "stdout": [
#         "Overwrite file [startup-config].... (Y/N)[N] ?y\nCopy succeeded"
#     ],
#     "stdout_lines": [
#         [
#             "Overwrite file [startup-config].... (Y/N)[N] ?y",
#             "Copy succeeded"
#         ]
#     ]
# }

- name: Run commands with complex values like special characters in variables
  nikitamishagin.eltex_mes.mes_command:
    commands:
      ["{{ 'username ' ~ user ~ ' password ' ~ password ~ ' privilege 1' }}"]
  vars:
    user: "admin"
    password: "eltex"

# ok: [sw1] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "username admin password eltex privilege 1"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": null
#         }
#     },
#     "stdout": [],
#     "stdout_lines": []
# }
"""

RETURN = """
stdout:
  description: The set of responses from the commands
  returned: always apart from low level errors (such as action plugin)
  type: list
  sample: ['...', '...']
stdout_lines:
  description: The value of stdout split into a list
  returned: always apart from low level errors (such as action plugin)
  type: list
  sample: [['...', '...'], ['...'], ['...']]
failed_conditions:
  description: The list of conditionals that have failed
  returned: failed
  type: list
  sample: ['...', '...']
"""
import time

from ansible.module_utils._text import to_text
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.parsing import (
    Conditional,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_lines,
    transform_commands,
)
from ansible_collections.nikitamishagin.eltex_mes.plugins.module_utils.network.mes.mes import (
    run_commands,
)


def parse_commands(module, warnings):
    commands = transform_commands(module)
    if module.check_mode:
        for item in list(commands):
            if not item["command"].startswith("show"):
                warnings.append(
                    "Only show commands are supported when using check mode, not executing %s"
                    % item["command"],
                )
                commands.remove(item)
    return commands


def main():
    """main entry point for module execution"""
    argument_spec = dict(
        commands=dict(type="list", elements="raw", required=True),
        wait_for=dict(type="list", elements="str", aliases=["waitfor"]),
        match=dict(default="all", choices=["all", "any"]),
        retries=dict(default=9, type="int"),
        interval=dict(default=1, type="int"),
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    warnings = list()
    result = {"changed": False, "warnings": warnings}
    commands = parse_commands(module, warnings)
    wait_for = module.params["wait_for"] or list()
    conditionals = []
    try:
        conditionals = [Conditional(c) for c in wait_for]
    except AttributeError as exc:
        module.fail_json(msg=to_text(exc))
    retries = module.params["retries"]
    interval = module.params["interval"]
    match = module.params["match"]
    responses = []
    while retries >= 0:
        responses = run_commands(module, commands)
        for item in list(conditionals):
            if item(responses):
                if match == "any":
                    conditionals = list()
                    break
                conditionals.remove(item)
        if not conditionals:
            break
        time.sleep(interval)
        retries -= 1
    if conditionals:
        failed_conditions = [item.raw for item in conditionals]
        msg = "One or more conditional statements have not been satisfied"
        module.fail_json(msg=msg, failed_conditions=failed_conditions)
    result.update({"stdout": responses, "stdout_lines": list(to_lines(responses))})
    module.exit_json(**result)


if __name__ == "__main__":
    main()
