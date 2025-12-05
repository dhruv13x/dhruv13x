<div align="center">
  <img src="https://raw.githubusercontent.com/dhruv13x/dhruv13x/main/dhruv13x_logo.png" alt="dhruv13x logo" width="200"/>
</div>

<div align="center">

<!-- Package Info -->
[![PyPI version](https://img.shields.io/pypi/v/dhruv13x.svg)](https://pypi.org/project/dhruv13x/)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
![Wheel](https://img.shields.io/pypi/wheel/dhruv13x.svg)
[![Release](https://img.shields.io/badge/release-PyPI-blue)](https://pypi.org/project/dhruv13x/)

<!-- Build & Quality -->
[![Build status](https://github.com/dhruv13x/dhruv13x/actions/workflows/publish.yml/badge.svg)](https://github.com/dhruv13x/dhruv13x/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/dhruv13x/dhruv13x/graph/badge.svg)](https://codecov.io/gh/dhruv13x/dhruv13x)
[![Test Coverage](https://img.shields.io/badge/coverage-90%25%2B-brightgreen.svg)](https://github.com/dhruv13x/dhruv13x/actions/workflows/test.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/linting-ruff-yellow.svg)](https://github.com/astral-sh/ruff)
![Security](https://img.shields.io/badge/security-CodeQL-blue.svg)

<!-- Usage -->
![Downloads](https://img.shields.io/pypi/dm/dhruv13x.svg)
[![PyPI Downloads](https://img.shields.io/pypi/dm/dhruv13x.svg)](https://pypistats.org/packages/dhruv13x)
![OS](https://img.shields.io/badge/os-Linux%20%7C%20macOS%20%7C%20Windows-blue.svg)
[![Python Versions](https://img.shields.io/pypi/pyversions/dhruv13x.svg)](https://pypi.org/project/dhruv13x/)

<!-- License -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

# ✨ dhruv13x: The Unified Developer Toolchain

**Elevator Pitch:** The "Swiss Army Knife" for modern Python engineering—a meta-package that installs and unifies a suite of essential developer utilities under a single, consistent CLI.

## 📖 About

Why juggle a dozen different tools when you can have a unified workflow? `dhruv13x` is a **"batteries-included"** toolkit that bundles high-quality utilities for code hygiene, backups, documentation, and automation. It streamlines your development process by providing a central interface to manage these tasks, while still allowing access to each underlying tool independently.

---

## 🚀 Quick Start

### Prerequisites
- Python **3.11** or higher

### Installation
Install the meta-suite with a single command:
```bash
pip install dhruv13x
```

### Usage Example
Verify the installation and see the suite of installed tools:

```bash
# Check version
dhruv13x version

# List all installed meta tools
dhruv13x tools
```

Run a cleanup of your project:
```bash
dhruv13x purge
```

---

## ✨ Key Features

- **Unified Ecosystem:** Installs 10+ developer utilities (like `duplifinder`, `pypurge`, `projectclone`) in one go.
- **God Level: Smart Cleanup:** The `purge` command intelligently removes clutter (`__pycache__`, `.pyc`, build artifacts) to keep your workspace pristine.
- **Atomic Snapshots:** Use `clone` to create instant, timestamped backups of your entire project state.
- **Disaster Recovery:** Mistake made? Use `restore` to revert your project to a previous snapshot immediately.
- **Duplicate Detection:** Identify copy-pasted code blocks using `dedupe` (powered by `duplifinder`).
- **Flexible Execution:** Acts as a smart wrapper—isolating tool execution in subprocesses for stability while allowing direct argument pass-through.

---

## ⚙️ Configuration & Advanced Usage

### CLI Commands

The `dhruv13x` CLI maps common tasks to specific underlying tools.

| Command | Description | underlying Tool |
| :--- | :--- | :--- |
| `tools` | List all installed meta tools in the suite. | *Internal* |
| `version` | Show the unified suite version. | *Internal* |
| `purge` | Clean project clutter (aggressive mode). | `pypurge` |
| `clone` | Create a timestamped project snapshot. | `projectclone` |
| `restore` | Restore project from a snapshot. | `projectrestore` |
| `dedupe` | Find duplicate code blocks. | `duplifinder` |

> **Note:** The `dedupe` command supports argument pass-through.
> ```bash
> # Pass arguments directly to duplifinder
> dhruv13x dedupe --min-lines 5 --exclude tests/
> ```

### Environment Variables
`dhruv13x` does not require specific environment variables. However, individual tools (like `enterprise-docs` or `create-dump`) may respect their own configuration files or env vars.

---

## 🏗️ Architecture

### Directory Structure
```text
src/
└── dhruv13x/
    ├── __init__.py
    ├── banner.py   # ASCII art and branding
    └── cli.py      # Main Typer application & command routing
```

### Core Logic
The application is built on [Typer](https://typer.tiangolo.com/).
1.  **Entry Point**: `cli.py` defines the main application and commands.
2.  **Command Routing**: Each `dhruv13x` command acts as a proxy.
    *   **Direct Import**: Some tools (like `projectclone`) are imported and run directly.
    *   **Subprocess**: Others (like `pypurge`, `duplifinder`) are executed in a shell subprocess to ensure environment isolation and capture output streams.

---

## 🗺️ Roadmap

- [x] **Core**: Unified CLI structure & tool installation.
- [x] **Maintenance**: `purge` (cleanup) and `dedupe` (code quality).
- [x] **Backup**: `clone` (snapshot) and `restore` (recovery).
- [ ] **Refactoring**: `import_fix` wrapper for `import-surgeon`.
- [ ] **Scaffolding**: `init` wrapper for `pyinitgen`.
- [ ] **Workflow**: `routine` wrapper for `routine-workflow`.
- [ ] **Docs**: `docs` wrapper for `enterprise-docs`.

---

## 🤝 Contributing

We welcome contributions! Whether it's adding a wrapper for a new tool or improving the existing CLI.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes.
4.  Push to the branch.
5.  Open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**.
