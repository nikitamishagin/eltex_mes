.. _nikitamishagin.eltex_mes.mes_command_module:


************************************
nikitamishagin.eltex_mes.mes_command
************************************

**Module to run commands on remote devices.**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Sends arbitrary commands to an ios node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module does not support running commands in configuration mode. Please use mes_config to configure MES devices.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=raw</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of commands to send to the remote ios device over the configured provider. The resulting output from the command is returned. If the <em>wait_for</em> argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. If a command sent to the device requires answering a prompt, it is possible to pass a dict containing <em>command</em>, <em>answer</em> and <em>prompt</em>. Common answers are &#x27;y&#x27; or &quot;\r&quot; (carriage return, must be double quotes). See examples.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">1</div>
                </td>
                <td>
                        <div>Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>any</li>
                                    <li><div style="color: blue"><b>all</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>The <em>match</em> argument is used in conjunction with the <em>wait_for</em> argument to specify the match policy.  Valid values are <code>all</code> or <code>any</code>.  If the value is set to <code>all</code> then all conditionals in the wait_for must be satisfied.  If the value is set to <code>any</code> then only one of the values must be satisfied.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>retries</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">9</div>
                </td>
                <td>
                        <div>Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the <em>wait_for</em> conditions.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>wait_for</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: waitfor</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module works with connection ``network_cli``. See https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html



Examples
--------

.. code-block:: yaml

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



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>failed_conditions</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>failed</td>
                <td>
                            <div>The list of conditionals that have failed</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;...&#x27;, &#x27;...&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>stdout</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always apart from low level errors (such as action plugin)</td>
                <td>
                            <div>The set of responses from the commands</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;...&#x27;, &#x27;...&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>stdout_lines</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always apart from low level errors (such as action plugin)</td>
                <td>
                            <div>The value of stdout split into a list</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[[&#x27;...&#x27;, &#x27;...&#x27;], [&#x27;...&#x27;], [&#x27;...&#x27;]]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Peter Sprygada (@privateip)
