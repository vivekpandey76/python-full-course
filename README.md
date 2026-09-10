# Python Course

Beginner-friendly Python notes and practice code. Every part has one markdown file with the theory and examples, written in plain language so anyone can follow along without prior programming experience.

---

## Contents

| Part | Topic | Notes |
|---|---|---|
| 1 | Introduction to Python | [Introduction to python.md](Introduction%20to%20python.md) |
| 2 | Variables & Data Types | [Variables and Data Types.md](Variables%20and%20Data%20Types.md) |
| 3 | Type Conversion & User Input | [Type Conversion and User Input.md](Type%20Conversion%20and%20User%20Input.md) |
| 4 | Operators | [Operators.md](Operators.md) |
| 5 | Conditional Statements | [Conditional Statements.md](Conditional%20Statements.md) |
| 6 | Loops | [Loops.md](Loops.md) |
| 7 | Strings | [Strings.md](Strings.md) |
| 8 | Lists | [Lists.md](Lists.md) |
| 9 | Tuples | [Tuples.md](Tuples.md) |

### Part 1 — Introduction to Python
What Python is, why it is worth learning, installing Python and VS Code, running your first program, comments, and how Python works internally (bytecode and the PVM).

### Part 2 — Variables & Data Types
Variables, assignment, naming rules, dynamic typing, the core data types (`int`, `float`, `bool`, `str`, `None`), checking types with `type()`, and mutable vs immutable objects.

### Part 3 — Type Conversion & User Input
Implicit vs explicit conversion, `int()`, `float()`, `str()`, `bool()`, truthy and falsy values, taking input with `input()`, converting input to numbers, multiple inputs with `split()` and `map()`, and the common `TypeError` / `ValueError` mistakes.

### Part 4 — Operators
Operators and operands, arithmetic operators (`+ - * / // % **`), assignment shortcuts (`+=`, `-=` and the rest), comparison operators, logical `and` / `or` / `not`, short-circuiting, and operator precedence.

### Part 5 — Conditional Statements
Indentation and blocks, `if`, `else`, `elif` chains and why order matters, nested conditions, the one-line ternary operator, and using truthy / falsy values as conditions.

### Part 6 — Loops
Why loops exist, `for` loops, `range()` and why the stop value is excluded, `while` loops and infinite loops, `for` vs `while`, nested loops and patterns, `break`, `continue`, `pass`, and the loop `else`.

### Part 7 — Strings
Quotes and multi-line strings, `len()`, indexing and negative indexing, slicing with `s[start:end:step]`, reversing with `s[::-1]`, the `+` / `*` / `in` operators, the common string methods, `split()` and `join()`, f-strings, and string immutability.

### Part 8 — Lists
Creating and accessing lists, indexing and slicing, mutability, adding elements with `append()` / `insert()` / `extend()`, removing with `remove()` / `pop()` / `del`, the common list methods, `sort()` vs `sorted()`, `reverse()`, nested lists, why `b = a` is not a copy, list comprehension, and two interview problems — second largest number and removing duplicates while keeping the order.

### Part 9 — Tuples
Creating tuples and why the comma matters more than the brackets, single item tuples, indexing and slicing, immutability and the `TypeError` it raises, the only two methods `count()` and `index()`, changing a tuple through `list()` and `tuple()`, why `sorted()` returns a list, unpacking and swapping, `*rest` unpacking, why a mutable item inside a tuple can still change, tuple vs list, and four interview questions.

---

## Files in this repo

| File | What it is |
|---|---|
| `Introduction to python.md` | Part 1 notes |
| `Variables and Data Types.md` | Part 2 notes |
| `Type Conversion and User Input.md` | Part 3 notes |
| `Operators.md` | Part 4 notes |
| `Conditional Statements.md` | Part 5 notes |
| `Loops.md` | Part 6 notes |
| `Strings.md` | Part 7 notes |
| `Lists.md` | Part 8 notes |
| `Tuples.md` | Part 9 notes |
| `script.py` | Working practice code for the current part |
| `notes.txt` | Raw rough notes for the part being recorded |

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
