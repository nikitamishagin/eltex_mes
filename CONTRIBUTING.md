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

## 🔖 License

By participating, you accept the terms of the project license.
