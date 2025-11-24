# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# Copyright 2025 Nikita Mishagin
# Modified from cisco.ios to Eltex MES
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The Hostname parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class HostnameTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(HostnameTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "hostname",
            "getval": re.compile(
                r"""
                ^hostname\s(?P<hostname>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "hostname {{ hostname }}",
            "result": {
                "hostname": "{{ hostname }}",
            },
        },
    ]
    # fmt: on
