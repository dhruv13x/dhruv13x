<div align="center">
  <img src="https://raw.githubusercontent.com/dhruv13x/dhruv13x/main/dhruv13x_logo.png" alt="dhruv13x logo" width="200"/>
</div>

<div align="center">

<!-- Package Info -->
[![PyPI version](https://img.shields.io/pypi/v/dhruv13x.svg)](https://pypi.org/project/dhruv13x/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
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

<!-- Docs -->
[![Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://your-docs-link)

</div>


# ✨ dhruv13x: The Unified Developer Toolchain

**Elevator Pitch:** A meta-package that installs and manages a suite of essential Python developer utilities, providing a single, unified command-line interface.

## 📖 About

Why install and manage a dozen different developer tools when you can have one? `dhruv13x` is a "batteries-included" toolkit that bundles a curated set of high-quality utilities into a single, easy-to-use CLI. It's designed to streamline your workflow, enforce best practices, and automate common development tasks.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher

### Installation
```bash
pip install dhruv13x
```

### Usage Example
Get a list of all available commands:
```bash
dhruv13x --help
```

See the suite of installed tools:
```bash
dhruv13x tools
```

Check the version of the meta-package:
```bash
dhruv13x version
```

---

## ✨ Key Features

- **Tool Agnostic:** Access a suite of standalone tools through a single, consistent interface.
- **God Level: One-Command Cleanup:** Run `dhruv13x purge` to intelligently remove clutter like `.pyc` files, `__pycache__` directories, and other temporary files from your project.
- **Atomic Project Snapshots:** Use `dhruv13x clone` to create a complete, timestamped snapshot of your project, perfect for backups or testing.
- **Project Restoration:** Use `dhruv13x restore` to restore your project from a snapshot created by `dhruv13x clone`.
- **Duplicate Code Detection:** The `dhruv13x dedupe` command runs `duplifinder` to identify and report duplicate code blocks.
- **Transparent Subprocess Execution:** `dhruv13x` acts as a wrapper, calling the underlying tools in a subprocess to ensure clean and isolated execution.

---

## ⚙️ Configuration & Advanced Usage

### CLI Commands

| Command    | Description                                       |
|------------|---------------------------------------------------|
| `tools`    | List all installed meta tools.                    |
| `version`  | Show the unified version info.                    |
| `purge`    | Run the `pypurge` cleanup tool.                   |
| `clone`    | Run the `projectclone` CLI to snapshot a project. |
| `restore`  | Run the `projectrestore` CLI to restore from snapshot. |
| `dedupe`   | Run the `duplifinder` tool to find duplicate code.|

> **Note:** For commands that act as wrappers (like `dedupe`), you can pass additional arguments directly to the underlying tool. For example, `dhruv13x dedupe --arg1 value` is equivalent to `duplifinder --arg1 value`.

### Environment Variables
This tool does not require any specific environment variables for its operation.

---

## 🏗️ Architecture

### Directory Structure
```
src/
└── dhruv13x/
    ├── __init__.py
    ├── banner.py   # ASCII art for the CLI
    └── cli.py      # Main Typer application and command definitions
```

### Core Logic
The application is built using [Typer](https://typer.tiangolo.com/), which provides a simple and intuitive way to create a command-line interface. The main entry point is the `app` object in `cli.py`. Each command is a separate function decorated with `@app.command()`. These functions then use the `subprocess` module to call the underlying tools, passing any additional arguments directly to them.

---

## 🗺️ Roadmap

- [x] Initial release with core functionality
- [x] Add `restore` command
- [ ] Add `import_fix` command
- [ ] Add `init` command
- [ ] Add `routine` command
- [ ] Add `docs` command

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

