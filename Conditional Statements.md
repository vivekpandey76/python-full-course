# Conditional Statements

Notes for Part 5 of the course. Simple explanations, real examples, nothing extra.

---

## 1. What are Conditional Statements?

**Code that runs only when a condition is True.**

Everything so far ran top to bottom, every line, every time. Conditional statements let your program **take a decision** and skip the lines that do not apply.

You already do this all day:

> "**If** it rains, take an umbrella."

- The **condition** → it is raining
- The **action** → take an umbrella

If it is not raining, you skip the umbrella. Python works exactly the same way.

```python
raining = True

if raining:
    print("Take an umbrella")
```

```
Take an umbrella
```

Change `raining` to `False` and nothing prints. The line did not fail — it was never run.

The condition is always something that ends up as `True` or `False`, which is why Part 4's comparison and logical operators matter here. `age >= 18`, `marks < 40`, `age > 18 and salary > 30000` — all of these are conditions.

---

## 2. Indentation

**Python decides what is inside a block by its spacing, not by brackets.**

Most languages use `{ }` to mark a block. Python uses **indentation** — the blank space at the start of a line.

```python
age = 20

if age >= 18:
    print("You can vote")      # indented → inside the if
print("End")                   # not indented → outside the if
```

```
You can vote
End
```

Now change `age` to `15`:

```
End
```

`"You can vote"` was skipped because it belongs to the `if`. `"End"` printed because it does not — it runs no matter what.

**The rules:**

1. The line that opens a block ends with a colon `:`
2. Every line inside the block is indented by the **same** amount
3. **4 spaces** is the standard (press Tab in VS Code)
4. Going back to the left ends the block

### The two mistakes everyone makes

**Forgetting the colon:**

```python
if age >= 18       # SyntaxError: expected ':'
    print("Adult")
```

**Forgetting to indent:**

```python
if age >= 18:
print("Adult")     # IndentationError: expected an indented block
```

Python is strict about this on purpose. The code is forced to look like what it does.

---

## 3. `if`

**Runs the block when the condition is True, skips it when False.**

```python
if condition:
    # runs only when the condition is True
```

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")

print("End")
```

**Sample run** — user enters `20`:

```
Enter your age: 20
You can vote
End
```

**Sample run** — user enters `15`:

```
Enter your age: 15
End
```

An `if` on its own has **one** exit: either the block runs or nothing happens. When you also need a "otherwise do this", you need `else`.

---

## 4. `else`

**The backup block that runs when the `if` condition is False.**

```python
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

**Sample run** — user enters `75`:

```
Pass
```

**Sample run** — user enters `32`:

```
Fail
```

`else` has **no condition** of its own — it is simply "everything the `if` did not catch". So exactly one of the two blocks always runs, never both, never neither.

```
marks >= 40 ?
├── True  → "Pass"
└── False → "Fail"
```

> `else:` takes no condition. Writing `else marks < 40:` is a `SyntaxError`.

---

## 5. `elif`

**Checks another condition, top to bottom, and stops at the first True one.**

`if`/`else` handles two outcomes. For three or more, use `elif` (short for "else if").

```python
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
```

**Sample run** — user enters `80`:

```
Grade B
```

**What Python did:**

1. `80 >= 90` → `False`, skip
2. `80 >= 75` → `True`, print `"Grade B"` and **stop**
3. The remaining `elif` and the `else` are never even checked

That last point is the whole idea: **only one block ever runs.** Once a condition matches, Python leaves the chain.

### Order matters

Because it stops at the first match, a badly ordered chain gives wrong answers:

```python
marks = 95

if marks >= 40:
    print("Grade C")       # ← this one wins, wrong!
elif marks >= 75:
    print("Grade B")
elif marks >= 90:
    print("Grade A")
```

```
Grade C
```

`95 >= 40` is true, so it stopped there. When your conditions overlap, put the **strictest one first**.

### `elif` vs many separate `if`s

```python
marks = 95

if marks >= 90:
    print("Grade A")
if marks >= 75:            # separate if → checked anyway
    print("Grade B")
if marks >= 40:
    print("Grade C")
```

```
Grade A
Grade B
Grade C
```

Three separate `if` statements are three independent questions, so all three can print. Use `elif` when the options are **alternatives** and only one should win.

---

## 6. Nested Conditions

**A condition inside another condition.**

Sometimes the second question only makes sense if the first one passed. Asking someone for their ID is pointless if they are already too young to enter.

```python
age = int(input("Enter your age: "))

if age >= 18:
    has_id = input("Do you have an ID (yes/no): ")
    if has_id == "yes":
        print("Entry allowed")
    else:
        print("Entry denied: ID required")
else:
    print("Entry denied: You must be 18 or above")
```

**Sample run** — `20`, then `yes`:

```
Entry allowed
```

**Sample run** — `20`, then `no`:

```
Entry denied: ID required
```

**Sample run** — `16`:

```
Entry denied: You must be 18 or above
```

Notice the ID question was never even asked in the last run. The inner block, including the `input()`, is inside the outer `if`.

The indentation is what shows the structure — the inner `if`/`else` is 4 spaces deeper because it lives inside the outer `if`:

```
if age >= 18:
    if has_id == "yes":  → "Entry allowed"
    else:                → "Entry denied: ID required"
else:                    → "Entry denied: You must be 18 or above"
```

> `input()` returns a string, so compare it to `"yes"` in quotes. Also, `"Yes"` and `"yes"` are different strings — `has_id.lower() == "yes"` accepts both.

**Do not over-nest.** When both conditions must be true and there is no separate message for each, `and` is cleaner:

```python
# nested
if age >= 18:
    if salary > 30000:
        print("Approved")

# better
if age >= 18 and salary > 30000:
    print("Approved")
```

Two levels deep is normal. Four levels deep usually means the logic can be rewritten.

---

## 7. Ternary Operator

**One-line `if else` that gives back a value.**

```python
value_if_true if condition else value_if_false
```

The long way:

```python
age = 20

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(status)      # Adult
```

The same thing in one line:

```python
age = 20

status = "Adult" if age >= 18 else "Minor"
print(status)      # Adult
```

Read it left to right: *"Adult", if age is 18 or above, else "Minor".*

It works inside `print()` too:

```python
n = 7
print("Even" if n % 2 == 0 else "Odd")     # Odd
```

**When to use it:** only when you are **choosing between two values**, like the two branches above. The `else` part is required — there is no one-line `if` without it.

**When not to use it:** when the branches *do* something rather than produce a value, or when there are more than two options. A regular `if`/`elif` is easier to read than a nested ternary.

---

## 8. Truthy and Falsy

**Any value can act as a condition, not just a comparison.**

You met this in Part 3 with `bool()`. It matters here because `if` accepts **any** value and quietly asks `bool()` about it.

**Falsy** — treated as `False`:

```python
0        0.0        ""        None        False
```

**Truthy** — everything else, including `"0"`, `"False"` and `-1`.

```python
name = input("Enter your name: ")

if name:
    print("Name entered")
else:
    print("Name is empty")
```

**Sample run** — user types `Vivek`:

```
Name entered
```

**Sample run** — user just presses Enter:

```
Name is empty
```

When nothing is typed, `input()` returns `""`, which is falsy, so the `else` runs. `if name:` is the normal Python way of writing "if name is not empty" — you rarely see `if name != "":`.

Same idea with numbers:

```python
balance = 0

if balance:
    print("You have money")
else:
    print("Account is empty")       # 0 is falsy
```

> Careful: `"0"` is a **string** with one character in it, so it is **truthy**. Only the empty string `""` is falsy. This is a classic bug with `input()` — always convert to `int()` before testing a number.

---

## Practice 1

Take a number and print whether it is positive, negative or zero.

```python
n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

**Sample run** — user enters `-5`:

```
Negative
```

Three outcomes, so `if` / `elif` / `else`. The `else` needs no condition — anything that is neither above nor below zero must be zero.

## Practice 2

Take a number and print whether it is even or odd.

```python
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Sample run** — user enters `8`:

```
Even
```

This is the `%` trick from Part 4, now with a decision attached. Any even number `% 2` is `0`, which also means `if n % 2:` alone would work — `0` is falsy.

## Practice 3

Take two numbers and print the larger one, handling the case where they are equal.

```python
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if a > b:
    print("1st number is larger:", a)
elif b > a:
    print("2nd number is larger:", b)
else:
    print("Both numbers are equal")
```

**Sample run** — user enters `10` and `10`:

```
Both numbers are equal
```

Guarding the equal case is the point here. With only `if`/`else`, equal numbers would wrongly print "2nd number is larger".

## Practice 4

Safe division — ask for two numbers and divide, but do not crash on zero.

```python
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if b != 0:
    print("Result:", a / b)
else:
    print("Cannot divide by zero")
```

**Sample run** — user enters `10` and `0`:

```
Cannot divide by zero
```

Part 4 ended with a `ZeroDivisionError` we could not avoid. This is the fix — check the condition **before** doing the operation.

---

## Quick Recap

- A **conditional statement** runs a block of code only when a condition is `True`.
- Python uses **indentation** (4 spaces) to decide what is inside a block, not `{ }`. The opening line always ends with a colon `:`.
- Missing colon → `SyntaxError`. Missing indent → `IndentationError`.
- **`if`** runs its block when the condition is true, and skips it otherwise.
- **`else`** runs when the `if` was false. It takes no condition of its own, so exactly one of the two blocks always runs.
- **`elif`** adds more conditions. Python checks them top to bottom and **stops at the first True one** — only one block ever runs.
- Because it stops at the first match, **order matters** in an `elif` chain. Put the strictest condition first.
- Separate `if` statements are independent questions and can all run. Use `elif` when only one option should win.
- **Nested conditions** are conditions inside conditions — use them when the inner question only makes sense after the outer one passes. Prefer `and` when there is no separate message for each case.
- The **ternary operator** — `"Adult" if age >= 18 else "Minor"` — is a one-line `if else` that returns a value. The `else` is required.
- `if` accepts **any** value, not just comparisons. `0`, `0.0`, `""`, `None` and `False` are **falsy**; everything else is **truthy**.
- `if name:` is the standard way to check that a string is not empty.
- `"0"` is a non-empty string, so it is truthy. Convert input with `int()` before testing numbers.
