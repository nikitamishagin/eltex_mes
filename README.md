# Eltex MES Collection

**PROJECT UNDER DEVELOPMENT**

🚀 Join the effort to build a dedicated Eltex Ansible collection!

If you work with Eltex network devices and are familiar with Ansible/Python, I invite you to contribute. The plan is a
phased adaptation of modules from the cisco.ios collection for Eltex devices. Please propose and implement your
Eltex-specific adaptations following the roadmap below.

I’m happy to receive any suggestions, ideas, and support for creating this collection. Thank you!

⚠️ **If you need a quick way** to make a cisco.ios module work with Eltex devices (just to get it working), check out
[this section](#old-description-files-in-archive). This is how my project started and how I adapted the module for
my needs.

## Common plan for improvement

- [x] Fork the Ansible cisco.ios collection
- [x] Create a list of modules that can be adapted for Eltex
- [ ] Polish the repository
    - [x] Improve the README
    - [x] Add the contribution page
    - [x] Add Pull Request and Issue templates
    - [x] Fix pre-commit hooks
    - [x] Fix import paths
    - [ ] Adapt GitHub Actions workflows
    - [ ] Add the support page
- [x] Define the order of the most important modules
- [ ] Adapt the main modules to get a minimally functional collection
    - [ ] Adapt cliconf module
    - [ ] Adapt terminal module
- [ ] Adapt facts modules
- [ ] Adapt high-priority modules
    - [ ] Adapt command module
    - [ ] Adapt config module
    - [ ] Adapt hostname module
    - [ ] Adapt vlans module
    - [ ] Adapt interfaces module
    - [ ] Adapt l2_interfaces module
    - [ ] Adapt l3_interfaces module
    - [ ] Adapt ping module
    - [ ] Adapt banner module
    - [ ] Adapt static_routes module
    - [ ] Adapt user module
    - [ ] Adapt system module
- [ ] Adapt less-important modules
    - [ ] Adapt prefix_lists module
    - [ ] Adapt route_maps module
    - [ ] Adapt acls module
    - [ ] Adapt acl_interfaces module
    - [ ] Adapt lldp_global module
    - [ ] Adapt lldp_interfaces module
    - [ ] Adapt lacp module
    - [ ] Adapt lacp_interfaces module
    - [ ] Adapt lag_interfaces module
    - [ ] Adapt snmp_server module
    - [ ] Adapt ntp_global module
    - [ ] Adapt logging_global module
- [ ] Create useful Ansible roles
- [ ] Prepare useful use cases with Ansible playbooks
- [ ] Try to adapt the remaining modules

Ansible Cisco IOS Collection: https://github.com/ansible-collections/cisco.ios

## Progress of improvement

- The improvement plan has been drafted and added to the README.
- A brief section for contributors has been added.
- A new branch has been created to evolve the project into an Ansible collection. The branch is named
  `feature/ansible-collection`. It is currently a copy of the cisco.ios project. All development of the new collection
  is planned to take place in this branch (as if it were the new main).
- Compiled a list of modules suitable for adaptation to Eltex.
- Added an important development task: implement getting facts.
- Merged the `feature/ansible-collection` branch into `main` to preserve the original cisco.ios project history and
  incorporate it into this project.
- Improved the part of the README that covers legacy solutions.
- Improved the contribution section.
- Added templates for issues and pull requests.
- Fixed pre-commit hooks and documentation generation.
- Fixed all import paths in modules and tests.
- Defined the order of the most important modules.
- Updated project improvement plan.

### List of modules that can be adapted for Eltex (series 23xx/33xx/53xx/54xx)

Facts are an important Ansible mechanism. It definitely needs to be adapted. However, this module has a lot of
dependencies and requires parsing multiple outputs from different devices. Therefore, adapting it can take a relatively
long time.

- `ios_facts` - collects facts from devices.

I believe these modules should be adapted first. They cover the basic functionality of network switches. They also adapt
well from iOS to MES.

- `ios_command` - run commands - supported.
- `ios_config` - push configuration fragments - supported.
- `ios_hostname` - set up hostname - supported.
- `ios_vlans` - create, delete VLAN - supported.
- `ios_interfaces` - basic L2/L3 interface attributes - supported.
- `ios_l2_interfaces` - switchport mode access/trunk, allowed VLANs - supported.
- `ios_l3_interfaces` - SVI (interface vlan) and IP on routed ports - supported on L3 models.
- `ios_ping` - device-originated ping - supported.
- `ios_banner` - add banner - supported.
- `ios_static_routes` - static routing - supported on L3 models.
- `ios_user` - local users/passwords/privilege - supported.
- `ios_system` - basic system parameters (hostname, domain-name, clock) - supported.

The following modules can be adapted, but I consider them less of a priority. They are supported by many models.

- `ios_prefix_lists` - prefix-lists - supported on L3 models.
- `ios_route_maps` - route-map - supported on L3 models.
- `ios_acls` - standard/extended ACLs - supported.
- `ios_acl_interfaces` - applying ACL to an interface - supported.
- `ios_lldp_global` - global LLDP parameters - supported.
- `ios_lldp_interfaces` - LLDP on interfaces - supported.
- `ios_lacp` - interface aggregation (802.3ad) - supported.
- `ios_lacp_interfaces` - configuring LAG membership and active/passive modes - supported.
- `ios_lag_interfaces` - aggregations (Port-Channel/LAG) - depends on model.
- `ios_snmp_server` - SNMP communities/users, traps - supported.
- `ios_ntp_global` - NTP server, source-interface - supported.
- `ios_logging_global` - syslog/logging host, facility/level - supported.

The modules below appear to be the least important. They implement specific and unpopular functionality. They are
difficult to adapt, and some require a complete rewrite. Furthermore, they are difficult to test at the initial stage of
a project. Therefore, their adaptation should be done last.

`ios_service` - manages specific functions.
`ios_evpn_evi`- can be adapted based on documentation, but is challenging and rarely supported on MES.
`ios_evpn_global` - can be adapted based on documentation, but is challenging and rarely supported on MES.
`ios_evpn_ethernet`  - can be adapted based on documentation, but is challenging and rarely supported on MES.
`ios_hsrp_interfaces` - HSRP is not present on many MES; VRRP is often used instead.
`ios_ospfv2` - OSPF is support depends on model and software version.
`ios_ospfv3` - OSPF is support depends on model and software version.
`ios_ospf_interfaces` - OSPF is support depends on model and software version.
`ios_bgp_global` - BGP is not on all MES; more common on higher-end models (MES5xxx) and certain software versions.
`ios_bgp_address_family` - BGP is not on all MES; more common on higher-end models.
`ios_vrf` - VRF is not on all MES; more common on higher-end models.
`ios_vrf_global` - VRF is not on all MES; more common on higher-end models.
`ios_vrf_interfaces` - VRF is not on all MES; more common on higher-end models.
`ios_vrf_address_family` - VRF is not on all MES; more common on higher-end models.
`ios_vxlan_vtep` - can be adapted based on documentation, but is challenging and rarely supported on MES.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against the following Ansible versions: **>=2.16.0**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

## Included content

<!--start collection content-->
### Cliconf plugins
Name | Description
--- | ---
[nikitamishagin.eltex_mes.mes](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_cliconf.rst)|Use mes cliconf to run commands on Eltex MES platform

### Modules
Name | Description
--- | ---
[nikitamishagin.eltex_mes.ios_acl_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_acl_interfaces_module.rst)|Resource module to configure ACL interfaces.
[nikitamishagin.eltex_mes.ios_acls](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_acls_module.rst)|Resource module to configure ACLs.
[nikitamishagin.eltex_mes.ios_banner](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_banner_module.rst)|Module to configure multiline banners.
[nikitamishagin.eltex_mes.ios_bgp_address_family](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_bgp_address_family_module.rst)|Resource module to configure BGP Address family.
[nikitamishagin.eltex_mes.ios_bgp_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_bgp_global_module.rst)|Resource module to configure BGP.
[nikitamishagin.eltex_mes.ios_command](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_command_module.rst)|Module to run commands on remote devices.
[nikitamishagin.eltex_mes.ios_config](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_config_module.rst)|Module to manage configuration sections.
[nikitamishagin.eltex_mes.ios_evpn_ethernet](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_evpn_ethernet_module.rst)|Resource module to configure L2VPN EVPN Ethernet Segment.
[nikitamishagin.eltex_mes.ios_evpn_evi](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_evpn_evi_module.rst)|Resource module to configure L2VPN EVPN EVI.
[nikitamishagin.eltex_mes.ios_evpn_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_evpn_global_module.rst)|Resource module to configure L2VPN EVPN.
[nikitamishagin.eltex_mes.ios_facts](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_facts_module.rst)|Module to collect facts from remote devices.
[nikitamishagin.eltex_mes.ios_hostname](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_hostname_module.rst)|Resource module to configure hostname.
[nikitamishagin.eltex_mes.ios_hsrp_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_hsrp_interfaces_module.rst)|Resource module to configure HSRP on interfaces.
[nikitamishagin.eltex_mes.ios_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_interfaces_module.rst)|Resource module to configure interfaces.
[nikitamishagin.eltex_mes.ios_l2_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_l2_interfaces_module.rst)|Resource module to configure L2 interfaces.
[nikitamishagin.eltex_mes.ios_l3_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_l3_interfaces_module.rst)|Resource module to configure L3 interfaces.
[nikitamishagin.eltex_mes.ios_lacp](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_lacp_module.rst)|Resource module to configure LACP.
[nikitamishagin.eltex_mes.ios_lacp_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_lacp_interfaces_module.rst)|Resource module to configure LACP interfaces.
[nikitamishagin.eltex_mes.ios_lag_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_lag_interfaces_module.rst)|Resource module to configure LAG interfaces.
[nikitamishagin.eltex_mes.ios_lldp_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_lldp_global_module.rst)|Resource module to configure LLDP.
[nikitamishagin.eltex_mes.ios_lldp_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_lldp_interfaces_module.rst)|Resource module to configure LLDP interfaces.
[nikitamishagin.eltex_mes.ios_logging_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_logging_global_module.rst)|Resource module to configure logging.
[nikitamishagin.eltex_mes.ios_ntp_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_ntp_global_module.rst)|Resource module to configure NTP.
[nikitamishagin.eltex_mes.ios_ospf_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_ospf_interfaces_module.rst)|Resource module to configure OSPF interfaces.
[nikitamishagin.eltex_mes.ios_ospfv2](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_ospfv2_module.rst)|Resource module to configure OSPFv2.
[nikitamishagin.eltex_mes.ios_ospfv3](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_ospfv3_module.rst)|Resource module to configure OSPFv3.
[nikitamishagin.eltex_mes.ios_ping](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_ping_module.rst)|Tests reachability using ping from IOS switch.
[nikitamishagin.eltex_mes.ios_prefix_lists](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_prefix_lists_module.rst)|Resource module to configure prefix lists.
[nikitamishagin.eltex_mes.ios_route_maps](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_route_maps_module.rst)|Resource module to configure route maps.
[nikitamishagin.eltex_mes.ios_service](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_service_module.rst)|Resource module to configure service.
[nikitamishagin.eltex_mes.ios_snmp_server](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_snmp_server_module.rst)|Resource module to configure snmp server.
[nikitamishagin.eltex_mes.ios_static_routes](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_static_routes_module.rst)|Resource module to configure static routes.
[nikitamishagin.eltex_mes.ios_system](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_system_module.rst)|Module to manage the system attributes.
[nikitamishagin.eltex_mes.ios_user](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_user_module.rst)|Module to manage the aggregates of local users.
[nikitamishagin.eltex_mes.ios_vrf](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_vrf_module.rst)|Module to configure VRF definitions.
[nikitamishagin.eltex_mes.ios_vrf_address_family](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_vrf_address_family_module.rst)|Resource module to configure VRF definitions.
[nikitamishagin.eltex_mes.ios_vrf_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_vrf_global_module.rst)|Resource module to configure global VRF definitions.
[nikitamishagin.eltex_mes.ios_vrf_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_vrf_interfaces_module.rst)|Manages VRF configuration on interfaces.
[nikitamishagin.eltex_mes.ios_vxlan_vtep](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.ios_vxlan_vtep_module.rst)|Resource module to configure VXLAN VTEP interface.
[nikitamishagin.eltex_mes.mes_vlans](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_vlans_module.rst)|Resource module to configure VLANs.

<!--end collection content-->

## Old description (files in ./archive/)

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
