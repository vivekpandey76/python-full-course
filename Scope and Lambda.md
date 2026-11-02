# Scope & Lambda

Notes for Part 14 of the course. Code first, short explanations, nothing extra.

---

## 1. Local & Global Scope

**Scope is where a variable can be used.**

| Type | Created | Can be used |
|---|---|---|
| Local | inside a function | only inside that function |
| Global | outside all functions | anywhere (read) |

```python
name = "Vivek"          # global

def greet():
    msg = "Hello"       # local
    print(msg, name)    # reading a global is fine

greet()
print(msg)
```

```
Hello Vivek
NameError: name 'msg' is not defined
```

`msg` is gone once the function ends.

### Same name inside and outside

The function uses its own local one. The global stays untouched.

```python
x = 10

def show():
    x = 99          # new local x, not the global one
    print("inside:", x)

show()
print("outside:", x)
```

```
inside: 99
outside: 10
```

**Q → Game app: `score = 100` is global. Write `show_score()` that prints it. Then write `reset()` that sets `score = 0` without `global`. Why does the global not change?**

```python
score = 100

def show_score():
    print(score)

def reset():
    score = 0       # creates a new local score

show_score()
reset()
print(score)
```

```
100
100
```

`score = 0` inside `reset()` creates a **new local variable**. The global `score` is never touched.

---

## 2. `global`

**To change a global variable inside a function, write `global name` first.**

| Action on a global | Need `global`? |
|---|---|
| Read it | No |
| Change it | Yes |

```python
count = 0

def increase():
    global count
    count += 1

increase()
increase()
print(count)
```

```
2
```

Without `global`, Python treats `count` as local, and it has no value yet:

```python
count = 0

def increase():
    count += 1

increase()
```

```
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

> **Use `global` rarely.** Better: pass the value in and return the new value.
>
> ```python
> def increase(count):
>     return count + 1
>
> count = increase(count)
> ```

**Q → Website counter: `visits = 0`. Write `new_visit()` that adds 1. Call it 3 times.**

```python
visits = 0

def new_visit():
    global visits
    visits += 1

new_visit()
new_visit()
new_visit()
print(visits)
```

```
3
```

Remove the `global visits` line and you get `UnboundLocalError`.

---

## 3. `nonlocal`

**Used in a function inside another function. Lets the inner function change the outer function's variable.**

| Keyword | Changes variable of |
|---|---|
| `global` | the whole file |
| `nonlocal` | the outer (enclosing) function |

```python
def outer():
    x = 1

    def inner():
        nonlocal x
        x = 5

    inner()
    print(x)

outer()
```

```
5
```

Without `nonlocal`, `x = 5` would create a new local `x` inside `inner()` and `outer()` would still print `1`.

**Q → Wallet app: `wallet()` has `balance = 100`. Inside it, `add_money()` adds 50 using `nonlocal`. Call it twice.**

```python
def wallet():
    balance = 100

    def add_money():
        nonlocal balance
        balance += 50

    add_money()
    add_money()
    print(balance)

wallet()
```

```
200
```

### How Python finds a variable (LEGB)

When you use a name, Python searches in this order and stops at the first match:

| Order | Scope | Example |
|---|---|---|
| L | Local | inside the current function |
| E | Enclosing | the outer function |
| G | Global | top of the file |
| B | Built-in | `print`, `len`, `sum` |

---

## 4. Lambda Functions

**A lambda is a small one-line function with no name.**

```
lambda inputs: result
```

```python
# normal function
def square(n):
    return n * n

# same thing as lambda
square = lambda n: n * n

print(square(5))
```

```
25
```

| Point | Detail |
|---|---|
| `return` | not written, the result is returned automatically |
| Lines | only one expression |
| Inputs | any number: `lambda a, b: a + b` |
| Use for | short, one-time logic (mostly inside `map`, `filter`, `sorted`) |
| Use `def` for | anything with more than one step |

### Lambda with if-else

```python
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(7))
```

```
Odd
```

### Lambda as a sort key (very common)

```python
students = [("Amit", 72), ("Priya", 91), ("Rahul", 65)]
print(sorted(students, key=lambda s: s[1]))
```

```
[('Rahul', 65), ('Amit', 72), ('Priya', 91)]
```

`key` tells `sorted()` what to compare. Here, the marks.

**Q → Shopping app: write a lambda `add_gst` that adds 18% GST.**

```python
add_gst = lambda price: price + price * 0.18
print(add_gst(100))
```

```
118.0
```

**Q → Write a lambda `is_even` that returns `True` if a number is even.**

```python
is_even = lambda n: n % 2 == 0
print(is_even(4))
print(is_even(9))
```

```
True
False
```

---

## 5. `map()`

**Applies a function to every item of a list.**

```
map(function, list)
```

```python
nums = [1, 2, 3, 4]
result = map(lambda n: n * 2, nums)

print(result)
print(list(result))
```

```
<map object at 0x...>
[2, 4, 6, 8]
```

`map()` returns a map object. Wrap it in `list()` to see the values.

**Q → Price list: add ₹50 delivery to each price.**

```python
prices = [100, 250, 400]
print(list(map(lambda p: p + 50, prices)))
```

```
[150, 300, 450]
```

**Q → Make all names uppercase.**

```python
names = ["rahul", "priya", "amit"]
print(list(map(str.upper, names)))
```

```
['RAHUL', 'PRIYA', 'AMIT']
```

You can pass any function to `map()`, not just a lambda. `lambda n: n.upper()` also works.

---

## 6. `filter()`

**Keeps only the items where the function returns `True`.**

```
filter(function, list)
```

```python
nums = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda n: n % 2 == 0, nums)))
```

```
[2, 4, 6]
```

### `map` vs `filter`

| | `map()` | `filter()` |
|---|---|---|
| Job | changes every item | picks some items |
| Function returns | new value | `True` / `False` |
| Output length | same as input | same or smaller |

**Q → Exam results: keep only passing marks (>= 40).**

```python
marks = [35, 80, 42, 90, 25]
print(list(filter(lambda m: m >= 40, marks)))
```

```
[80, 42, 90]
```

**Q → Filter prices above 1000, then give 10% off.**

```python
prices = [500, 1200, 300, 2500]

costly = filter(lambda p: p > 1000, prices)
final = map(lambda p: p * 0.9, costly)

print(list(final))
```

```
[1080.0, 2250.0]
```

---

## Quick Recap

- **Local** variables live only inside their function. **Global** variables can be read anywhere.
- Assigning to a name inside a function makes it **local**, even if a global has the same name.
- **`global`** is needed to change a global. Reading does not need it.
- **`nonlocal`** changes the outer function's variable from an inner function.
- Python looks up names in **LEGB** order: Local, Enclosing, Global, Built-in.
- **`lambda inputs: result`** is a one-line function with no `return` keyword.
- **`map()`** changes every item. **`filter()`** keeps items that pass a test.
- Both return objects. Wrap them in **`list()`**.

---

## Interview Questions

**1. What is the output?**

```python
x = 5

def f():
    print(x)
    x = 10

f()
```

```
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
```

Because `x = 10` appears in the function, Python treats `x` as local for the **whole** function, so the `print` runs before it has a value.

**2. What is the difference between `global` and `nonlocal`?**

`global` changes a variable at the top of the file. `nonlocal` changes a variable of the enclosing (outer) function. `nonlocal` does not work for global variables.

**3. Lambda vs normal function?**

A lambda has no name, only one expression, and no `return` keyword. A `def` function can have many lines, statements and a name. Use lambda for short logic passed to `map`, `filter` or `sorted`.

**4. Square only the odd numbers from a list in one line.**

```python
nums = [1, 2, 3, 4, 5]
print(list(map(lambda n: n * n, filter(lambda n: n % 2 != 0, nums))))
```

```
[1, 9, 25]
```

The same with a list comprehension, which is often easier to read:

```python
print([n * n for n in nums if n % 2 != 0])
```

**5. Sort a list of words by length.**

```python
words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words, key=lambda w: len(w)))
```

```
['fig', 'kiwi', 'apple', 'banana']
```
