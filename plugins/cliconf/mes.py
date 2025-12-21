#
# (c) 2017 Red Hat Inc.
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
# Copyright 2025 Nikita Mishagin
# Modified from cisco.ios to Eltex MES
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type

# Note: commit-confirm workflow from Cisco IOS is not supported on Eltex MES.
DOCUMENTATION = """
author:
- Ansible Networking Team (@ansible-network)
- Nikita Mishagin
name: mes
short_description: Use mes cliconf to run commands on Eltex MES platform
description:
- This mes plugin provides low-level abstraction APIs for sending and receiving CLI
  commands from Eltex MES network devices.
version_added: 1.0.0
options:
  config_commands:
    description:
    - Specifies a list of commands that can make configuration changes
      to the target device.
    - When `ansible_network_single_user_mode` is enabled, if a command sent
      to the device is present in this list, the existing cache is invalidated.
    version_added: 2.0.0
    type: list
    elements: str
    default: []
    vars:
    - name: ansible_mes_config_commands
"""

EXAMPLES = """
- name: Set hostname on Eltex MES
  tasks:
    - name: Configure hostname
      nikitamishagin.eltex_mes.mes_hostname:
        state: merged
        config:
          hostname: SW1

"""

import json
import re
import time

from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils._text import to_text
from ansible.module_utils.common._collections_compat import Mapping
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.config import (
    NetworkConfig,
    dumps,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list
from ansible_collections.ansible.netcommon.plugins.plugin_utils.cliconf_base import (
    CliconfBase,
    enable_mode,
)


class Cliconf(CliconfBase):
    def __init__(self, *args, **kwargs):
        self._device_info = {}
        super(Cliconf, self).__init__(*args, **kwargs)

    @enable_mode
    def get_config(self, source="running", flags=None, format=None):
        if source != "running":
            raise ValueError("fetching configuration from %s is not supported" % source)

        if format:
            raise ValueError("'format' value %s is not supported for get_config" % format)

        if not flags:
            flags = []

        cmd = "show running-config "
        cmd += " ".join(to_list(flags))
        cmd = cmd.strip()

        return self.send_command(cmd)

    # I'm not sure if this can be used in Eltex MES, but let's leave it for now
    # @enable_mode
    # def restore(self, filename=None, path=""):
    #     if not filename:
    #         raise ValueError("'file_name' value is required for restore")
    #     cmd = f"configure replace {path}{filename} force"
    #     return self.send_command(cmd)

    def get_diff(
        self,
        candidate=None,
        running=None,
        diff_match="line",
        diff_ignore_lines=None,
        path=None,
        diff_replace="line",
    ):
        """
        Generate diff between candidate and running configuration. If the
        remote host supports onbox diff capabilities ie. supports_onbox_diff in that case
        candidate and running configurations are not required to be passed as argument.
        In case if onbox diff capability is not supported candidate argument is mandatory
        and running argument is optional.
        :param candidate: The configuration which is expected to be present on remote host.
        :param running: The base configuration which is used to generate diff.
        :param diff_match: Instructs how to match the candidate configuration with current device configuration
                           Valid values are 'line', 'strict', 'exact', 'none'.
                           'line' - commands are matched line by line
                           'strict' - command lines are matched with respect to position
                           'exact' - command lines must be an equal match
                           'none' - will not compare the candidate configuration with the running configuration
        :param diff_ignore_lines: Use this argument to specify one or more lines that should be
                                  ignored during the diff.  This is used for lines in the configuration
                                  that are automatically updated by the system.  This argument takes
                                  a list of regular expressions or exact line matches.
        :param path: The ordered set of parents that uniquely identify the section or hierarchy
                     the commands should be checked against.  If the parents argument
                     is omitted, the commands are checked against the set of top
                     level or global commands.
        :param diff_replace: Instructs on the way to perform the configuration on the device.
                             If the replace argument is set to I(line) then the modified lines are
                             pushed to the device in configuration mode.  If the replace argument is
                             set to I(block) then the entire command block is pushed to the device in
                             configuration mode if any line is not correct.
        :return: Configuration diff in json format.
                 {
                     'config_diff': '',
                     'banner_diff': {}
                 }
        """
        diff = {}
        device_operations = self.get_device_operations()
        option_values = self.get_option_values()

        if candidate is None and device_operations["supports_generate_diff"]:
            raise ValueError("candidate configuration is required to generate diff")

        if diff_match not in option_values["diff_match"]:
            raise ValueError(
                "'match' value %s in invalid, valid values are %s"
                % (diff_match, ", ".join(option_values["diff_match"])),
            )

        if diff_replace not in option_values["diff_replace"]:
            raise ValueError(
                "'replace' value %s in invalid, valid values are %s"
                % (diff_replace, ", ".join(option_values["diff_replace"])),
            )

        # prepare candidate configuration
        candidate_obj = NetworkConfig(indent=1)
        want_src, want_banners = self._extract_banners(candidate)
        candidate_obj.load(want_src)

        if running and diff_match != "none":
            # running configuration
            have_src, have_banners = self._extract_banners(running)
            running_obj = NetworkConfig(indent=1, contents=have_src, ignore_lines=diff_ignore_lines)
            configdiffobjs = candidate_obj.difference(
                running_obj,
                path=path,
                match=diff_match,
                replace=diff_replace,
            )

        else:
            configdiffobjs = candidate_obj.items
            have_banners = {}

        diff["config_diff"] = dumps(configdiffobjs, "commands") if configdiffobjs else ""
        banners = self._diff_banners(want_banners, have_banners)
        diff["banner_diff"] = banners if banners else {}
        return diff

    @enable_mode
    def configure(self):
        """
        Enter global configuration mode
        :return: None
        """
        # Enter configuration mode on Eltex MES
        self.send_command("configure terminal")

    @enable_mode
    def edit_config(self, candidate=None, commit=True, replace=None, comment=None):
        resp = {}
        operations = self.get_device_operations()
        self.check_edit_config_capability(operations, candidate, commit, replace, comment)

        results = []
        requests = []
        if commit:
            self.configure()
            try:
                for line in to_list(candidate):
                    if not isinstance(line, Mapping):
                        line = {"command": line}

                    cmd = line["command"]
                    if cmd != "end" and cmd[0] != "!":
                        results.append(self.send_command(**line))
                        requests.append(cmd)

            finally:
                # guaranteed exit from configuration mode
                self.send_command("end")
        else:
            raise ValueError("check mode is not supported")

        resp["request"] = requests
        resp["response"] = results
        return resp

    def edit_macro(self, candidate=None, commit=True, replace=None, comment=None):
        """
        mes_config:
          lines: "{{ macro_lines }}"
          parents: "macro name {{ macro_name }}"
          after: '@'
          match: line
          replace: block
        """
        resp = {}
        operations = self.get_device_operations()
        self.check_edit_config_capability(operations, candidate, commit, replace, comment)

        results = []
        requests = []
        if commit:
            commands = ""
            self.send_command("configure terminal")
            time.sleep(0.1)
            # first item: macro command
            commands += candidate.pop(0) + "\n"
            multiline_delimiter = candidate.pop(-1)
            for line in candidate:
                commands += " " + line + "\n"
            commands += multiline_delimiter + "\n"
            obj = {"command": commands, "sendonly": True}
            results.append(self.send_command(**obj))
            requests.append(commands)

            time.sleep(0.1)
            self.send_command("end", sendonly=True)
            time.sleep(0.1)
            results.append(self.send_command("\n"))
            requests.append("\n")

        resp["request"] = requests
        resp["response"] = results
        return resp

    def get(
        self,
        command=None,
        prompt=None,
        answer=None,
        sendonly=False,
        newline=True,
        output=None,
        check_all=False,
    ):
        if not command:
            raise ValueError("must provide value of command to execute")
        if output:
            raise ValueError("'output' value %s is not supported for get" % output)

        return self.send_command(
            command=command,
            prompt=prompt,
            answer=answer,
            sendonly=sendonly,
            newline=newline,
            check_all=check_all,
        )

    def check_device_type(self):
        device_type = "L2"
        try:
            self.get(command="show vlan")
        except Exception:
            device_type = "L3"
        return device_type

    def get_device_info(self):
        if not self._device_info:
            device_info = {"network_os": "mes"}

            # Ensure we are not in config mode
            self._update_cli_prompt_context(config_context=")#", exit_command="end")

            # Get information about software versions
            reply = self.get(command="show version")
            data = to_text(reply, errors="surrogate_or_strict").strip()

            # Search an active image (path and version)
            active_match = re.search(
                r"Active-image:\s+(\S+)\n\s+Version:\s+(\S+)",
                data,
                re.S | re.I,
            )
            if active_match:
                device_info["network_os_image"] = active_match.group(1)
                device_info["network_os_version"] = active_match.group(2)

            # Search an inactive image (path and version)
            inactive_match = re.search(
                r"Inactive-image:\s+(\S+)\n\s+Version:\s+(\S+)",
                data,
                re.S | re.I,
            )
            if inactive_match:
                device_info["network_os_inactive_image"] = inactive_match.group(1)
                device_info["network_os_inactive_version"] = inactive_match.group(2)

            # Get information about a device
            reply = self.get(command="show system")
            data = to_text(reply, errors="surrogate_or_strict").strip()

            # Search a model name and hostname
            device_match = re.search(
                r"System Description:\s+(MES\S+)[\s\S]*?System Name:\s+(\S+)",
                data,
                re.M | re.I,
            )
            if device_match:
                device_info["network_os_model"] = device_match.group(1).strip(",")
                device_info["network_os_hostname"] = device_match.group(2).strip(",")

            device_info["network_os_type"] = self.check_device_type()
            self._device_info = device_info

        return self._device_info

    def get_device_operations(self):
        return {
            "supports_diff_replace": True,
            "supports_commit": False,
            "supports_rollback": False,
            "supports_defaults": True,
            "supports_onbox_diff": False,
            "supports_commit_comment": False,
            "supports_multiline_delimiter": True,
            "supports_diff_match": True,
            "supports_diff_ignore_lines": True,
            "supports_generate_diff": True,
            "supports_replace": False,
        }

    def get_option_values(self):
        return {
            "format": ["text"],
            "diff_match": ["line", "strict", "exact", "none"],
            "diff_replace": ["line", "block"],
            "output": [],
        }

    def get_capabilities(self):
        result = super(Cliconf, self).get_capabilities()
        result["rpc"] += ["edit_banner", "get_diff", "run_commands", "get_defaults_flag"]
        result["device_operations"] = self.get_device_operations()
        result.update(self.get_option_values())
        return json.dumps(result)

    def edit_banner(self, candidate=None, multiline_delimiter="@", commit=True):
        """
        Edit banner on remote device
        :param banners: Banners to be loaded in json format
        :param multiline_delimiter: Line delimiter for banner
        :param commit: Boolean value that indicates if the device candidate
               configuration should be  pushed in the running configuration or discarded.
        :param diff: Boolean flag to indicate if configuration applied on remote host should be
               generated and returned in response or not
        :return: Returns response of executing the configuration command received
                 from remote host
        """
        resp = {}
        banners_obj = json.loads(candidate)
        results = []
        requests = []
        if commit:
            for key, value in banners_obj.items():
                key += " %s" % multiline_delimiter
                self.send_command("config terminal", sendonly=True)
                for cmd in [key, value, multiline_delimiter]:
                    obj = {"command": cmd, "sendonly": True}
                    results.append(self.send_command(**obj))
                    requests.append(cmd)

                self.send_command("end", sendonly=True)
                time.sleep(0.1)
                results.append(self.send_command("\n"))
                requests.append("\n")

        resp["request"] = requests
        resp["response"] = results

        return resp

    def run_commands(self, commands=None, check_rc=True):
        if commands is None:
            raise ValueError("'commands' value is required")

        responses = list()
        for cmd in to_list(commands):
            if not isinstance(cmd, Mapping):
                cmd = {"command": cmd}

            output = cmd.pop("output", None)
            if output:
                raise ValueError("'output' value %s is not supported for run_commands" % output)

            try:
                out = self.send_command(**cmd)
            except AnsibleConnectionFailure as e:
                if check_rc:
                    raise
                out = getattr(e, "err", to_text(e))

            responses.append(out)

        return responses

    def get_defaults_flag(self):
        """
        The method identifies the filter that should be used to fetch running-configuration
        with defaults.
        :return: Valid default filter
        """
        out = self.get("show running-config ?")
        out = to_text(out, errors="surrogate_then_replace")

        commands = set()
        for line in out.splitlines():
            if line.strip():
                commands.add(line.strip().split()[0])

        if "all" in commands:
            return "all"
        else:
            return "full"

    def set_cli_prompt_context(self):
        """
        Make sure we are in the operational cli mode
        :return: None
        """
        if self._connection.connected:
            out = self._connection.get_prompt()

            if out is None:
                raise AnsibleConnectionFailure(
                    message="cli prompt is not identified from the last received"
                    " response window: %s" % self._connection._last_recv_window,
                )

            if re.search(r"config.*\)#", to_text(out, errors="surrogate_then_replace").strip()):
                self._connection.queue_message("vvvv", "wrong context, sending end to device")
                self._connection.send_command("end")

    def _extract_banners(self, config):
        banners = {}
        banner_cmds = re.findall(r"^banner (\w+)", config, re.M)
        for cmd in banner_cmds:
            regex = r"banner %s \^C(.+?)(?=\^C)" % cmd
            match = re.search(regex, config, re.S)
            if match:
                key = "banner %s" % cmd
                banners[key] = match.group(1).strip()

        for cmd in banner_cmds:
            regex = r"banner %s \^C(.+?)(?=\^C)" % cmd
            match = re.search(regex, config, re.S)
            if match:
                config = config.replace(str(match.group(1)), "")

        config = re.sub(r"banner \w+ \^C\^C", "!! banner removed", config)
        return config, banners

    def _diff_banners(self, want, have):
        candidate = {}
        for key, value in want.items():
            if value != have.get(key):
                candidate[key] = value
        return candidate
