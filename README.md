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
| 10 | Sets | [Sets.md](Sets.md) |
| 11 | Dictionaries | [Dictionaries.md](Dictionaries.md) |
| 12 | Interview Questions on Collections | [Interview Questions on Collections.md](Interview%20Questions%20on%20Collections.md) |
| 13 | Functions | [Functions.md](Functions.md) |
| 14 | Scope & Lambda | [Scope and Lambda.md](Scope%20and%20Lambda.md) |
| 15 | Modules | [modules.md](modules.md) |
| 16 | Packages, pip & Virtual Environment | [Packages pip and Virtual Environment.md](Packages%20pip%20and%20Virtual%20Environment.md) |
| 17 | File Handling | [File Handling.md](File%20Handling.md) |
| 18 | Exception Handling | [Exception Handling.md](Exception%20Handling.md) |

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

### Part 10 — Sets
Creating sets, unique values and no order, why `{}` is a dict and `set()` is an empty set, no indexing, only immutable items, `add()` / `update()`, `remove()` vs `discard()`, `pop()` and `clear()`, union / intersection / difference / symmetric difference, subset and superset checks, `frozenset`, set vs list vs tuple, and five interview questions.

### Part 11 — Dictionaries
Key-value pairs, empty dict with `{}` and `dict()`, unique keys and why the last duplicate wins, which types can be keys, `[]` vs `get()` and avoiding `KeyError`, adding and changing items, merging with `update()`, `pop()` / `popitem()` / `del` / `clear()`, `keys()` / `values()` / `items()`, looping with `for k, v in d.items()`, nested dictionaries, dictionary comprehension with conditions, and five interview questions.

### Part 12 — Interview Questions on Collections
List vs tuple vs dictionary vs set and when to use which, counting character frequency, common elements between two lists, merging dictionaries and adding values, grouping words by length, anagram check, list and dictionary comprehension, set vs `frozenset`, and the Two Sum problem.

### Part 13 — Functions
Defining and calling functions, parameters vs arguments, `return` vs `print` and why a function without `return` gives `None`, returning multiple values as a tuple, positional and keyword arguments, default arguments and the mutable default trap, `*args`, `**kwargs`, the order of parameters, recursion basics with factorial and sum, and five interview questions.

### Part 14 — Scope & Lambda
Local and global scope, why assigning inside a function creates a new local, `global` and the `UnboundLocalError`, `nonlocal` for nested functions, the LEGB lookup order, lambda functions, lambda as a `sorted()` key, `map()`, `filter()`, map vs filter, and five interview questions.

### Part 15 — Modules
What a module is, making your own `calculator.py` and importing it, why importing runs top-level code and how `if __name__ == "__main__":` fixes it, the four ways to import and why to avoid `import *`, the `math` module (`sqrt`, `pow`, `ceil`, `floor`), `random` (`randint`, `choice`, `shuffle`), `datetime` (`strftime`, `timedelta`), `os` (`getcwd`, `listdir`, `mkdir`, `path.exists`), and six interview questions.

### Part 16: Packages, pip & Virtual Environment
Module vs package vs library, making a `shop` package with `__init__.py`, why `__init__.py` code runs on import, the ways to import from a package, installing and removing packages with `pip`, `pip list` / `pip show`, saving and restoring with `pip freeze > requirements.txt` and `pip install -r`, why each project needs its own virtual environment, creating and activating a `venv` on macOS / Linux / Windows, keeping `venv/` out of Git, and six interview questions.

### Part 17: File Handling
Why files keep data after the program stops, `open()` and the `"r"` / `"w"` / `"a"` modes, why `"w"` erases old content, always using `with` so the file closes itself, `write()` and adding `\n` yourself, `read()` / `readline()` / `readlines()` and looping line by line, `strip()`, saving and loading JSON with `json.dump()` and `json.load()`, the load → change → dump update pattern, real-life uses (uploads, logs, ETL, reports), and six interview questions.

### Part 18: Exception Handling
What an exception is and how to read a traceback, the common exceptions (`ValueError`, `TypeError`, `ZeroDivisionError`, `KeyError` and more), `try` / `except` and why specific exceptions go before `Exception`, why to avoid a bare `except:`, `else` and `finally` and when each one runs, raising your own errors with `raise`, custom exceptions like `OutOfStockError`, the exception hierarchy, real-life uses, an ATM simulator homework, and seven interview questions.

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
| `Sets.md` | Part 10 notes |
| `Dictionaries.md` | Part 11 notes |
| `Interview Questions on Collections.md` | Part 12 notes |
| `Functions.md` | Part 13 notes |
| `Scope and Lambda.md` | Part 14 notes |
| `modules.md` | Part 15 notes |
| `Packages pip and Virtual Environment.md` | Part 16 notes |
| `File Handling.md` | Part 17 notes |
| `Exception Handling.md` | Part 18 notes |
| `main.py` | Working practice code for the current part |
| `shop/` | Example package used in Part 16 (`billing.py`, `discount.py`) |
| `requirements.txt` | Packages for this project, install with `pip install -r requirements.txt` |
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
python main.py        # Windows
python3 main.py       # macOS / Linux
```

Or press the **Run** (▶) button in VS Code.

---

## How to Use These Notes

1. Read the markdown file for the part you are on.
2. Type the examples yourself in `main.py` — do not copy-paste. Typing is how it sticks.
3. Do the **Practice Questions** at the end of each file before moving on.
4. Use the **Quick Recap** section to revise later.

---

## Requirements

- Python 3.x
- Any code editor (VS Code recommended)
- Parts 1 to 15 need no external libraries
- From Part 16 on, create a virtual environment and run `pip install -r requirements.txt`
