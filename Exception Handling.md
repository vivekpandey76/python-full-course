# Exception Handling

Notes for Part 18 of the course. Code first, short explanations, nothing extra.

An **exception** is an error that happens while the program is running. If nobody handles it, Python stops the program and prints a traceback. Exception handling lets you catch the error, show a clear message, and keep the program alive.

---

## 1. What is an Exception?

```python
int("abc")
```

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
```

```python
10 / 0
```

```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    10 / 0
ZeroDivisionError: division by zero
```

**Read a traceback from the bottom up.** The last line gives the exception name and the message. The lines above it show which file and line caused it.

Any code after the error never runs. The program has already stopped.

**Q → Run `int("abc")` and `10 / 0`. Read the traceback and identify the exception names.**

| Code | Exception | Why |
|---|---|---|
| `int("abc")` | `ValueError` | right type (a string), but `"abc"` is not a valid number |
| `10 / 0` | `ZeroDivisionError` | you cannot divide by zero |

### Common exceptions

| Exception | When | Example |
|---|---|---|
| `ValueError` | right type, wrong value | `int("abc")` |
| `TypeError` | wrong type | `"5" + 5` |
| `ZeroDivisionError` | dividing by zero | `10 / 0` |
| `NameError` | variable not defined | `print(age)` |
| `IndexError` | index out of range | `[1, 2, 3][5]` |
| `KeyError` | dictionary key missing | `{"a": 1}["b"]` |
| `AttributeError` | object has no such method | `(5).append(1)` |
| `FileNotFoundError` | file does not exist | `open("missing.txt")` |
| `ModuleNotFoundError` | module not installed | `import abcxyz` |

> `SyntaxError` and `IndentationError` happen **before** the program runs, so `try` cannot catch them. Fix the code instead.

---

## 2. `try` & `except`

```python
try:
    num = int("abc")
except ValueError:
    print("That is not a number")

print("Program continues")
```

```
That is not a number
Program continues
```

| Block | Does |
|---|---|
| `try` | code that might fail |
| `except` | runs only if that error happens inside `try` |
| `except Exception as e` | catches almost any error and stores it in `e` |

- As soon as a line in `try` fails, Python jumps straight to `except`. The rest of `try` is skipped.
- Python checks the `except` blocks **from top to bottom** and runs the first one that matches.
- So put **specific exceptions first** and `Exception` **last**. If `Exception` is first, it catches everything and the specific blocks never run.
- `type(e).__name__` gives the exception name, e.g. `ZeroDivisionError`.

**Q → Ask the user for two numbers and print `a / b`. Handle `ValueError`, `ZeroDivisionError` and anything else. Test with: 10 and 2, abc and 2, 10 and 0.**

```python
try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    print(a / b)
except ValueError:
    print("Please enter valid numbers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print("Something went wrong:", e)
```

| Input | Output |
|---|---|
| `10` and `2` | `5.0` |
| `abc` and `2` | `Please enter valid numbers` |
| `10` and `0` | `Cannot divide by zero` |

> **Common mistake:** a bare `except:` with no exception name. It also catches `Ctrl + C` (`KeyboardInterrupt`) and hides real bugs. Always name the exception, or use `except Exception`.

---

## 3. `else` & `finally`

```python
try:
    # code that might fail
except SomeError:
    # runs if that error happens
else:
    # runs only if NO error happened
finally:
    # always runs, error or not
```

| Block | Runs when |
|---|---|
| `try` | always starts |
| `except` | an error happened |
| `else` | **no** error happened |
| `finally` | **always**, error or not |

`finally` is for cleanup: closing a file, closing a database connection, printing a "done" message.

**Q → Open `cart.txt` and read it. `except FileNotFoundError` → "Cart not found". `else` → print the content. `finally` → "Program finished". Run it with and without `cart.txt`.**

```python
try:
    with open("cart.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Cart not found")
else:
    print(content)
finally:
    print("Program finished")
```

Without `cart.txt`:

```
Cart not found
Program finished
```

With `cart.txt`:

```
Milk
Bread
Eggs

Program finished
```

`except` and `else` never both run. `finally` runs both times.

---

## 4. `raise`

```python
raise ValueError("Age cannot be negative")
```

`raise` throws an exception yourself when a value is wrong, even if Python itself would accept it. The text you pass becomes the message in `e`.

**Q → Write `check_age(age)`. Raise `ValueError` if age is less than 18, otherwise print "You are eligible to vote." Call it with 15 and 20.**

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age is less than 18")
    print("You are eligible to vote.")


for age in [15, 20]:
    try:
        check_age(age)
    except ValueError as e:
        print("Error:", e)
```

```
Error: Age is less than 18
You are eligible to vote.
```

After `raise`, the rest of the function does not run, the same as `return`.

---

## 5. Custom Exceptions

```python
class OutOfStockError(Exception):
    pass
```

Make your own exception by creating a class that inherits from `Exception`. `pass` is enough. It already works like any built-in exception.

Why bother? `OutOfStockError` tells the reader exactly what went wrong. A plain `ValueError` could mean anything.

**Q → Create `OutOfStockError`. Write `place_order(stock, quantity)` that raises it with "Only 5 items left" when quantity is more than stock.**

```python
class OutOfStockError(Exception):
    pass


def place_order(stock, quantity):
    if quantity > stock:
        raise OutOfStockError(f"Only {stock} items left")
    print("Order placed")


try:
    place_order(5, 8)
except OutOfStockError as e:
    print("Error:", e)
```

```
Error: Only 5 items left
```

---

## 6. Exception Hierarchy

Catching a parent also catches all its children.

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception                <- catch this, not BaseException
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── OSError
      │    ├── FileNotFoundError
      │    └── PermissionError
      ├── ValueError
      ├── TypeError
      ├── NameError
      └── ImportError
           └── ModuleNotFoundError
```

```python
try:
    [1, 2, 3][5]
except LookupError:
    print("Index or key not found")
```

`LookupError` catches both `IndexError` and `KeyError`.

---

## 7. Where It's Used in Real Life

| Area | Example |
|---|---|
| User input | invalid number or wrong data typed in a form |
| Files | file not found, permission denied |
| APIs | request timeout, server down |
| Databases | connection failure |
| Payments | insufficient balance, payment failed |

---

## Homework: ATM Simulator

- Starting balance: ₹10,000.
- Ask the user for a withdrawal amount.
- Handle invalid number input.
- Raise `InsufficientBalanceError` if the amount is more than the balance.
- Raise `ValueError` if the amount is zero or negative.
- Use `else` to print the updated balance.
- Use `finally` to print "Thank you for using the ATM".

```python
class InsufficientBalanceError(Exception):
    pass


balance = 10000

try:
    try:
        amount = int(input("Enter withdrawal amount: "))
    except ValueError:
        raise ValueError("Please enter a valid number")

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    if amount > balance:
        raise InsufficientBalanceError(f"Insufficient balance. Available: ₹{balance}")
except ValueError as e:
    print("Error:", e)
except InsufficientBalanceError as e:
    print("Error:", e)
else:
    balance -= amount
    print("Updated balance: ₹", balance)
finally:
    print("Thank you for using the ATM")
```

| Input | Output |
|---|---|
| `500` | `Updated balance: ₹ 9500` |
| `abc` | `Error: Please enter a valid number` |
| `0` or `-50` | `Error: Amount must be greater than 0` |
| `20000` | `Error: Insufficient balance. Available: ₹10000` |

"Thank you for using the ATM" prints after every one.

- The inner `try` turns Python's message (`invalid literal for int()...`) into a clear one for the user.
- `int()` instead of `float()`: an ATM pays whole rupees, and `float("nan")` would slip past both checks.

---

## Quick Revision

- `try` → code that might fail | `except` → handle the error
- `else` → runs only if no error | `finally` → always runs
- `raise` → throw an exception yourself
- Custom exception → `class MyError(Exception): pass`
- Specific exceptions first, `Exception` last. Never a bare `except:`.
- Read a traceback from the bottom: the last line has the exception name.

---

## Interview Questions

**1. What is the difference between an error and an exception?**

A syntax error is found before the program runs, and you must fix the code. An exception happens while the program is running, and you can catch it with `try` / `except`.

**2. What is the difference between `else` and `finally`?**

`else` runs only when the `try` block had no error. `finally` always runs, error or not, so it is used for cleanup.

**3. Why should `except Exception` come last?**

Python runs the first `except` that matches. `Exception` matches almost everything, so any specific block after it would never run.

**4. Why avoid a bare `except:`?**

It catches everything, including `KeyboardInterrupt` and `SystemExit`. The user cannot stop the program with `Ctrl + C`, and real bugs get hidden.

**5. When do you use `raise`?**

When a value is valid for Python but wrong for your program, such as a negative age or a withdrawal larger than the balance.

**6. How do you create a custom exception, and why?**

Create a class that inherits from `Exception`, e.g. `class OutOfStockError(Exception): pass`. The name explains the problem better than a generic `ValueError`, and callers can catch exactly that error.

**7. Does `finally` run if there is a `return` inside `try`?**

Yes. `finally` runs before the function actually returns.
