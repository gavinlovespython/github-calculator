# Multi Language Calculator Project

This project started as a simple calculator, but it has grown into a small
multi language playground with Python, C, organized modules, utilities,
and a clean folder structure. The goal is to keep everything simple and
easy to understand while still feeling like a real project.

The calculator now supports:
- basic math operations
- advanced operations like power and square root
- simple statistics
- a C version of the calculator
- reusable input and formatting helpers
- a clean operations folder with multiple modules

Everything is written to be readable and beginner friendly.

---

## Project Structure
project/ │ ├── calculator.py ├── calculator.c ├── CHANGELOG.md │ ├── operations/ │   ├── init.py │   ├── basic.py │   ├── advanced.py │   └── statistics.py │ └── utils/ ├── formatting.py └── input_helpers.py

---

## Python Version

The Python calculator includes:
- a menu system
- input validation
- formatted output
- basic, advanced, and statistics modes
- clean separation of logic into modules

Run it with:
python3 calculator.py

---

## C Version

The C version is a simpler version of the calculator that includes:
- basic operations
- advanced operations
- a simple menu

Compile it with:
gcc calculator.c -o calculator -lm
Then run:
./calculator
---

## Operations

### Basic
- add
- subtract
- multiply
- divide

### Advanced
- power
- square root
- absolute value

### Statistics
- mean
- median
- minimum
- maximum

---

## Utilities

The utils folder contains helper functions that keep the main code clean.

### formatting.py
Handles:
- result formatting
- operation descriptions

### input_helpers.py
Handles:
- number input
- integer input
- menu choices
- yes or no prompts
- range validation
- general input utilities

---

## Purpose

This project is mainly for experimenting, learning, and building a clean
and organized codebase across multiple languages. It is not meant to be
complex. It is meant to be fun to expand and easy to maintain.

---

## License

This project uses the MIT License.
