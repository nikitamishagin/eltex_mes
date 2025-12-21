#
# (c) 2019 Red Hat Inc.
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

import json

from os import path
from unittest import TestCase
from unittest.mock import MagicMock

from ansible.module_utils._text import to_bytes
from ansible_collections.nikitamishagin.eltex_mes.plugins.cliconf import mes


b_FIXTURE_DIR = b"%s/fixtures/mes" % (
    to_bytes(path.dirname(path.abspath(__file__)), errors="surrogate_or_strict")
)


def _connection_side_effect(*args, **kwargs):
    try:
        if args:
            value = args[0]
        else:
            value = kwargs.get("command")

        fixture_path = path.abspath(
            b"%s/%s" % (b_FIXTURE_DIR, b"_".join(value.split(b" "))),
        )
        with open(fixture_path, "rb") as file_desc:
            return file_desc.read()
    except (OSError, IOError):
        if args:
            value = args[0]
            return value
        elif kwargs.get("command"):
            value = kwargs.get("command")
            return value

        return "Nope"


class TestPluginCLIConfMES(TestCase):
    """Test class for MES CLI Conf Methods"""

    def setUp(self):
        self._mock_connection = MagicMock()
        self._mock_connection.send.side_effect = _connection_side_effect
        self._cliconf = mes.Cliconf(self._mock_connection)
        self.maxDiff = None

    def tearDown(self):
        pass

    def test_get_device_info(self):
        """Test get_device_info"""
        device_info = self._cliconf.get_device_info()

        mock_device_info = {
            "network_os": "mes",
            "network_os_model": "MES2324P",
            "network_os_version": "6.6.3.8",
            "network_os_inactive_version": "6.5.1.6",
            "network_os_hostname": "SW1",
            "network_os_image": "flash://system/images/mes3300-663-8R4.ros",
            "network_os_inactive_image": "flash://system/images/_image1.bin",
            "network_os_type": "L2",
        }

        self.assertEqual(device_info, mock_device_info)

    def test_get_capabilities(self):
        """Test get_capabilities"""
        capabilities = json.loads(self._cliconf.get_capabilities())
        mock_capabilities = {
            "device_info": {
                "network_os": "mes",
                "network_os_hostname": "SW1",
                "network_os_image": "flash://system/images/mes3300-663-8R4.ros",
                "network_os_inactive_image": "flash://system/images/_image1.bin",
                "network_os_inactive_version": "6.5.1.6",
                "network_os_model": "MES2324P",
                "network_os_type": "L2",
                "network_os_version": "6.6.3.8",
            },
            "device_operations": {
                "supports_commit": False,
                "supports_commit_comment": False,
                "supports_defaults": True,
                "supports_diff_ignore_lines": True,
                "supports_diff_match": True,
                "supports_diff_replace": True,
                "supports_generate_diff": True,
                "supports_multiline_delimiter": True,
                "supports_onbox_diff": False,
                "supports_replace": False,
                "supports_rollback": False,
            },
            "diff_match": ["line", "strict", "exact", "none"],
            "diff_replace": ["line", "block"],
            "format": ["text"],
            "network_api": "cliconf",
            "output": [],
            "rpc": [
                "edit_config",
                "enable_response_logging",
                "get",
                "get_capabilities",
                "get_config",
                "disable_response_logging",
                "run_commands",
                "edit_banner",
                "get_diff",
                "run_commands",
                "get_defaults_flag",
            ],
        }
        self.assertEqual(sorted(mock_capabilities), sorted(capabilities))
