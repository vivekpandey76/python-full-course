# Packages, pip & Virtual Environment

Notes for Part 16 of the course. Code first, short explanations, nothing extra.

---

## 1. What is a Package?

**A module is one `.py` file. A package is a folder of modules.**

| Term | What it is | Example |
|---|---|---|
| Module | one `.py` file | `billing.py` |
| Package | a folder of modules with an `__init__.py` | `shop/` |
| Library | a collection of packages you install | `requests`, `django` |

### `__init__.py`

- Put an `__init__.py` file inside the folder. It can be **empty**.
- It tells Python "this folder is a package".
- Any code inside it **runs once**, the first time the package is imported.

### Structure

```
python course/
├── shop/
│   ├── __init__.py
│   ├── billing.py      → calculate_total(a, b)
│   └── discount.py     → apply_discount(amount, percentage)
└── main.py
```

**Q → Make a `shop` package with `billing.py` and `discount.py`. In `main.py`, print the total of 500 + 300, then apply a 10% discount → `720.0`.**

`shop/__init__.py`

```python
print("Hello")
```

`shop/billing.py`

```python
def calculate_total(a, b):
    return a + b
```

`shop/discount.py`

```python
def apply_discount(amount, percentage):
    discount_allot = amount * percentage / 100
    return amount - discount_allot
```

`main.py` (in the folder **next to** `shop/`, not inside it)

```python
from shop import billing, discount

total = billing.calculate_total(500, 300)
print(f"Total {total}")

applied = discount.apply_discount(total, 10)
print(f"After discount price {applied}")
```

```
Hello
Total 800
After discount price 720.0
```

`Hello` prints first because importing `shop` runs `__init__.py`. Leave `__init__.py` empty unless you need setup code.

`720.0` is a float because `/` always returns a float.

### Ways to import from a package

| Syntax | How you call it |
|---|---|
| `from shop import billing` | `billing.calculate_total(100, 50)` |
| `from shop.discount import apply_discount` | `apply_discount(1000, 10)` |
| `import shop.billing` | `shop.billing.calculate_total(100, 50)` |
| `import shop.billing as bill` | `bill.calculate_total(100, 50)` |

```python
from shop.discount import apply_discount

print(apply_discount(1000, 10))
```

```
900.0
```

---

## 2. pip

**pip installs packages written by other people from PyPI (<https://pypi.org>).** It comes with Python.

| Command | Does |
|---|---|
| `pip install requests` | install a package |
| `pip install requests==2.32.3` | install a specific version |
| `pip uninstall requests` | remove a package |
| `pip list` | show installed packages |
| `pip show requests` | details of one package (version, location) |
| `pip freeze > requirements.txt` | save the project's packages and versions to a file |
| `pip install -r requirements.txt` | install everything in that file |

On macOS / Linux use `pip3` if `pip` is not found. The safest form on any system is `python -m pip install requests`, because it uses the pip of the Python you are running.

**Q → Install `requests` and check it with `pip list`.**

```bash
pip install requests
pip list
```

```
Package            Version
------------------ ---------
certifi            2026.4.22
charset-normalizer 3.4.7
idna               3.13
requests           2.34.2
urllib3            2.6.3
```

`requests` brings its own dependencies (`certifi`, `idna`, `urllib3`). pip installs them automatically. Your version numbers may differ.

Use it:

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

```
200
```

**Q → Your teammate cloned your project. Which one command installs everything?**

```bash
pip install -r requirements.txt
```

`requirements.txt` looks like this:

```
requests==2.34.2
pyjokes==0.8.3
```

One package per line, with the exact version, so everyone gets the same setup.

> **Common mistake:** running `pip freeze > requirements.txt` **outside** a venv. It dumps every package on your computer into the file, including ones this project never uses. Always freeze from inside the project's venv.

---

## 3. Virtual Environment (venv)

**Problem:** Project A needs Django 4, Project B needs Django 5. One computer, one Python. Installing one breaks the other.

**Fix:** a virtual environment is a separate box of packages for each project.

| Command | Does |
|---|---|
| `python -m venv venv` | create a venv in a folder called `venv` |
| `source venv/bin/activate` | activate (macOS / Linux) |
| `venv\Scripts\activate` | activate (Windows) |
| `deactivate` | exit the venv |

- `(venv)` at the start of the terminal line means it is active.
- While active, `pip install` puts packages **only** in this project's venv.
- Add `venv/` to `.gitignore`. Share `requirements.txt`, never the `venv` folder.
- In VS Code, pick the venv's Python: `Cmd + Shift + P` / `Ctrl + Shift + P` → *Python: Select Interpreter*.

**Q → weather-app: create a venv, activate it, install `requests`, save `requirements.txt`, then deactivate.**

macOS / Linux:

```bash
mkdir weather-app
cd weather-app

python3 -m venv venv
source venv/bin/activate

pip install requests
pip freeze > requirements.txt

deactivate
```

Windows:

```bash
mkdir weather-app
cd weather-app

python -m venv venv
venv\Scripts\activate

pip install requests
pip freeze > requirements.txt

deactivate
```

Terminal while active:

```
(venv) weather-app $ pip freeze
certifi==2026.4.22
charset-normalizer==3.4.7
idna==3.13
requests==2.34.2
urllib3==2.6.3
```

`.gitignore`

```
venv/
__pycache__/
```

Folder after:

```
weather-app/
├── venv/              ← not pushed to Git
├── .gitignore
└── requirements.txt   ← pushed to Git
```

### Teammate setup

```bash
git clone <repo-url>
cd weather-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Quick Revision

- **Module** = file | **Package** = folder | **Library** = collection of packages
- `__init__.py` marks a folder as a package and runs once on import.
- `pip install` | `pip list` | `pip freeze > requirements.txt` | `pip install -r requirements.txt`
- New project → **create venv → activate → install → freeze**
- Push `requirements.txt`, ignore `venv/`.

---

## Interview Questions

**1. What is the difference between a module, a package and a library?**

A module is one `.py` file. A package is a folder of modules with an `__init__.py`. A library is a bigger collection of packages you install, like `requests` or `django`.

**2. What is `__init__.py` for? Is it required?**

It marks a folder as a regular package and runs once when the package is imported. Since Python 3.3, a folder without it still imports (a "namespace package"), but adding it is the standard practice.

**3. Why use a virtual environment?**

So each project has its own packages and versions. Upgrading Django in one project cannot break another.

**4. Why not push the `venv` folder to Git?**

It is large, full of files built for your OS, and can be recreated in one command from `requirements.txt`.

**5. What is the difference between `pip freeze` and `pip list`?**

Both show installed packages. `pip freeze` prints them as `name==version`, ready to save into `requirements.txt`. `pip list` prints a readable table.

**6. You ran `pip install requests` but `import requests` gives `ModuleNotFoundError`. Why?**

pip installed it into a different Python than the one running your code (for example, a venv is not active, or VS Code picked another interpreter). Activate the venv, or install with `python -m pip install requests`, and check the interpreter in VS Code.
