# Functions

Notes for Part 13 of the course. Code first, short explanations, nothing extra.

---

## 1. Defining and Calling a Function

**A function is a named block of code you write once and run whenever you call it.**

```python
def greet():
    print("Hello, welcome to Python")

greet()
greet()
```

```
Hello, welcome to Python
Hello, welcome to Python
```

| Part | Meaning |
|---|---|
| `def` | keyword that starts a function |
| `greet` | function name |
| `()` | where parameters go |
| `:` and indent | the body of the function |
| `greet()` | calling (running) the function |

Defining a function does nothing on its own. The code runs only when you **call** it.

**Q → Write a function `line()` that prints `----------`. Call it 2 times.**

```python
def line():
    print("----------")

line()
line()
```

```
----------
----------
```

---

## 2. Parameters and Arguments

**Parameters are the names in the definition. Arguments are the actual values you pass when calling.**

```python
def greet(name):          # name is a parameter
    print("Hello", name)

greet("Vivek")            # "Vivek" is an argument
greet("Virat")
```

```
Hello Vivek
Hello Virat
```

Pass the wrong number of arguments and Python stops:

```python
greet()
```

```
TypeError: greet() missing 1 required positional argument: 'name'
```

**Q → Write `add(a, b)` that prints the sum. Call it with `5, 3`.**

```python
def add(a, b):
    print(a + b)

add(5, 3)
```

```
8
```

---

## 3. `return`

**`return` sends a value back to the caller so you can store or use it. `print` only shows it on screen.**

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
print(add(10, 20) * 2)
```

```
8
60
```

### `print` vs `return`

```python
def show(a, b):
    print(a + b)

x = show(2, 3)
print(x)
```

```
5
None
```

A function with no `return` gives back `None`.

### Code after `return` never runs

```python
def test():
    return "done"
    print("never printed")

print(test())
```

```
done
```

### Returning multiple values

```python
def calc(a, b):
    return a + b, a - b

s, d = calc(10, 4)
print(s, d)
print(calc(10, 4))
```

```
14 6
(14, 6)
```

Multiple values come back as a **tuple**, and you can unpack them.

**Q → Write `is_even(n)` that returns `True` if `n` is even, else `False`.**

```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(7))
```

```
True
False
```

---

## 4. Positional and Keyword Arguments

**Positional: matched by order. Keyword: matched by name, so order does not matter.**

```python
def intro(name, age):
    print(f"{name} is {age} years old")

intro("Vivek", 25)              # positional
intro(age=25, name="Vivek")     # keyword
intro(25, "Vivek")              # positional in wrong order
```

```
Vivek is 25 years old
Vivek is 25 years old
25 is Vivek years old
```

The last line shows why order matters for positional arguments.

### Mixing both

Positional must come **before** keyword:

```python
intro("Vivek", age=25)      # works
intro(name="Vivek", 25)     # error
```

```
SyntaxError: positional argument follows keyword argument
```

**Q → Call `intro` using keyword arguments with age first.**

```python
intro(age=30, name="Virat")
```

```
Virat is 30 years old
```

---

## 5. Default Arguments

**Give a parameter a default value. If the caller skips it, the default is used.**

```python
def greet(name, msg="Good morning"):
    print(msg, name)

greet("Vivek")
greet("Vivek", "Good night")
```

```
Good morning Vivek
Good night Vivek
```

Default parameters must come **after** non-default ones:

```python
def greet(msg="Hi", name):    # error
    pass
```

```
SyntaxError: parameter without a default follows parameter with a default
```

> **Common mistake:** never use a list as a default (`def f(items=[])`). The same list is shared between calls and keeps growing. Use `items=None` and create the list inside.

**Q → Write `power(base, exp=2)`. Call it with `power(5)` and `power(2, 3)`.**

```python
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, 3))
```

```
25
8
```

---

## 6. `*args`

**`*args` accepts any number of positional arguments and collects them into a tuple.**

```python
def total(*args):
    print(args)
    print(type(args))
    return sum(args)

print(total(1, 2, 3))
print(total(10, 20))
```

```
(1, 2, 3)
<class 'tuple'>
6
(10, 20)
<class 'tuple'>
30
```

The name `args` is just a convention. The `*` is what matters.

**Q → Write `find_max(*nums)` that returns the largest number without using `max()`.**

```python
def find_max(*nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest

print(find_max(4, 9, 2, 7))
```

```
9
```

---

## 7. `**kwargs`

**`**kwargs` accepts any number of keyword arguments and collects them into a dictionary.**

```python
def profile(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, "=", v)

profile(name="Vivek", age=25, city="Mumbai")
```

```
{'name': 'Vivek', 'age': 25, 'city': 'Mumbai'}
name = Vivek
age = 25
city = Mumbai
```

### Order when using everything together

```python
def f(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)

f(1, 2, 3, 4, x=5, y=6)
```

```
1 2 (3, 4) {'x': 5, 'y': 6}
```

| Order | Type |
|---|---|
| 1 | normal parameters |
| 2 | default parameters |
| 3 | `*args` |
| 4 | `**kwargs` |

**Q → Write `bill(**items)` that takes item prices as keyword arguments and returns the total.**

```python
def bill(**items):
    return sum(items.values())

print(bill(pen=10, book=50, bag=300))
```

```
360
```

---

## 8. Recursion Basics

**Recursion is when a function calls itself. Every recursive function needs a base case to stop.**

| Part | Job |
|---|---|
| Base case | the condition where the function stops calling itself |
| Recursive case | the function calls itself with a smaller problem |

### Factorial

`5! = 5 * 4 * 3 * 2 * 1 = 120`

```python
def factorial(n):
    if n == 1:              # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))
```

```
120
```

How it runs:

```
factorial(5) = 5 * factorial(4)
             = 5 * 4 * factorial(3)
             = 5 * 4 * 3 * factorial(2)
             = 5 * 4 * 3 * 2 * factorial(1)
             = 5 * 4 * 3 * 2 * 1
             = 120
```

Without a base case the function never stops:

```
RecursionError: maximum recursion depth exceeded
```

**Q → Write a recursive function `sum_n(n)` that returns `1 + 2 + ... + n`.**

```python
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))
```

```
15
```

---

## Quick Recap

- **`def name():`** defines a function. **`name()`** runs it.
- **Parameters** are in the definition. **Arguments** are the values you pass.
- **`return`** sends a value back. No `return` means the function gives `None`.
- **Multiple return values** come back as a tuple.
- **Positional** arguments match by order, **keyword** arguments match by name. Positional comes first.
- **Default arguments** go after non-default ones. Never use a list as a default.
- **`*args`** collects extra positional arguments into a **tuple**.
- **`**kwargs`** collects extra keyword arguments into a **dict**.
- **Order:** normal, default, `*args`, `**kwargs`.
- **Recursion** needs a base case, or you get `RecursionError`.

---

## Interview Questions

**1. What is the difference between `print` and `return`?**

`print` shows a value on screen. `return` sends the value back to the caller so it can be stored or used. A function without `return` gives `None`.

**2. What is the difference between `*args` and `**kwargs`?**

`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary.

**3. What is the output?**

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))
```

```
[1]
[1, 2]
```

The default list is created once, when the function is defined, and shared by every call. The fix:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

**4. Write a recursive function to find the nth Fibonacci number.**

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(7))
```

```
13
```

Series: `0, 1, 1, 2, 3, 5, 8, 13`. `fib(7)` is the 8th value, counting from `fib(0)`.

**5. Reverse a string using recursion.**

```python
def reverse(s):
    if s == "":
        return s
    return reverse(s[1:]) + s[0]

print(reverse("python"))
```

```
nohtyp
```
