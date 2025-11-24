# Eltex Ansible Project

**PROJECT UNDER DEVELOPMENT**

🚀 Join the effort to build a dedicated Eltex Ansible collection!

If you work with Eltex network devices and are familiar with Ansible/Python, I invite you to contribute. The plan is a
phased adaptation of modules from the cisco.ios collection for Eltex devices. Please propose and implement your
Eltex-specific adaptations following the roadmap below.

I’m happy to receive any suggestions, ideas, and support for creating this collection. Thank you!

## Common plan for improvement

- [x] Fork the Ansible cisco.ios collection
- [x] Create a list of modules that can be adapted for Eltex
- [ ] Define the order of the most important modules
- [ ] Implement getting facts for Eltex devices
- [ ] Implement the modules in this order
- [ ] Identify useful Ansible roles for device configuration
- [ ] Create the Ansible roles
- [ ] Prepare Ansible playbooks

Ansible Cisco IOS Collection: https://github.com/ansible-collections/cisco.ios

## Progress of improvement

- The improvement plan has been drafted and added to the README.
- A brief section for contributors has been added.
- A new branch has been created to evolve the project into an Ansible collection. The branch is named
  `feature/ansible-collection`. It is currently a copy of the cisco.ios project. All development of the new collection
  is planned to take place in this branch (as if it were the new main).
- Compiled a list of modules suitable for adaptation to Eltex.
- Added an important development task: implement getting facts.

### List of modules that can be adapted for Eltex (series 23xx/33xx/53xx/63xx/75xx)

High applicability (expected to be adaptable):

- `ios_hostname` - hostname is supported.
- `ios_interfaces` - basic L2/L3 interface attributes are supported (shutdown, description, speed/duplex/mtu -
  model-dependent).
- `ios_l2_interfaces` - switchport mode access/trunk, allowed VLANs - supported.
- `ios_vlans` - create/delete VLAN, name - supported.
- `ios_l3_interfaces` - SVI (interface vlan) and IP on routed ports - supported on L3 models.
- `ios_static_routes` - static routing - supported on L3 models.
- `ios_acl_interfaces` - applying ACL to an interface - supported (ACL in/out).
- `ios_acls` - standard/extended ACLs - supported, but syntax may differ (translation needed).
- `ios_prefix_lists` - prefix-lists are typically available (for routing/policy) - supported on L3 models.
- `ios_route_maps` - route-map (policy routing/redistribution) - present on L3 models, syntax differences expected.
- `ios_ntp_global` - NTP server, source-interface - usually available.
- `ios_logging_global` - syslog/logging host, facility/level - available.
- `ios_lldp_global` - LLDP enable/global options - available.
- `ios_lldp_interfaces` - LLDP on interfaces - available.
- `ios_snmp_server` - SNMP communities/users, traps - available.
- `ios_system` - basic system parameters (hostname, domain-name, clock) - partially overlap; usable.
- `ios_banner` - MOTD/exec banners - typically supported.
- `ios_user` - local users/passwords/privilege - supported.
- `ios_ping` - device-originated ping - available.
- `ios_command` - run commands - universal.
- `ios_config` - push configuration fragments - universal.

Conditionally applicable/depends on model and firmware (requires thorough verification):

- `ios_hsrp_interfaces` - HSRP is not present on many MES; VRRP is often used instead. If you need FHRP, adapting to
  VRRP is more likely (requires a different module/logic).
- `ios_lacp` - LACP (802.3ad) is usually supported, but global parameters may differ.
- `ios_lacp_interfaces` - configuring LAG membership and active/passive modes - generally available, but syntax and
  terms (channel-group/lag) differ.
- `ios_lag_interfaces` - aggregations (Port-Channel/LAG) - supported, but translation to Eltex CLI is needed.
- `ios_vrf` / `ios_vrf_global` / `ios_vrf_address_family` / `ios_vrf_interfaces` - VRF exists on L3 models/lines with IP
  Advanced; feature set and commands differ. Realistically adaptable, but verify per series.
- `ios_ospfv2` / `ios_ospf_interfaces` - OSPFv2 is supported on L3 models with the appropriate license/firmware.
- `ios_ospfv3` - IPv6 OSPF support depends on model and software version; often available on high-end MES.
- `ios_bgp_global` / `ios_bgp_address_family` - BGP is not on all MES; more common on higher-end models (MES53xx/75xx)
  and certain software versions. Adaptation is possible but highly model-dependent.
- `ios_evpn_global` / `ios_evpn_evi` / `ios_evpn_ethernet` - сan be adapted based on documentation, but is challenging
  and highly model/firmware-dependent.
- `ios_vxlan_vtep` - сan be adapted based on documentation, but is challenging and rarely supported on MES.

Low applicability/typically not supported on MES:

- `ios_service` - IOS-specific service toggles/options (service timestamps, pad, etc.) may partially exist, but overlap
  is small; benefit is questionable.## Old description

## Old description (files in ./archive/)

Playbooks for automating routine administration tasks of Eltex switches.
(mes2100, mes2300, mes3300, mes3500, mes5300 series.)

Modules ios_command and ios_config are suitable (almost) for work with Eltex switches. I made two changes to the
modules:

/usr/lib/python3/dist-packages/ansible_collections/cisco/ios/plugins/cliconf/ios.py
self.send_command("configure terminal") // "configure terminal" -> "configure"

/usr/lib/python3/dist-packages/ansible_collections/cisco/ios/plugins/terminal/ios.py
self._exec_cli_command(b"terminal lenght 0") // "terminal lenght 0" -> "terminal datadump"

This made it possible to use modules for Eltex.

mes-upgrade.yml - playbook for downloading new firmware images;
mes-schedule.yml - playbook for restarting switches on a schedule;
*.textfsm - templates for parsing.
