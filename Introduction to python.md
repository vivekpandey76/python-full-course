# Introduction to Python

Notes for Part 1 of the course. Theory kept short and practical — only what you actually need to know.

---

## 1. What is Python?

Python is a **high-level, general-purpose programming language** used to build software and automate tasks.

- **High-level** → the code is written in a way that is close to plain English, so it is easy for humans to read and write. You don't manage memory, pointers, or CPU registers yourself.
- **General-purpose** → not tied to one field. The same language works for websites, data, AI, testing, and scripts.
- **Simple, readable syntax** → this is the main reason Python is easy to learn. Fewer symbols, fewer rules, less boilerplate.

Created by Guido van Rossum, first released in 1991. The version used today is **Python 3**.

---

## 2. Why Learn Python?

Python is used across many areas:

| Area | What Python is used for |
|---|---|
| Web development | Building websites and web apps (Django, Flask) |
| Backend development | Server-side logic and APIs (FastAPI) |
| Automation & scripting | Automating repetitive daily tasks |
| Data analysis | Cleaning and analysing data (Pandas, NumPy) |
| Data engineering | Building data pipelines |
| AI & Machine Learning | Models and deep learning (scikit-learn, PyTorch) |
| Web scraping | Pulling data from websites (BeautifulSoup, Selenium) |
| Testing | Automated test scripts (PyTest, Selenium) |

**Must know:** one language, many career paths. That is why it is usually the first language recommended.

---

## 3. Python Installation

1. Go to <https://www.python.org/downloads/>
2. Download the latest Python 3 version for your OS.
3. On Windows, tick **"Add Python to PATH"** during installation. This step is easy to miss and causes most "python is not recognized" errors.
4. Verify in the terminal:

```bash
python --version      # Windows
python3 --version     # macOS / Linux
```

If a version number prints, Python is installed correctly.

---

## 4. VS Code Installation

VS Code is the **editor** (where you write code). Python is the **language** (what runs the code). You need both.

1. Download from <https://code.visualstudio.com/>
2. Install it.
3. Open the **Extensions** panel and install the **Python** extension by Microsoft.
4. Select your interpreter: `Ctrl + Shift + P` / `Cmd + Shift + P` → *Python: Select Interpreter* → pick the Python you installed.

---

## 5. Running Your First Python Program

Create a file ending in `.py`, for example `Part_1.py`:

```python
print("Hello Welcome to my channel")
```

Run it:

```bash
python Part_1.py      # Windows
python3 Part_1.py     # macOS / Linux
```

Or press the **Run** (▶) button in VS Code.

`print()` is a built-in function that displays whatever you put inside the brackets on the screen.

---

## 6. Comments

Comments are notes for humans. Python **ignores** them completely when running the code.

### Single-line comment — `#`

```python
# Adding two numbers and storing in result
a = 12
b = 13
result = a + b
# print(result)
```

Shortcut to comment/uncomment a line: **`Ctrl + /`** (Windows) or **`Cmd + /`** (macOS).

### Multi-line comment block — `'''` or `"""`

```python
'''
    This is my comment block
    this is vivek pandey
'''
```

**Why comments matter:** they explain *why* the code does something. Code shows *what* happens; comments explain the reason. Also useful to temporarily disable a line while testing.

---

## 7. How Python Works Internally

This is the part most beginners skip, but it explains a lot of Python's behaviour.

### The flow

```
Python Code (.py)
      ↓
Python Compiler
      ↓
Bytecode (.pyc)
      ↓
PVM  (Python Virtual Machine)
      ↓
Machine-level execution
      ↓
CPU
```

### What each step does

| Step | What happens |
|---|---|
| **Python Code** | The `.py` file you wrote — plain, human-readable text. |
| **Python Compiler** | Converts your source code into **bytecode**. It also catches syntax errors here, before anything runs. |
| **Bytecode** | A low-level, platform-independent set of instructions. Not machine code, not readable Python. Cached in a `__pycache__` folder as `.pyc` files so the same file doesn't get recompiled every time. |
| **PVM (Python Virtual Machine)** | The engine that **understands and executes the bytecode**, one instruction at a time. This is the actual "interpreter" part of Python. |
| **Machine-level execution** | The PVM translates each bytecode instruction into operations the machine can perform. |
| **CPU** | Executes the machine instructions produced by the PVM and returns the result. |

### Things worth remembering

- **Python is both compiled and interpreted.** Compiled to bytecode, then interpreted by the PVM. So the common line "Python is an interpreted language" is only half the story.
- **You never compile manually.** Unlike C or Java, this happens automatically every time you run the file.
- **Bytecode is portable, the PVM is not.** The same `.pyc` runs anywhere, but each OS needs its own Python installation. This is what makes Python platform-independent.
- **This extra layer costs speed.** Python is slower than C because of the PVM step in the middle. In return you get readability and speed of development.
- **CPython** is the standard implementation (written in C) — that's what you get from python.org. Other implementations exist: PyPy (faster), Jython (runs on the JVM), IronPython (.NET).

### See the bytecode yourself

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

This prints the actual bytecode instructions the PVM will run. Useful once, just to make the concept concrete.

---

## Quick Recap

- Python is high-level, general-purpose, and readable.
- It is used in web, backend, automation, data, AI, scraping, and testing.
- Install Python first, then VS Code, then the Python extension.
- `print()` displays output; `#` and `'''...'''` create comments.
- Your code is compiled to bytecode, and the PVM runs that bytecode on the CPU.
