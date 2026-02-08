==================================
Eltex MES Collection Release Notes
==================================

.. contents:: Topics

v0.1.0
======

Minor Changes
-------------

- Refactor `mes_config` module for Eltex MES support (https://github.com/nikitamishagin/eltex_mes/pull/29)
- [Adaptation]: Command module (https://github.com/nikitamishagin/eltex_mes/pull/25)

v0.0.1
======

Release Summary
---------------

This is the zeroth version of the Cisco IOS package adaptation for Eltex MES devices. It contains the minimum necessary changes for working with the MES command-line interface.

Major Changes
-------------

- Cliconf and terminal plugins updated for MES CLI detection and command execution.
- Galaxy metadata adjusted to reflect the new collection name and platform.
- Plugins, modules, argspecs, facts, config handlers, rm_templates migrated to `mes/*`.

Minor Changes
-------------

- Added repository templates (issues, PR) and contributor docs tailored for MES.
- Updated unit tests and fixtures to MES equivalents to maintain coverage.

Documentation Changes
---------------------

- Documentation restructured under `docs/nikitamishagin.eltex_mes.*`.
- Updated README and CONTRIBUTING to reflect MES usage and development workflow.
