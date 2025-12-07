<div align="center">
  <img src="https://raw.githubusercontent.com/dhruv13x/dhruv13x/main/dhruv13x_logo.png" alt="dhruv13x logo" width="200"/>
</div>

<div align="center">

<!-- Package Info -->
[![PyPI version](https://img.shields.io/pypi/v/dhruv13x.svg)](https://pypi.org/project/dhruv13x/)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Python Versions](https://img.shields.io/pypi/pyversions/dhruv13x.svg)](https://pypi.org/project/dhruv13x/)
![Wheel](https://img.shields.io/pypi/wheel/dhruv13x.svg)
[![Release](https://img.shields.io/badge/release-PyPI-blue)](https://pypi.org/project/dhruv13x/)

<!-- Build & Quality -->
[![Build status](https://github.com/dhruv13x/dhruv13x/actions/workflows/publish.yml/badge.svg)](https://github.com/dhruv13x/dhruv13x/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/dhruv13x/dhruv13x/graph/badge.svg)](https://codecov.io/gh/dhruv13x/dhruv13x)
[![Test Coverage](https://img.shields.io/badge/coverage-95%25%2B-brightgreen.svg)](https://github.com/dhruv13x/dhruv13x/actions/workflows/test.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/linting-ruff-yellow.svg)](https://github.com/astral-sh/ruff)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

<!-- Usage -->
![Downloads](https://img.shields.io/pypi/dm/dhruv13x.svg)
[![PyPI Downloads](https://img.shields.io/pypi/dm/dhruv13x.svg)](https://pypistats.org/packages/dhruv13x)
![OS](https://img.shields.io/badge/os-Linux%20%7C%20macOS%20%7C%20Windows-blue.svg)

<!-- License -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

# ✨ dhruv13x: The Unified Developer Toolchain

**Elevator Pitch:** The "Swiss Army Knife" for modern Python engineering—a meta-package that installs and unifies a suite of essential developer utilities under a single, consistent CLI. Stop juggling dozen tools; install `dhruv13x` and get a "batteries-included" workflow for cleanup, backups, documentation, and code hygiene.

---

## ⚡ Quick Start

### Prerequisites
- Python **3.11** or higher.
- Basic familiarity with CLI tools.

### Installation
Install the meta-suite with a single command (requires pip):

```bash
pip install dhruv13x
```

Or, for local development:
```bash
pip install .
```

### Run & Demo
Verify the installation and see the suite of installed tools in action:

```bash
# 1. Verify installation and version
dhruv13x version

# 2. List all available meta tools
dhruv13x tools

# 3. Run a safe cleanup of your project
dhruv13x purge
```

---

## ✨ Features

`dhruv13x` aggregates 10+ developer utilities into a cohesive ecosystem.

*   **Core Ecosystem**
    *   **Unified Interface**: Access all tools via the `dhruv13x` command.
    *   **Meta-Package**: Automatically installs dependencies like `duplifinder`, `pypurge`, `projectclone`, etc.
    *   **Flexible Execution**: Acts as a smart wrapper—isolating tool execution in subprocesses for stability while allowing direct argument pass-through.

*   **Maintenance & Hygiene**
    *   **Smart Cleanup (`purge`)**: Intelligently removes clutter (`__pycache__`, `.pyc`, build artifacts) to keep your workspace pristine.
    *   **Duplicate Detection (`dedupe`)**: Identify copy-pasted code blocks using `duplifinder` to reduce technical debt.

*   **Backup & Recovery**
    *   **Atomic Snapshots (`clone`)**: Create instant, timestamped backups of your entire project state.
    *   **Disaster Recovery (`restore`)**: Mistake made? Revert your project to a previous snapshot immediately.

---

## 🛠️ Configuration

### Environment Variables
`dhruv13x` is designed to work out-of-the-box, but you can customize certain behaviors.

| Variable Name | Description | Default | Required |
| :--- | :--- | :--- | :--- |
| `CREATE_DUMP_PALETTE` | Integer index (0-5) to select a fixed color palette for the banner. | Random | No |

### CLI Arguments
The `dhruv13x` CLI maps common tasks to specific underlying tools.

| Command | Description | Underlying Tool | Flags Supported |
| :--- | :--- | :--- | :--- |
| `tools` | List all installed meta tools in the suite. | *Internal* | No |
| `version` | Show the unified suite version. | *Internal* | No |
| `purge` | Clean project clutter (aggressive mode). | `pypurge` | No |
| `clone` | Create a timestamped project snapshot. | `projectclone` | No |
| `restore` | Restore project from a snapshot. | `projectrestore` | No |
| `dedupe` | Find duplicate code blocks. | `duplifinder` | Yes (Pass-through) |

> **Example of Pass-through:**
> ```bash
> # Pass arguments directly to the underlying duplifinder tool
> dhruv13x dedupe --min-lines 5 --exclude tests/
> ```

---

## 🏗️ Architecture

The project is structured as a lightweight wrapper around powerful standalone tools.

### Directory Tree

```text
src/
└── dhruv13x/
    ├── __init__.py
    ├── banner.py   # 🎨 Visuals: ASCII art and procedural color generation
    └── cli.py      # 🧠 Brain: Main Typer application & command routing
```

### Data Flow
1.  **Entry Point**: User runs `dhruv13x [COMMAND]`.
2.  **CLI Router (`cli.py`)**: `Typer` parses the command.
3.  **Execution Strategy**:
    *   **Direct Import**: Tools like `projectclone` are imported and run within the same process.
    *   **Subprocess**: Tools like `pypurge` and `duplifinder` are executed via `subprocess.run` to ensure environment isolation and capture stdout/stderr.

---

## 🐞 Troubleshooting

Common issues and how to resolve them.

| Error Message | Possible Cause | Solution |
| :--- | :--- | :--- |
| `Command not found: dhruv13x` | PATH issue or not installed. | Ensure `pip install dhruv13x` was successful and your Python scripts folder is in your PATH. |
| `FileNotFoundError: [Errno 2] No such file or directory: 'duplifinder'` | Dependency missing. | Reinstall the package: `pip install --force-reinstall dhruv13x`. |
| `ModuleNotFoundError` during dev | Virtual environment issue. | Ensure you are running within the correct virtual environment where `dhruv13x` is installed. |

**Debug Mode**:
Most commands support standard verbose flags if passed through to the underlying tool. For `dhruv13x` itself, errors are printed to stderr with clear descriptions.

---

## 🤝 Contributing

We welcome contributions! Whether it's adding a wrapper for a new tool or improving the existing CLI.

1.  **Fork** the repository.
2.  **Clone** your fork:
    ```bash
    git clone https://github.com/your-username/dhruv13x.git
    cd dhruv13x
    ```
3.  **Install for Development**:
    ```bash
    pip install -e ".[dev]"
    ```
4.  **Run Tests**:
    ```bash
    python -m pytest
    ```
5.  **Submit a Pull Request**.

See [CONTRIBUTING.md](CONTRIBUTING.md) (if available) for more detailed guidelines.

---

## 🗺️ Roadmap

Future enhancements planned for `dhruv13x`:

- [ ] **Refactoring**: `import_fix` wrapper for `import-surgeon`.
- [ ] **Scaffolding**: `init` wrapper for `pyinitgen`.
- [ ] **Workflow**: `routine` wrapper for `routine-workflow`.
- [ ] **Docs**: `docs` wrapper for `enterprise-docs` compliance.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
