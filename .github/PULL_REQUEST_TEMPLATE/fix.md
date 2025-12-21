**Suggested title:** `[Fix]: <short explanation>`

**Before submitting:** please fill out all required sections.

### What was fixed?

**Required:** short explanation of what changed and why (1–3 sentences).

### Testing / Verification

Optional: how you verified the fix or reproduced the issue. Include exact commands/playbooks and device context.

```sh
# Fill this in with your real context/results.
# Environment: <device/model> (FW <version>), Ansible <version>, Python <version>
# Repro/verify steps:
#   ansible-playbook <playbook>.yml -i <inventory> -l <host-or-group>
# Expected vs actual CLI/output:
#   <command>
#   <command>
```

### Checklist

- [ ] No behavior change except the fix
- [ ] Linted (ansible-lint/flake8) and basic tests pass
- [ ] Playbook/examples run without errors on target device(s)
- [ ] Docs/README updated if behavior or usage changed
