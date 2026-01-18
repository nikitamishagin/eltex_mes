# Contributing to Eltex MES Collection

Thank you for considering contributing to this project! This document describes how you can help — whether it is
reporting bugs, writing documentation, adapting modules, or making other improvements.

## 🧰 What you can contribute

- Errors / bugs / issues on switches.
- Adaptations of existing modules for Eltex devices.
- New roles / playbooks using the collection.
- Improvements / additions to documentation (README, examples, guides).
- Tests / usage examples that will help others.
- Discussions and suggestions — issues, feature requests, feedback.

## 🙋 How to start if you don't code

Documentation, functionality checks, test cases, Eltex command outputs, ideas — everything is useful. Even simple
remarks or suggestions can help.

## 🚀 Getting Started

1. Fork the repository.
2. Create your branch — for example, `feature/adapt-vlan` or `bugfix/xxx`.
3. Make your changes.
4. Check that everything works for Eltex (if you have the opportunity to test).
5. Submit a Pull Request with a clear title and description:
   - What exactly you are changing.
   - For which Eltex models/versions.
   - Usage examples.

## 📄 Code / Style / Structure

- We try to maintain the existing style in names, comments, and module/docs documentation.
- If you add roles/playbooks for a "quick way" — please place them in `archive/`.
- When adapting existing modules — specify compatibility with Eltex models and add the outputs of commands executed on
  Eltex.

## 🧪 Testing

If possible, test changes on real (or emulated, if available) Eltex switches. However, this is not a mandatory
requirement yet.

## 📝 Issues / Feature Requests

When opening an issue:

- Specify the device model and firmware version.
- Steps to reproduce or a reproducible playbook.
- Expected behavior vs. actual behavior.

## 🔧 Enable pre-commit locally

To run the same checks locally as in CI:

1. Ensure Python is available, then install pre-commit in your **virtualenv**:

   ```bash
   python -m pip install pre-commit
   ```

2. Install the git hook scripts:

   ```bash
   pre-commit install
   ```

3. (Optional) Update hooks to the latest compatible versions:

   ```bash
   pre-commit autoupdate
   ```

4. Run all checks on the whole repo before committing:

   ```bash
   pre-commit run --all-files
   ```

Notes:

- pre-commit runs automatically on commit after step 2.
- If a hook reformats files, re-stage the changes and commit again.
- Some hooks respect ignore files like `.prettierignore`.

## Common plan for improvement

- [x] Fork the Ansible cisco.ios collection
- [x] Create a list of modules that can be adapted for Eltex
- [ ] Polish the repository
  - [x] Improve the README
  - [x] Add the contribution page
  - [x] Add Pull Request and Issue templates
  - [x] Fix pre-commit hooks
  - [x] Fix import paths
  - [x] Adapt GitHub Actions workflows
  - [ ] Add the support page
- [x] Define the order of the most important modules
- [x] Adapt the main modules to get a minimally functional collection
  - [x] Adapt cliconf module
  - [x] Adapt terminal module
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
- Cliconf module adapted.
- Terminal module adapted.
- Cliconf and terminal modules tested on real devices.
- GitHub Actions workflows updated.

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

- `ios_service` - manages specific functions.
- `ios_evpn_evi`- can be adapted based on documentation, but is challenging and rarely supported on MES.
- `ios_evpn_global` - can be adapted based on documentation, but is challenging and rarely supported on MES.
- `ios_evpn_ethernet` - can be adapted based on documentation, but is challenging and rarely supported on MES.
- `ios_hsrp_interfaces` - HSRP is not present on many MES; VRRP is often used instead.
- `ios_ospfv2` - OSPF is support depends on model and software version.
- `ios_ospfv3` - OSPF is support depends on model and software version.
- `ios_ospf_interfaces` - OSPF is support depends on model and software version.
- `ios_bgp_global` - BGP is not on all MES; more common on higher-end models (MES5xxx) and certain software versions.
- `ios_bgp_address_family` - BGP is not on all MES; more common on higher-end models.
- `ios_vrf` - VRF is not on all MES; more common on higher-end models.
- `ios_vrf_global` - VRF is not on all MES; more common on higher-end models.
- `ios_vrf_interfaces` - VRF is not on all MES; more common on higher-end models.
- `ios_vrf_address_family` - VRF is not on all MES; more common on higher-end models.
- `ios_vxlan_vtep` - can be adapted based on documentation, but is challenging and rarely supported on MES.

## 🔖 License

By participating, you accept the terms of the project license.
