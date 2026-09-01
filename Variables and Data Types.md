# Variables & Data Types

Notes for Part 2 of the course. Simple explanations, real examples, nothing extra.

---

## 1. What is a Variable?

A **variable is a name that refers to a value** in your program.

Think of it as a name tag you stick on a value so you can use that value later without typing it again.

```python
name = "Vivek"
age = 25
```

**Why we need variables:**

| Reason | Meaning |
|---|---|
| Store data | Keep a value in memory so it isn't lost |
| Reuse data | Use the same value in many places by its name |
| Modify data | Change the value while the program is running |

Without variables you would have to write the same value again and again, and you could never change it.

---

## 2. Creating Variables

In Python a variable is created the moment you **assign a value to a name**. There is no separate "declare" step.

```python
name = "Vivek"
age = 25
```

The `=` sign is the **assignment operator**. It does *not* mean "equal to" in the maths sense. Read it as **"put the value on the right into the name on the left"**.

### A variable can be reassigned

```python
x = 10
x = 20
print(x)    # 20
```

The old value is simply replaced. `x` now refers to `20`, and `10` is gone.

### Multiple variables at once

```python
# The long way
name = "Vivek"
age = 25
is_student = True

# The short way — same result
name, age, is_student = "Vivek", 25, True
print(name, age, is_student)    # Vivek 25 True
```

### Same value to many variables

```python
a = b = c = 10
print(a, b, c)    # 10 10 10
```

---

## 3. Variable Naming Rules

A variable name is called an **identifier**.

### Rules you must follow

- Can contain **letters, numbers and underscore `_`**
- **Cannot start with a number**
- **Cannot contain spaces**
- Names are **case-sensitive**
- **Cannot use Python keywords** (`class`, `if`, `for`, `True`, ...)

### Valid names

```python
student_name = "Vivek"
total_salary = 10000
first_name = "Vivek"
is_student = True
student9 = "Vivek"
```

### Invalid names

```python
9name = "Vivek"          # starts with a number
student name = "Vivek"   # contains a space
class = "Python"         # 'class' is a Python keyword
```

### Case-sensitivity in action

```python
Name = "vivek"
name = "pandey"
print(Name, name)    # vivek pandey
```

`Name` and `name` are two **completely different** variables.

**Good habit:** use `snake_case` — lowercase words joined by underscores (`total_salary`, `first_name`). That is the standard style in Python.

---

## 4. Dynamic Typing

Python is **dynamically typed**: you never declare the type of a variable, and the same variable can point to different types at different times.

```python
x = 10        # x refers to an integer
x = "Python"  # now the same x refers to a string
```

In many other languages this would be an error. In Python it is perfectly normal.

### The important idea

> In Python, the **object has a type**. The **variable is just a name** that refers to that object.

```
Object  =  actual value  +  type
```

So `10` is an object of type `int`. The name `x` is only a label pointing at it. When you write `x = "Python"`, you are not changing the type of `x` — you are pointing the same label at a **different object**.

---

## 5. What are Data Types?

A **data type** defines what kind of value an object represents.

### The core types

| Type | What it represents | Example |
|---|---|---|
| `int` | Whole numbers | `25`, `-7`, `10000` |
| `float` | Decimal numbers | `19.8`, `3.14`, `-0.5` |
| `bool` | `True` or `False` | `True`, `False` |
| `str` | Text — a sequence of characters | `"Vivek"`, `'Python'` |
| `None` | The absence of a value | `None` |

```python
age = 25              # int
salary = 19.8         # float
is_student = True     # bool
name = "Vivek"        # str
result = None         # NoneType
```

**Note on `bool`:** `True` and `False` must start with a capital letter. `true` will give an error.

**Note on `None`:** it does not mean `0` or `""`. It means "there is no value here yet".

### Other important types

- `list` — an ordered, changeable collection → `["Vivek", "Virat", "Vishal"]`
- `tuple` — an ordered, unchangeable collection → `("Vivek", "Virat")`
- `set` — unordered collection with no duplicates → `{"Vivek", "Virat"}`
- `dict` — key-value pairs → `{"name": "Vivek", "age": 25}`

These four are covered in detail later in the course.

---

## 6. Checking Data Types with `type()`

`type()` is a built-in function that tells you the type of an object.

```python
print(type(10))         # <class 'int'>
print(type(10.5))       # <class 'float'>
print(type("Python"))   # <class 'str'>
print(type(True))       # <class 'bool'>
```

It works on variables too:

```python
a = "vivek"
b = 18
c = 19.8

print(type(a))    # <class 'str'>
print(type(b))    # <class 'int'>
print(type(c))    # <class 'float'>
```

`<class 'int'>` simply means "this object belongs to the int type".

---

## 7. Mutable vs Immutable

- **Mutable** → the object **can be changed** after it is created.
- **Immutable** → the object **cannot be changed** after it is created.

| Immutable | Mutable |
|---|---|
| `int` | `list` |
| `float` | `set` |
| `bool` | `dict` |
| `str` | |
| `tuple` | |

### Mutable example — a list can be changed in place

```python
names = ["Vivek", "virat", "vishal", "vikas"]
names[0] = "Vivek Pandey"
print(names)    # ['Vivek Pandey', 'virat', 'vishal', 'vikas']
```

The list object itself was modified.

### The common confusion

```python
x = 10
x = 20
```

This looks like the value changed, but it did not. `int` is immutable — the object `10` was never modified. Python created a **new object** `20` and pointed `x` at it.

**Reassigning a variable is not the same as mutating an object.**

Mutability matters more once you work with lists, tuples, sets and dictionaries — it is covered again there.

---

## Full Working Example (`script.py`)

```python
# Variables & Data Types

name = "vivek"
age = 25

# Creating multiple variables at once
name, age, salary, is_student = "Vivek", 25, 10000, True

# Checking the data type of each value
print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(salary))       # <class 'int'>
print(type(is_student))   # <class 'bool'>

# Dynamic typing — the same name pointing to a different type
x = 10
x = "Python"
print(type(x))            # <class 'str'>
```

Run it:

```bash
python script.py      # Windows
python3 script.py     # macOS / Linux
```

---

# Practice Questions

## Practice 1

Create variables to store your name, age, salary and whether you are a student. Then print the data type of each.

```python
name, age, salary, is_student = "Vivek", 25, 10000, True

print(type(name))         # <class 'str'>
print(type(age))          # <class 'int'>
print(type(salary))       # <class 'int'>
print(type(is_student))   # <class 'bool'>
```

**Answer:** `str`, `int`, `int`, `bool`.

> If you wrote `salary = 10000.50`, the type would be `float` instead.

## Practice 2

```python
x = 10
x = "Python"
```

1. **What happens to `x`?** → It is **reassigned**. `x` stops referring to the integer `10` and starts referring to the string `"Python"`.
2. **What is the data type of `x` at the end?** → `str` (string).

---

## Quick Recap

- A variable is a **name that refers to a value**; it is created the moment you assign to it with `=`.
- Names can use letters, numbers and `_`, cannot start with a number, cannot contain spaces or keywords, and **are case-sensitive**.
- Python is **dynamically typed** — no type declaration, and a name can point to any type.
- The **object** has the type; the **variable** is only a label.
- Core types: `int`, `float`, `bool`, `str`, `None`. Collections: `list`, `tuple`, `set`, `dict`.
- `type()` tells you the type of any object.
- `int`, `float`, `bool`, `str`, `tuple` are **immutable**. `list`, `set`, `dict` are **mutable**.
- Reassigning a variable is **not** the same as changing an object.
