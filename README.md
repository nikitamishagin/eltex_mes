# Eltex MES Collection

[![CI](https://github.com/nikitamishagin/eltex_mes/actions/workflows/tests.yml/badge.svg?branch=main&event=schedule)](https://github.com/nikitamishagin/eltex_mes/actions/workflows/tests.yml) [![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/nikitamishagin/eltex_mes?sort=semver)](https://github.com/nikitamishagin/eltex_mes/releases)

Ansible collection to help automate the management of Eltex MES network devices.

**The collection is under development but can already be used to perform some tasks.**

🚀 Join the effort to build a dedicated Eltex Ansible collection!

If you work with Eltex network devices and are familiar with Ansible/Python, I invite you to contribute. The plan is a
phased adaptation of modules from the cisco.ios collection for Eltex devices. Please propose and implement your
Eltex-specific adaptations by following the plan on
the [contributing](https://github.com/nikitamishagin/eltex_mes?tab=contributing-ov-file) page.

I'm happy to receive any suggestions, ideas, and support for creating this collection. Thank you!

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
[nikitamishagin.eltex_mes.mes_acl_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_acl_interfaces_module.rst)|Resource module to configure ACL interfaces.
[nikitamishagin.eltex_mes.mes_acls](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_acls_module.rst)|Resource module to configure ACLs.
[nikitamishagin.eltex_mes.mes_banner](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_banner_module.rst)|Module to configure multiline banners.
[nikitamishagin.eltex_mes.mes_bgp_address_family](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_bgp_address_family_module.rst)|Resource module to configure BGP Address family.
[nikitamishagin.eltex_mes.mes_bgp_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_bgp_global_module.rst)|Resource module to configure BGP.
[nikitamishagin.eltex_mes.mes_command](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_command_module.rst)|Module to run commands on remote devices.
[nikitamishagin.eltex_mes.mes_config](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_config_module.rst)|Module to manage configuration sections.
[nikitamishagin.eltex_mes.mes_evpn_ethernet](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_evpn_ethernet_module.rst)|Resource module to configure L2VPN EVPN Ethernet Segment.
[nikitamishagin.eltex_mes.mes_evpn_evi](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_evpn_evi_module.rst)|Resource module to configure L2VPN EVPN EVI.
[nikitamishagin.eltex_mes.mes_evpn_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_evpn_global_module.rst)|Resource module to configure L2VPN EVPN.
[nikitamishagin.eltex_mes.mes_facts](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_facts_module.rst)|Module to collect facts from remote devices.
[nikitamishagin.eltex_mes.mes_hostname](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_hostname_module.rst)|Resource module to configure hostname.
[nikitamishagin.eltex_mes.mes_hsrp_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_hsrp_interfaces_module.rst)|Resource module to configure HSRP on interfaces.
[nikitamishagin.eltex_mes.mes_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_interfaces_module.rst)|Resource module to configure interfaces.
[nikitamishagin.eltex_mes.mes_l2_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_l2_interfaces_module.rst)|Resource module to configure L2 interfaces.
[nikitamishagin.eltex_mes.mes_l3_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_l3_interfaces_module.rst)|Resource module to configure L3 interfaces.
[nikitamishagin.eltex_mes.mes_lacp](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_lacp_module.rst)|Resource module to configure LACP.
[nikitamishagin.eltex_mes.mes_lacp_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_lacp_interfaces_module.rst)|Resource module to configure LACP interfaces.
[nikitamishagin.eltex_mes.mes_lag_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_lag_interfaces_module.rst)|Resource module to configure LAG interfaces.
[nikitamishagin.eltex_mes.mes_lldp_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_lldp_global_module.rst)|Resource module to configure LLDP.
[nikitamishagin.eltex_mes.mes_lldp_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_lldp_interfaces_module.rst)|Resource module to configure LLDP interfaces.
[nikitamishagin.eltex_mes.mes_logging_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_logging_global_module.rst)|Resource module to configure logging.
[nikitamishagin.eltex_mes.mes_ntp_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_ntp_global_module.rst)|Resource module to configure NTP.
[nikitamishagin.eltex_mes.mes_ospf_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_ospf_interfaces_module.rst)|Resource module to configure OSPF interfaces.
[nikitamishagin.eltex_mes.mes_ospfv2](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_ospfv2_module.rst)|Resource module to configure OSPFv2.
[nikitamishagin.eltex_mes.mes_ospfv3](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_ospfv3_module.rst)|Resource module to configure OSPFv3.
[nikitamishagin.eltex_mes.mes_ping](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_ping_module.rst)|Tests reachability using ping from IOS switch.
[nikitamishagin.eltex_mes.mes_prefix_lists](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_prefix_lists_module.rst)|Resource module to configure prefix lists.
[nikitamishagin.eltex_mes.mes_route_maps](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_route_maps_module.rst)|Resource module to configure route maps.
[nikitamishagin.eltex_mes.mes_service](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_service_module.rst)|Resource module to configure service.
[nikitamishagin.eltex_mes.mes_snmp_server](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_snmp_server_module.rst)|Resource module to configure snmp server.
[nikitamishagin.eltex_mes.mes_static_routes](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_static_routes_module.rst)|Resource module to configure static routes.
[nikitamishagin.eltex_mes.mes_system](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_system_module.rst)|Module to manage the system attributes.
[nikitamishagin.eltex_mes.mes_user](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_user_module.rst)|Module to manage the aggregates of local users.
[nikitamishagin.eltex_mes.mes_vlans](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_vlans_module.rst)|Resource module to configure VLANs.
[nikitamishagin.eltex_mes.mes_vrf](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_vrf_module.rst)|Module to configure VRF definitions.
[nikitamishagin.eltex_mes.mes_vrf_address_family](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_vrf_address_family_module.rst)|Resource module to configure VRF definitions.
[nikitamishagin.eltex_mes.mes_vrf_global](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_vrf_global_module.rst)|Resource module to configure global VRF definitions.
[nikitamishagin.eltex_mes.mes_vrf_interfaces](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_vrf_interfaces_module.rst)|Manages VRF configuration on interfaces.
[nikitamishagin.eltex_mes.mes_vxlan_vtep](https://github.com/nikitamishagin/eltex_mes/blob/main/docs/nikitamishagin.eltex_mes.mes_vxlan_vtep_module.rst)|Resource module to configure VXLAN VTEP interface.

<!--end collection content-->

## Installing this collection

You can install the Eltex MES collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install nikitamishagin.eltex_mes

You can also include it in a `requirements.yml` file and install it with
`ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: nikitamishagin.eltex_mes
```

## Using this collection

This collection
includes [network resource modules](https://docs.ansible.com/ansible/latest/network/user_guide/network_resource_modules.html).

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
