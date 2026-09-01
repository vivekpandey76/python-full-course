# Python Course

Beginner-friendly Python notes and practice code. Every part has one markdown file with the theory and examples, written in plain language so anyone can follow along without prior programming experience.

---

## Contents

| Part | Topic | Notes |
|---|---|---|
| 1 | Introduction to Python | [Introduction to python.md](Introduction%20to%20python.md) |
| 2 | Variables & Data Types | [Variables and Data Types.md](Variables%20and%20Data%20Types.md) |
| 3 | Type Conversion & User Input | [Type Conversion and User Input.md](Type%20Conversion%20and%20User%20Input.md) |

### Part 1 — Introduction to Python
What Python is, why it is worth learning, installing Python and VS Code, running your first program, comments, and how Python works internally (bytecode and the PVM).

### Part 2 — Variables & Data Types
Variables, assignment, naming rules, dynamic typing, the core data types (`int`, `float`, `bool`, `str`, `None`), checking types with `type()`, and mutable vs immutable objects.

### Part 3 — Type Conversion & User Input
Implicit vs explicit conversion, `int()`, `float()`, `str()`, `bool()`, truthy and falsy values, taking input with `input()`, converting input to numbers, multiple inputs with `split()` and `map()`, and the common `TypeError` / `ValueError` mistakes.

---

## Files in this repo

| File | What it is |
|---|---|
| `Introduction to python.md` | Part 1 notes |
| `Variables and Data Types.md` | Part 2 notes |
| `Type Conversion and User Input.md` | Part 3 notes |
| `script.py` | Working practice code for the current part |
| `notes.txt` | Raw rough notes taken while learning |

---

## Getting Started

### 1. Install Python

Download Python 3 from <https://www.python.org/downloads/>.
On Windows, tick **"Add Python to PATH"** during installation.

Check that it worked:

```bash
python --version      # Windows
python3 --version     # macOS / Linux
```

### 2. Install VS Code

Download from <https://code.visualstudio.com/>, then install the **Python** extension by Microsoft.

Select your interpreter: `Ctrl + Shift + P` / `Cmd + Shift + P` → *Python: Select Interpreter*.

### 3. Run the code

```bash
python script.py      # Windows
python3 script.py     # macOS / Linux
```

Or press the **Run** (▶) button in VS Code.

---

## How to Use These Notes

1. Read the markdown file for the part you are on.
2. Type the examples yourself in `script.py` — do not copy-paste. Typing is how it sticks.
3. Do the **Practice Questions** at the end of each file before moving on.
4. Use the **Quick Recap** section to revise later.

---

## Requirements

- Python 3.x
- Any code editor (VS Code recommended)
- No external libraries needed
