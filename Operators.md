# Operators

Notes for Part 4 of the course. Simple explanations, real examples, nothing extra.

---

## 1. What are Operators?

**An operator is a symbol or keyword that performs an operation on values.**

The values it works on are called **operands**.

```python
print(10 + 5)     # 15
```

```
10  +  5
│   │  │
│   │  └── operand
│   └───── operator
└───────── operand
```

So in `10 + 5`:

- `10` and `5` are the **operands**
- `+` is the **operator**

Most operators are symbols (`+`, `-`, `==`), but a few are plain English words (`and`, `or`, `not`). Both count as operators.

### The five groups in this part

| Group | What it does | Examples |
|---|---|---|
| **Arithmetic** | Maths | `+` `-` `*` `/` `//` `%` `**` |
| **Assignment** | Store or update a value | `=` `+=` `-=` `*=` |
| **Comparison** | Compare two values → `True` / `False` | `==` `!=` `>` `<` `>=` `<=` |
| **Logical** | Combine or reverse conditions | `and` `or` `not` |
| **Precedence** | The order Python evaluates them in | `()` first, `or` last |

---

## 2. Arithmetic Operators

**Operators used to perform mathematical calculations.**

```python
a = 10
b = 3

print("addition:", a + b)          # 13
print("subtract:", a - b)          # 7
print("multiply:", a * b)          # 30
print("divide:", a / b)            # 3.3333333333333335
print("floor divide:", a // b)     # 3
print("modulus:", a % b)           # 1
print("power:", a ** b)            # 1000
```

| Operator | Name | `10` and `3` | Meaning |
|---|---|---|---|
| `+` | Addition | `13` | adds |
| `-` | Subtraction | `7` | subtracts |
| `*` | Multiplication | `30` | multiplies |
| `/` | Division | `3.333...` | normal division |
| `//` | Floor division | `3` | division, whole-number part only |
| `%` | Modulus | `1` | the remainder |
| `**` | Exponent | `1000` | power (10 × 10 × 10) |

The first three are obvious. The last four are where beginners get stuck, so take them one at a time.

### `/` always gives a float

```python
print(10 / 3)     # 3.3333333333333335
print(10 / 5)     # 2.0    ← not 2
print(type(10 / 5))   # <class 'float'>
```

Even when the division is clean, `/` returns a **float**. That is normal in Python 3.

### `//` — floor division

`//` divides two numbers and gives the **whole-number part** of the result, rounding **down**.

```python
print(10 // 3)    # 3      (3.33 → 3)
print(10 // 5)    # 2
print(9 // 2)     # 4      (4.5 → 4)
```

"Rounding down" means towards the smaller number, not towards zero. With negatives that surprises people:

```python
print(-9 // 2)    # -5     ← 4.5 rounds down to -5, not -4
```

If either operand is a float, the result is a float:

```python
print(10.0 // 3)  # 3.0
```

### `%` — modulus (remainder)

`%` gives you what is **left over** after division.

```python
print(10 % 3)     # 1      10 = (3 × 3) + 1
print(10 % 5)     # 0      divides exactly, nothing left over
print(7 % 2)      # 1
print(8 % 2)      # 0
```

`//` and `%` are a pair — one gives the answer, the other gives the leftover:

```
10 ÷ 3  →  10 // 3 = 3   (how many times 3 fits)
           10 %  3 = 1   (what is left over)
```

**The most common use of `%`:** checking if a number is even or odd.

```python
n = 8
print(n % 2)      # 0  → even
n = 7
print(n % 2)      # 1  → odd
```

Any number `% 2` is `0` for even and `1` for odd. You will use this constantly once you learn `if` statements.

### `**` — power

`**` is used to calculate a power.

```python
print(2 ** 3)     # 8      2 × 2 × 2
print(10 ** 2)    # 100
print(5 ** 0)     # 1      anything to the power 0 is 1
print(2 ** 0.5)   # 1.4142135623730951   ← square root
```

A fractional power gives you roots. `x ** 0.5` is the square root of `x`.

### Dividing by zero

```python
print(10 / 0)     # ZeroDivisionError: division by zero
print(10 // 0)    # ZeroDivisionError
print(10 % 0)     # ZeroDivisionError
```

Maths does not allow it, and neither does Python. The program stops there. Guarding against it needs `if`, which comes later.

### `+` and `*` also work on strings

```python
print("Viv" + "ek")     # Vivek     ← joins text
print("ha" * 3)         # hahaha    ← repeats text
print("10" + "20")      # 1020      ← joins, does NOT add
```

Same operator, different behaviour depending on the **type** of the operands. This is why Part 3 mattered — `"10" + "20"` is `1020`, not `30`.

The others do not work on strings at all:

```python
print("hello" - "h")    # TypeError: unsupported operand type(s)
```

---

## 3. Assignment Operators

**Operators used to assign or update values stored in variables.**

### `=` — plain assignment

```python
x = 12
```

Read it as **"put 12 into x"**, never as "x equals 12". `=` stores; `==` compares. Mixing them up is the single most common beginner bug.

### The shortcut operators

Very often you want to update a variable using its own current value:

```python
x = 12
x = x + 5     # take x, add 5, put it back into x
print(x)      # 17
```

That works, but it is long. `+=` does exactly the same thing in fewer characters:

```python
x = 12
x += 5        # same as x = x + 5
print(x)      # 17
```

```
x += 5
│  │
│  └── the amount
└───── the variable being updated in place
```

Every arithmetic operator has a matching shortcut:

| Operator | Example | Same as | Result if `x = 12` |
|---|---|---|---|
| `=` | `x = 5` | — | `5` |
| `+=` | `x += 5` | `x = x + 5` | `17` |
| `-=` | `x -= 5` | `x = x - 5` | `7` |
| `*=` | `x *= 5` | `x = x * 5` | `60` |
| `/=` | `x /= 5` | `x = x / 5` | `2.4` |
| `//=` | `x //= 5` | `x = x // 5` | `2` |
| `%=` | `x %= 5` | `x = x % 5` | `2` |
| `**=` | `x **= 5` | `x = x ** 5` | `248832` |

These are called **compound assignment** operators. There is no new logic here — just less typing.

### They run one after another

Each line updates the variable, and the next line starts from the new value:

```python
x = 12
x += 5        # x is now 17
x -= 5        # x is now 12  ← back where we started
print(x)      # 12
```

### The variable must already exist

```python
y += 5        # NameError: name 'y' is not defined
```

`y += 5` means `y = y + 5`, and Python cannot read `y` if nothing was ever put in it. Always assign with `=` first.

---

## 4. Comparison Operators

**Operators used to compare two values and produce `True` or `False`.**

Every comparison gives back a **bool** — nothing else.

```python
age = 18

print(age > 18)     # False
print(age < 18)     # False
print(age >= 18)    # True
print(age <= 18)    # True
print(age == 18)    # True
print(age != 18)    # False
```

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | equal to | `18 == 18` | `True` |
| `!=` | not equal to | `18 != 18` | `False` |
| `>` | greater than | `18 > 18` | `False` |
| `<` | less than | `18 < 18` | `False` |
| `>=` | greater than **or equal to** | `18 >= 18` | `True` |
| `<=` | less than **or equal to** | `18 <= 18` | `True` |

The difference between `>` and `>=` is exactly the boundary value. For `age = 18`, `age > 18` is `False` but `age >= 18` is `True`. When you write real conditions ("18 and above"), that one character decides whether 18 is included.

### `=` vs `==`

```python
age = 18      # assignment — stores 18 in age
age == 18     # comparison — asks "is age 18?" → True
```

| You write | It means |
|---|---|
| `=` | put this value in the variable |
| `==` | are these two the same? |

```python
if age = 18:      # ❌ SyntaxError
if age == 18:     # ✅
```

Python catches this one for you with a syntax error, which is a small mercy.

### Type matters — `19` is not `"19"`

```python
a = 19
b = "19"

print(a == b)     # False   ← int vs str
print(a != b)     # True
```

They look the same when printed, but one is a number and the other is text, so they are **not** equal. This is the Part 3 lesson showing up again.

```python
print(a == int(b))    # True   ✅ convert first, then compare
```

And ordering comparisons across those types fail outright:

```python
print(19 > "19")      # TypeError: '>' not supported between 'int' and 'str'
```

### Comparing strings

Strings compare **alphabetically** (by character code), and it is case-sensitive:

```python
print("apple" == "apple")    # True
print("apple" == "Apple")    # False  ← capital A is a different character
print("apple" < "banana")    # True   ← a comes before b
```

### Chained comparisons

Python lets you write a range the way maths does:

```python
age = 25
print(18 < age < 60)     # True
```

That reads as "age is more than 18 **and** less than 60". Most languages do not allow this; Python does.

---

## 5. Logical Operators

**Operators used to combine or reverse conditions and produce `True` or `False`.**

There are three: `and`, `or`, `not`. They are English words, not symbols.

### `and` — both must be true

```python
print(True and True)      # True
print(True and False)     # False
print(False and True)     # False
print(False and False)    # False
```

| A | B | `A and B` |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

**One `False` anywhere makes the whole thing `False`.**

### `or` — at least one must be true

```python
print(True or True)       # True
print(True or False)      # True
print(False or True)      # True
print(False or False)     # False
```

| A | B | `A or B` |
|---|---|---|
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

**One `True` anywhere makes the whole thing `True`.**

### `not` — reverses it

`not` takes one value and flips it.

```python
print(not True)      # False
print(not False)     # True
```

| A | `not A` |
|---|---|
| `True` | `False` |
| `False` | `True` |

### With real conditions

You rarely type `True and False` by hand. You combine comparisons:

```python
age = 25
salary = 50000

print(age > 18 and salary > 30000)     # True   ← both conditions hold
print(age > 30 and salary > 30000)     # False  ← first one fails
print(age > 30 or salary > 30000)      # True   ← second one is enough
print(not age > 18)                    # False  ← age > 18 is True, flipped
```

The comparisons run first, then the logical operator combines the two `True`/`False` results. Precedence handles that for you (next section) — no brackets needed.

### The easy way to remember it

| Operator | Plain English | Passes when |
|---|---|---|
| `and` | "both" | every condition is true |
| `or` | "either" | at least one condition is true |
| `not` | "opposite" | the condition is false |

### Short-circuiting

Python stops as soon as the answer is decided:

```python
print(False and 10 / 0)    # False  ← never evaluates 10 / 0
print(True or 10 / 0)      # True   ← never evaluates 10 / 0
```

With `and`, a `False` on the left settles it. With `or`, a `True` on the left settles it. So the right side is skipped — no `ZeroDivisionError`. This is called **short-circuit evaluation**, and it is genuinely useful later for avoiding errors.

### They work on truthy values too

Because `bool()` treats empty and zero as `False` (Part 3), logical operators work on ordinary values as well:

```python
print(bool(0) and True)     # False
name = ""
print(not name)             # True   ← empty string is falsy
```

---

## 6. Operator Precedence

**Precedence is the order in which Python evaluates different operators in an expression.**

```python
z = 10 + 15 * 10
print(z)      # 160
```

Not `250`. Python does **not** just read left to right — `*` is evaluated before `+`:

```
10 + 15 * 10
     └────┘   ← 15 * 10 = 150 happens first
10 + 150  =  160
```

### The order

```
Highest priority
       ↓
()                          brackets
**                          power
*, /, //, %                 multiply, divide, floor divide, modulus
+, -                        add, subtract
==, !=, >, <, >=, <=        comparisons
not                         logical NOT
and                         logical AND
or                          logical OR
       ↓
Lowest priority
```

Read it top to bottom: whatever is higher up runs first. Arithmetic before comparisons, comparisons before logic, and `or` dead last.

### Brackets beat everything

```python
print(10 + 15 * 10)      # 160
print((10 + 15) * 10)    # 250   ← brackets force the addition first
```

`()` is at the top of the table, so anything inside brackets is evaluated first. **When in doubt, add brackets.** They cost nothing and they make your intent obvious to anyone reading the line — including you, next week.

### Same priority → left to right

Operators on the same row are evaluated left to right:

```python
print(100 / 10 * 2)     # 20.0   ← (100 / 10) * 2, not 100 / (10 * 2)
print(10 - 5 - 2)       # 3      ← (10 - 5) - 2
```

`**` is the exception — it goes **right to left**:

```python
print(2 ** 3 ** 2)      # 512    ← 2 ** (3 ** 2) = 2 ** 9, not (2 ** 3) ** 2 = 64
```

And `-` in front of a number is weaker than `**`:

```python
print(-2 ** 2)          # -4     ← -(2 ** 2)
print((-2) ** 2)        # 4
```

### Why it matters for conditions

Precedence is what lets you write conditions without brackets everywhere:

```python
print(age > 18 and salary > 30000)
```

Comparisons sit above `and` in the table, so both comparisons resolve to `True`/`False` first, and `and` combines them. Written out with the implied brackets:

```python
print((age > 18) and (salary > 30000))    # identical result
```

`not` binds tighter than `and` and `or`, but looser than comparisons:

```python
print(not 10 > 5)        # False   ← not (10 > 5)
print(not True and False) # False  ← (not True) and False
```

### Worked example

```python
print(10 + 2 * 3 ** 2 > 20 and not False)
```

```
3 ** 2            → 9        (** first)
2 * 9             → 18       (* next)
10 + 18           → 28       (+ next)
28 > 20           → True     (comparison next)
not False         → True     (not next)
True and True     → True     (and last)
```

Result: `True`. You would never write that line in real code, but tracing it once locks the table into your head.

---

## Full Working Example (`script.py`)

```python
# Operators in Python

# --- Arithmetic Operators ---
a = 10
b = 3
print("addition:", a + b)          # 13
print("subtract:", a - b)          # 7
print("multiply:", a * b)          # 30
print("divide:", a / b)            # 3.3333333333333335
print("floor divide:", a // b)     # 3
print("modulus:", a % b)           # 1
print("power:", a ** b)            # 1000


# --- Assignment Operators ---
x = 12
x += 5        # x = x + 5  → 17
x -= 5        # x = x - 5  → 12
print(x)                           # 12


# --- Comparison Operators ---
a = 19
b = "19"
print(a == b)                      # False  (int vs str)
print(a != b)                      # True

age = 18
print(age > 18)                    # False
print(age < 18)                    # False
print(age >= 18)                   # True
print(age <= 18)                   # True


# --- Logical Operators ---
print(True and True)               # True
print(True and False)              # False
print(False and True)              # False
print(False and False)             # False

print(True or True)                # True
print(True or False)               # True
print(False or True)               # True
print(False or False)              # False

print(not True)                    # False


# --- Operator Precedence ---
z = 10 + 15 * 10
print(z)                           # 160  (not 250 — * runs before +)

z = (10 + 15) * 10
print(z)                           # 250  (brackets first)
```

Run it:

```bash
python script.py      # Windows
python3 script.py     # macOS / Linux
```

---

# Practice Questions

## Practice 1

Take two numbers from the user and print all seven arithmetic results.

```python
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
```

**Sample run** — user enters `10` and `3`:

```
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Power: 1000
```

**Two things to notice:**

1. `int()` is essential — without it `a + b` would give `103`, not `13`.
2. `/` gives a float, `//` gives an int. Same division, two different answers.

> Enter `0` as the second number and you get `ZeroDivisionError`. Guarding against that needs `if`.

## Practice 2

Ask the user for a number and print whether it is even or odd — using only what you know so far.

```python
n = int(input("Enter a number: "))

print("Remainder when divided by 2:", n % 2)
print("Is it even?", n % 2 == 0)
```

**Sample run** — user enters `7`:

```
Remainder when divided by 2: 1
Is it even? False
```

**Why this works:** `n % 2` is `0` for every even number and `1` for every odd one. Comparing that to `0` with `==` turns it into a straight `True`/`False`. Note the precedence — `%` runs before `==`, so no brackets are needed.

## Practice 3

Take a person's age and salary and check whether they qualify: age above 18 **and** salary above 30000.

```python
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

print("Age check:", age > 18)
print("Salary check:", salary > 30000)
print("Qualifies:", age > 18 and salary > 30000)
```

**Sample run** — user enters `25` and `50000`:

```
Age check: True
Salary check: True
Qualifies: True
```

**Sample run** — user enters `16` and `50000`:

```
Age check: False
Salary check: True
Qualifies: False
```

One `False` is enough to make `and` return `False`. Swap `and` for `or` and the second run gives `True` instead — try it and watch the difference.

---

## Quick Recap

- An **operator** performs an operation; the values it works on are **operands**. In `10 + 5`, `+` is the operator and `10`, `5` are the operands.
- **Arithmetic:** `+ - * / // % **`. `/` always returns a float; `//` gives the whole-number part rounded down; `%` gives the remainder; `**` is power.
- `n % 2` is the standard even/odd check — `0` means even.
- Dividing by zero raises `ZeroDivisionError`.
- `+` joins strings and `*` repeats them, so `"10" + "20"` is `1020`, not `30`.
- **Assignment:** `=` stores a value. `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` are shortcuts — `x += 5` is just `x = x + 5`. The variable must already exist.
- **Comparison:** `== != > < >= <=` always return `True` or `False`. `>` excludes the boundary, `>=` includes it.
- `=` assigns, `==` compares. Never mix them up.
- `19 == "19"` is `False` — type matters. Convert first.
- Python allows chained comparisons: `18 < age < 60`.
- **Logical:** `and` needs both true, `or` needs at least one true, `not` flips it. They short-circuit, so the right side may never run.
- **Precedence** decides evaluation order: `()` → `**` → `* / // %` → `+ -` → comparisons → `not` → `and` → `or`.
- `10 + 15 * 10` is `160`, not `250`. When in doubt, use brackets — they are free and they make your intent clear.
