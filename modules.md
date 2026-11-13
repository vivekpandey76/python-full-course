# Modules

Notes for Part 15 of the course. Code first, short explanations, nothing extra.

---

## 1. What is a Module? (Make Your Own)

**A module is a single `.py` file with reusable code (functions, classes, variables) that you can import into another file.**

| Point | Detail |
|---|---|
| Idea | write it once, import it anywhere |
| Your own module | any `.py` file, kept in the **same folder** as the file that imports it |
| Built-in modules | `math`, `random`, `datetime`, `os` and more, no install needed |
| Import by | file name **without** `.py` → `import calculator` |

**Q → Make `calculator.py` with 4 functions: `add`, `subtract`, `multiply`, `divide`. In `divide`, return `"Cannot divide by zero"` if `b` is 0. Import it in `main.py` and call each one.**

`calculator.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```

`main.py`

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
print(calculator.divide(10, 0))
```

```
15
5
50
2.0
Cannot divide by zero
```

`/` always gives a float, so `10 / 5` is `2.0`, not `2`.

### `if __name__ == "__main__":`

**Importing a file runs all of its top-level code.** So any test `print` you leave in the module also runs inside `main.py`.

**Q → Add `print(add(2, 3))` at the bottom of `calculator.py`. Run `main.py`. Why does 5 print? Fix it.**

`calculator.py` (bottom)

```python
print(add(2, 3))
```

Running `main.py`:

```
5
15
5
50
2.0
Cannot divide by zero
```

`5` prints first because `import calculator` runs the whole file once, including the test line.

Every file has a built-in variable `__name__`:

| How the file is used | Value of `__name__` |
|---|---|
| Run directly: `python calculator.py` | `"__main__"` |
| Imported: `import calculator` | `"calculator"` |

**Fix:** put test code under the check.

```python
if __name__ == "__main__":
    print(add(2, 3))
```

| Command | Prints the test `5`? |
|---|---|
| `python calculator.py` | Yes |
| `python main.py` | No |

---

## 2. Ways to Import

| Syntax | How you call it | Note |
|---|---|---|
| `import calculator` | `calculator.add(2, 3)` | clearest, name shows where it came from |
| `from calculator import add` | `add(2, 3)` | only what you need |
| `import calculator as calc` | `calc.add(2, 3)` | short name (alias) |
| `from calculator import *` | `add(2, 3)` | **avoid**, you can't tell where a name came from |

**Q → Import only `add` and `divide`. Then import the module as `calc` and call `calc.multiply(4, 3)`.**

```python
from calculator import add, divide

print(add(2, 3))
print(divide(9, 3))

import calculator as calc

print(calc.multiply(4, 3))
```

```
5
3.0
12
```

### Why avoid `import *`

If two modules have a function with the same name, the **last import wins** silently.

```python
from calculator import *
from calculator2 import *   # also has add()

print(add(10, 15))          # runs calculator2's add, not calculator's
```

With `import calculator` and `import calculator2`, you write `calculator.add()` or `calculator2.add()` and there is no confusion.

---

## 3. `math`

```python
import math
```

| Function | Does | Example | Result |
|---|---|---|---|
| `math.sqrt(x)` | square root | `math.sqrt(16)` | `4.0` |
| `math.pow(x, y)` | x to the power y | `math.pow(2, 3)` | `8.0` |
| `math.pi` | value of π | `math.pi` | `3.141592653589793` |
| `math.ceil(x)` | round **up** | `math.ceil(5.1)` | `6` |
| `math.floor(x)` | round **down** | `math.floor(5.9)` | `5` |

**Q → Pizza party: 23 people, 1 pizza feeds 4. How many pizzas to order?**

```python
import math

people = 23
per_pizza = 4

print(people / per_pizza)
print(math.ceil(people / per_pizza))
```

```
5.75
6
```

You can't order 5.75 pizzas. `ceil` rounds up so nobody stays hungry. `floor` would give 5 and 3 people get nothing.

---

## 4. `random`

```python
import random
```

| Function | Does |
|---|---|
| `random.randint(a, b)` | random whole number from `a` to `b`, **both included** |
| `random.choice(list)` | one random item |
| `random.shuffle(list)` | mixes the list **in place**, returns `None` |

Outputs below are examples. Yours will be different every run.

**Q → Login app: generate a 4-digit OTP.**

```python
import random

otp = random.randint(1000, 9999)
print(f"Your verification code is {otp}")
```

```
Your verification code is 4821
```

`randint(1000, 9999)` always gives exactly 4 digits. `randint(0, 9999)` could give `57`.

**Q → Lucky draw: pick 1 random winner.**

```python
names = ["Rahul", "Priya", "Amit", "Neha"]
print(random.choice(names))
```

```
Priya
```

**Q → Quiz app: shuffle the questions before showing them.**

```python
questions = ["What is your name?", "What is your age?",
             "What are your hobbies?", "Tell me about yourself"]

random.shuffle(questions)
print(questions)
```

```
['What are your hobbies?', 'Tell me about yourself', 'What is your name?', 'What is your age?']
```

> **Common mistake:** `questions = random.shuffle(questions)` makes `questions` equal to `None`. `shuffle` changes the list itself and returns nothing.

---

## 5. `datetime`

```python
import datetime
```

| Code | Gives |
|---|---|
| `datetime.datetime.now()` | current date and time |
| `datetime.date.today()` | today's date only |
| `.strftime("%d-%m-%Y")` | date as text in your format |
| `datetime.timedelta(days=7)` | a gap of 7 days, to add or subtract |

### Format codes for `strftime`

| Code | Meaning | Example |
|---|---|---|
| `%d` | day | `05` |
| `%m` | month (number) | `11` |
| `%Y` | year (4 digits) | `2026` |
| `%B` | month name | `November` |
| `%H:%M` | hour:minute (24h) | `14:30` |

Outputs below depend on the day you run the code.

**Q → Bill receipt: print today's date like `05-11-2026`.**

```python
import datetime

today = datetime.date.today()
print(today)
print(today.strftime("%d-%m-%Y"))
```

```
2026-11-05
05-11-2026
```

**Q → Library app: a book is issued today. Print the return date after 14 days.**

```python
import datetime

issued = datetime.date.today()
return_date = issued + datetime.timedelta(days=14)

print("Issued:", issued.strftime("%d-%m-%Y"))
print("Return by:", return_date.strftime("%d-%m-%Y"))
```

```
Issued: 05-11-2026
Return by: 19-11-2026
```

`timedelta` handles month ends for you. 25 Nov + 14 days correctly becomes 09 Dec.

---

## 6. `os`

```python
import os
```

| Function | Does |
|---|---|
| `os.getcwd()` | path of the current folder |
| `os.listdir()` | list of files and folders in the current folder |
| `os.mkdir("name")` | create a folder |
| `os.path.exists("name")` | `True` if the file or folder exists |

`os.mkdir()` on a folder that already exists crashes:

```
FileExistsError: [Errno 17] File exists: 'photos'
```

So check with `os.path.exists()` first.

**Q → Photo app: create a folder `photos` only if it does not exist yet. Then print all files in the current folder.**

```python
import os

if not os.path.exists("photos"):
    os.mkdir("photos")
    print("Folder created successfully")
else:
    print("Folder already exists")

for file_name in os.listdir():
    print(file_name)
```

First run:

```
Folder created successfully
main.py
calculator.py
photos
```

Second run:

```
Folder already exists
main.py
calculator.py
photos
```

Shortcut that does both in one line: `os.makedirs("photos", exist_ok=True)`.

---

## Quick Recap

- A **module** is a `.py` file. Import it by name without `.py`.
- Importing a module **runs its top-level code** once.
- **`if __name__ == "__main__":`** keeps test code from running on import.
- Prefer **`import module`** or **`from module import name`**. Avoid **`import *`**.
- **`math.ceil`** rounds up, **`math.floor`** rounds down.
- **`random.randint(a, b)`** includes both ends. **`shuffle`** returns `None`.
- **`timedelta(days=n)`** adds or subtracts days. **`strftime`** formats dates.
- Check **`os.path.exists()`** before **`os.mkdir()`**.

---

## Interview Questions

**1. What is the difference between a module and a package?**

A module is one `.py` file. A package is a folder of modules (usually with an `__init__.py` file). Example: `os` is a module, `os.path` is a module inside it.

**2. What does `if __name__ == "__main__":` do?**

It runs the code under it only when the file is run directly. When the file is imported, `__name__` is the module name, so the block is skipped.

**3. If you import the same module twice, does its code run twice?**

```python
import calculator
import calculator
```

No. Python runs a module only on the first import and keeps it in memory. The second import reuses it.

**4. What is the output?**

```python
import random
nums = [1, 2, 3]
print(random.shuffle(nums))
```

```
None
```

`shuffle` changes `nums` in place and returns nothing.

**5. `math.ceil(-2.5)` and `math.floor(-2.5)`?**

```python
import math
print(math.ceil(-2.5))
print(math.floor(-2.5))
```

```
-2
-3
```

Ceil goes **up** toward `+∞`, so `-2.5` → `-2`. Floor goes **down**, so `-2.5` → `-3`.

**6. You named your file `random.py` and now `random.randint` gives an error. Why?**

```
AttributeError: module 'random' has no attribute 'randint'
```

Python finds your `random.py` in the current folder before the built-in one. Never name your files after built-in modules (`random.py`, `math.py`, `os.py`). Rename it and delete the `__pycache__` folder.
