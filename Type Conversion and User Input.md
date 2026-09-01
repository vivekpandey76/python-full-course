# Type Conversion & User Input

Notes for Part 3 of the course. Simple explanations, real examples, nothing extra.

---

## 1. What is Type Conversion?

**Type conversion means changing a value from one data type to another.**

Think of it like changing the packaging, not the contents. The number twenty-five can be packed as text `"25"` or as a number `25`. It looks the same to you, but Python treats them very differently.

```python
x = "10"        # this is a string (text)
x = int(x)      # now it is an integer (number)

print(x)          # 10
print(type(x))    # <class 'int'>
```

### Why do we need it?

Because Python will not do maths on text.

```python
print("10" + 5)     # TypeError — cannot add a string and an int
print(10 + 5)       # 15  ✅
```

The output `10` and `"10"` look identical on screen. The difference is only in the **type**, and the type decides what you are allowed to do with the value.

```python
print("10" + "20")   # 1020   ← joins the text together
print(10 + 20)       # 30     ← adds the numbers
```

Same-looking values, completely different result. This one example is the reason type conversion exists.

### Two kinds of conversion

| Kind | Who does it | Example |
|---|---|---|
| **Implicit** | Python does it automatically | `10 + 2.5` → `12.5` |
| **Explicit** | You do it yourself with `int()`, `float()`, `str()`, `bool()` | `int("10")` → `10` |

```python
# Implicit — Python promotes the int to a float on its own
result = 10 + 2.5
print(result, type(result))    # 12.5 <class 'float'>
```

Python only converts automatically when it is safe (int → float). It will **never** guess that `"10"` should become a number. That part is your job — and that is called **explicit conversion** or **type casting**.

---

## 2. `int()` — convert to a whole number

```python
x = "25"
x = int(x)

print(x)          # 25
print(type(x))    # <class 'int'>
```

### What `int()` accepts

```python
print(int("25"))      # 25    ← string of digits
print(int(25.9))      # 25    ← float (decimal part is cut off)
print(int(True))      # 1
print(int(False))     # 0
```

**Important:** `int()` on a float **does not round** — it chops off everything after the decimal point.

```python
print(int(25.9))      # 25   (not 26!)
print(int(-25.9))     # -25
print(round(25.9))    # 26   ← use round() if you actually want rounding
```

### What `int()` refuses

```python
int("hello")     # ValueError: invalid literal for int()
int("25.5")      # ValueError — a string with a dot is not an int string
int("")          # ValueError
```

The string must contain a **clean whole number** and nothing else. If you have the string `"25.5"`, go through `float()` first:

```python
print(int(float("25.5")))    # 25  ✅
```

---

## 3. `float()` — convert to a decimal number

```python
x = "25.5"
x = float(x)

print(x)          # 25.5
print(type(x))    # <class 'float'>
```

```python
print(float("25.5"))    # 25.5
print(float("25"))      # 25.0   ← .0 gets added
print(float(25))        # 25.0
print(float(True))      # 1.0
```

`float()` is more forgiving than `int()` — it accepts both `"25"` and `"25.5"`. But it still refuses nonsense:

```python
float("vivek")     # ValueError
```

> **Handy rule:** if you are not sure whether the user will type `50` or `50.5`, use `float()`. It handles both.

---

## 4. `str()` — convert to text

```python
z = 10
print(z, type(z))         # 10 <class 'int'>

z = str(z)
print(z, type(z))         # 10 <class 'str'>
```

Notice the printed value looks exactly the same — only the type changed.

`str()` never fails. Anything can become text.

```python
print(str(100))       # "100"
print(str(19.8))      # "19.8"
print(str(True))      # "True"
print(str(None))      # "None"
```

### Where you actually need it

When you join a number into a sentence with `+`:

```python
age = 25

print("My age is " + age)         # ❌ TypeError
print("My age is " + str(age))    # ✅ My age is 25
```

Or just let `print()` handle it with a comma — no conversion needed:

```python
print("My age is", age)           # ✅ My age is 25
```

---

## 5. `bool()` — convert to `True` or `False`

`bool()` answers one question: **"is there something here, or is it empty/zero?"**

```python
print(bool(1))      # True
print(bool(0))      # False
print(bool(100))    # True
print(bool("v"))    # True
print(bool(""))     # False
```

### The rule

**Empty or zero → `False`. Everything else → `True`.**

| Value | `bool()` | Why |
|---|---|---|
| `0`, `0.0` | `False` | zero |
| `""` | `False` | empty string |
| `[]`, `{}`, `()` | `False` | empty collection |
| `None` | `False` | no value |
| `1`, `-5`, `100` | `True` | not zero |
| `"v"`, `"hello"` | `True` | not empty |
| `"0"`, `"False"` | `True` | ⚠️ **not empty** — it is text! |

The last row catches everyone:

```python
print(bool(0))        # False
print(bool("0"))      # True   ← "0" is a string with one character in it
print(bool("False"))  # True   ← same reason
```

The values that give `False` are called **falsy**; everything else is **truthy**. You will use this a lot later with `if` statements.

---

## 6. `input()` — taking input from the user

`input()` stops the program, waits for the user to type something and press Enter, and gives you back what they typed.

```python
name = input("Enter your name: ")

print(name)          # Vivek
print(type(name))    # <class 'str'>
```

The text inside `input(...)` is the **prompt** — the message shown to the user. It is optional but always worth writing.

### The one rule you must never forget

> **`input()` ALWAYS returns a string.** Always. No exceptions.

Even if the user types `25`, you get the string `"25"`, not the number `25`.

```python
age = input("Enter your age: ")     # user types: 25

print(age)          # 25
print(type(age))    # <class 'str'>   ← string, not int!
print(age + 5)      # ❌ TypeError
```

This single fact is behind almost every beginner error with input.

---

## 7. Taking Integer Input

Wrap `input()` inside `int()`:

```python
age = int(input("Enter your age: "))

print(age)          # 25
print(type(age))    # <class 'int'>
print(age + 5)      # 30  ✅
```

### How to read `int(input(...))`

Read it **from the inside out**:

```
int(  input("Enter your age: ")  )
      └── 1. ask the user → "25" (string)
 └───────── 2. convert it   →  25  (int)
```

Two steps in one line. You can also write it as two lines — exactly the same thing:

```python
age = input("Enter your age: ")   # "25"
age = int(age)                    # 25
```

---

## 8. Taking Float Input

Same idea, with `float()`:

```python
salary = float(input("Enter your salary: "))

print(salary)          # 19000.5
print(type(salary))    # <class 'float'>
```

Use `float()` for anything that can have a decimal — salary, height, weight, price, marks, temperature.

---

## 9. Taking Multiple Inputs with `split()`

Sometimes you want two values from one line. `split()` breaks a string into a **list of pieces**, cutting at every space.

```python
print("Vivek Delhi".split())    # ['Vivek', 'Delhi']
```

Then you assign those pieces to two variables at once — this is called **unpacking** (you saw it in Part 2):

```python
name, city = input("Enter your name and city: ").split()

print(name)    # Vivek
print(city)    # Delhi
```

User types: `Vivek Delhi`

### Step by step

```
input()   →  "Vivek Delhi"              (one string)
.split()  →  ['Vivek', 'Delhi']         (list of 2 strings)
name, city = ...  →  name="Vivek", city="Delhi"
```

### The count must match

```python
name, city = input().split()
```

| User types | Result |
|---|---|
| `Vivek Delhi` | ✅ works |
| `Vivek` | ❌ `ValueError: not enough values to unpack` |
| `Vivek Kumar Delhi` | ❌ `ValueError: too many values to unpack` |

Two variables means the user must type **exactly two** words.

### Splitting on a comma

By default `split()` cuts at spaces. Pass a separator to cut somewhere else:

```python
# User types: Vivek,Delhi
name, city = input("Enter name,city: ").split(",")
print(name, city)    # Vivek Delhi
```

> These pieces are still **strings**. `split()` splits — it does not convert.

---

## 10. Multiple Integer Inputs with `map()`

`split()` gives you strings. To turn all of them into numbers, use `map()`.

`map(function, iterable)` applies a function to **every item** in a list.

```python
a, b = map(int, input("Enter two numbers: ").split())

print(a + b)    # user types "10 20" → 30
```

### Step by step

```
input()      →  "10 20"                 (one string)
.split()     →  ['10', '20']            (list of STRINGS)
map(int, …)  →  10, 20                  (int applied to each item)
a, b = …     →  a=10, b=20              (both are real ints)
```

Without `map()`:

```python
a, b = input("Enter two numbers: ").split()
print(a + b)      # "1020"  ❌ joined the text, did not add
```

With `map()`:

```python
a, b = map(int, input("Enter two numbers: ").split())
print(a + b)      # 30  ✅
```

### The long way vs the short way

Both do the same job — pick whichever is clearer to you:

```python
# Long way — two separate questions
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(a + b)

# Short way — one line, one question
a, b = map(int, input("Enter 2 numbers: ").split())
print(a + b)
```

`map(float, ...)` works the same way for decimals.

---

## 11. Common Input Mistakes

### Mistake 1 — Forgetting the conversion

```python
age = input("Enter your age: ")
print(age + 5)          # ❌ TypeError: can only concatenate str
```

**Fix:**

```python
age = int(input("Enter your age: "))
print(age + 5)          # ✅ 30
```

### Mistake 2 — Invalid conversion

```python
int("hello")     # ❌ ValueError
int("25.5")      # ❌ ValueError — has a dot
float("vivek")   # ❌ ValueError
```

The string must contain a **valid number**. `int()` needs a whole number; `float()` accepts a decimal too.

### Mistake 3 — Assuming `input()` returns a number

```python
age = input("Enter your age: ")     # user types 25
```

Even though the user typed `25`, `age` holds the **string** `"25"`. It looks like a number when printed, which is exactly why the mistake is so easy to make. Always check with `type()` if you are unsure.

### Mistake 4 — Misplaced brackets

```python
age = int(input("Enter your age: "))     # ✅ correct
age = int(input("Enter your age: ")      # ❌ SyntaxError — one bracket missing
```

Count them: `int(` and `input(` are two open brackets, so you need **two closing brackets** `))` at the end.

### Two error types, one table

| Error | Meaning | Typical cause |
|---|---|---|
| `TypeError` | Wrong type for this operation | `"25" + 5` — forgot to convert |
| `ValueError` | Right type, impossible value | `int("hello")` — not a number |

---

## Full Working Example (`script.py`)

```python
# Type Conversion & User Input

# --- Explicit conversion ---
x = "10"
x = int(x)
print(x, type(x))              # 10 <class 'int'>

y = float("100")
print(y, type(y))              # 100.0 <class 'float'>

z = 10
z = str(z)
print(z, type(z))              # 10 <class 'str'>

print(bool(100))               # True
print(bool(0))                 # False


# --- Taking input ---
name = input("Enter your name: ")
print(name, type(name))                    # str

age = int(input("Enter your age: "))
print(age + 5)                             # works, it's an int now

salary = float(input("Enter your salary: "))
print(salary, type(salary))                # float


# --- Multiple inputs ---
name, age = input("Enter your name and age: ").split()
print(name, type(name), age, type(age))    # both are strings

a, b = map(int, input("Enter 2 numbers: ").split())
print(a, type(a), b, type(b))              # both are ints
print(a + b)
```

Run it:

```bash
python script.py      # Windows
python3 script.py     # macOS / Linux
```

---

# Practice Questions

## Practice 1

Take two numbers from the user and print their addition, subtraction, multiplication and division.

```python
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

**Sample run** — user enters `10` and `4`:

```
Addition: 14
Subtraction: 6
Multiplication: 40
Division: 2.5
```

**Two things to notice:**

1. `int()` is essential. Without it, `a + b` would give `104` instead of `14`.
2. `/` always returns a **float**, even for `10 / 5` → `2.0`. That is normal in Python 3.

> Try dividing by `0` and you get `ZeroDivisionError`. Handling that comes later with `if` statements.

## Practice 2

Take the user's name, age and height. Convert age to `int` and height to `float`. Print each value with its data type.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("name:", name, type(name))
print("age:", age, type(age))
print("height:", height, type(height))
```

**Sample run** — user enters `Vivek`, `25`, `5.9`:

```
name: Vivek <class 'str'>
age: 25 <class 'int'>
height: 5.9 <class 'float'>
```

**Why each type was chosen:**

| Value | Type | Reason |
|---|---|---|
| name | `str` | Text — no conversion needed, `input()` already gives a string |
| age | `int` | Age is a whole number |
| height | `float` | Height has a decimal part |

---

## Quick Recap

- **Type conversion** changes a value from one type to another. `"10"` and `10` look identical but behave completely differently.
- **Implicit** conversion is automatic (`10 + 2.5` → `12.5`). **Explicit** conversion is yours to do: `int()`, `float()`, `str()`, `bool()`.
- `int()` → whole number. Chops off decimals (`int(25.9)` → `25`), and refuses `"hello"` or `"25.5"`.
- `float()` → decimal number. Accepts both `"25"` and `"25.5"`.
- `str()` → text. Never fails. Needed when joining a number into a sentence with `+`.
- `bool()` → empty or zero is `False`, everything else is `True`. Careful: `bool("0")` is `True`.
- **`input()` always returns a string** — this is the most important line in this part.
- Convert as you take input: `int(input(...))`, `float(input(...))`. Read it inside out.
- `split()` breaks one line into a list of strings, then unpack it: `name, city = input().split()`. The number of words must match the number of variables.
- `map(int, ...)` converts every piece at once: `a, b = map(int, input().split())`.
- `TypeError` → wrong type for the operation. `ValueError` → right type, impossible value.
