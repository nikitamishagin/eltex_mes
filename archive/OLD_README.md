# Description (files in ./archive/)

Playbooks for automating routine administration tasks of Eltex switches.
(mes2100, mes2300, mes3300, mes3500, mes5300 series.)

Modules ios_command and ios_config are (almost) suitable for working with Eltex switches. I made two changes to the
modules:

1. File `/ansible_collections/cisco/ios/plugins/cliconf/ios.py`. You need to replace the following command:
   `self.send_command("configure terminal")` // "configure terminal" -> "configure"
2. File `/ansible_collections/cisco/ios/plugins/terminal/ios.py`. You need to replace the following command:
   `self._exec_cli_command(b"terminal length 0")` // "terminal length 0" -> "terminal datadump"

These changes will let you use some basic cisco.ios modules with Eltex MES devices. But you should not use a
`gather_facts` function, because it will not work correctly. Set `gather_facts: false` in your playbook by default.

Also, you can see my old playbooks for some tasks:

- `./archive/mes-upgrade.yml` - playbook for downloading new firmware images;
- `./archive/mes-schedule.yml` - playbook for restarting switches on a schedule;
- `./archive/mes-ntp-check.yml` - playbook for configuring NTP servers;
- `./archive/mes2300-global-config.yml` - playbook for configuring global parameters.

`*.textfsm` - templates for parsing.

**Warning: This is an old and clumsy way to use the cisco.ios collection. I recommend using it only for
familiarization.**
