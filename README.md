# P01-01 — Command-line Calculator

A Python CLI calculator supporting `+`, `-`, `*`, `/`, `//`, `%`, `**`, parentheses and unary signs. Uses a restricted Python AST parser rather than `eval()`.

## Setup

```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
python -m pip install -e ".[dev]"
```

## Run

```bash
python -m calculator "(2 + 3) * 4"
python -m calculator
```

In interactive mode, type `quit` to exit.

## Test and lint

```bash
python -m pytest
python -m ruff check .
```

## Learning goals

- Functions, modules, packages, and type hints
- Command-line argument parsing and REPL input
- AST parsing and allowlisting safe arithmetic
- Exceptions, validation, and unit tests

## Limitations

This is a learning project, not a symbolic math engine. Expressions are capped at 200 characters, recursion depth at 25, and exponent size is limited. Floating-point operations use Python's normal precision.
