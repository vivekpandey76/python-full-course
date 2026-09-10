# Tuples

Notes for Part 9 of the course. Code first, short explanations, nothing extra.

---

## 1. What is a Tuple?

**A tuple stores many values in one variable, written inside `( )`. Once created, it cannot be changed.**

```python
point = (10, 20)
empty = ()

print(point)
print(len(point))
```

```
(10, 20)
2
```

Everything about a list applies here — comma separated, order is fixed, duplicates allowed — except one thing: a tuple is **immutable**.

### The comma is what makes a tuple, not the brackets

```python
print(type(("hi",)))      # comma -> tuple
print(type(("hi")))       # no comma -> just a string in brackets
```

```
<class 'tuple'>
<class 'str'>
```

A single item tuple **needs** the trailing comma. Without it, Python reads `( )` as normal grouping brackets.

And because the comma is the real signal, the brackets are optional:

```python
t = 10, 20, 30
print(t)
print(type(t))
```

```
(10, 20, 30)
<class 'tuple'>
```

### Converting a list into a tuple

```python
print(tuple([1, 2, 3]))
```

```
(1, 2, 3)
```

**Q → Make a tuple of 3 cities, print it and its `len()`. Then make a single item tuple and check its `type()`.**

```python
city_names = ("mumbai", "bangalore", "delhi")
print(city_names)
print(len(city_names))

numbers = (10,)
print(type(numbers))
```

```
('mumbai', 'bangalore', 'delhi')
3
<class 'tuple'>
```

---

## 2. Indexing & Slicing

**Exactly the same rules as lists and strings — counting starts at 0.**

```python
t = ("a", "b", "c", "d")
#     0    1    2    3
#    -4   -3   -2   -1

print(t[0])
print(t[-1])
```

```
a
d
```

Going past the end is still an error:

```python
print(t[10])
```

```
IndexError: tuple index out of range
```

Slicing works the same way — `start` included, `end` excluded:

```python
t = ("a", "b", "c", "d")

print(t[1:3])
print(t[:2])
print(t[2:])
print(t[::-1])
```

```
('b', 'c')
('a', 'b')
('c', 'd')
('d', 'c', 'b', 'a')
```

Slicing gives back a **new tuple**. It never touches the original — and since a tuple cannot be touched anyway, this is the only way to get a "changed" version.

**Q → From `(10, 20, 30, 40, 50)` print the middle three items and the tuple reversed.**

```python
num = (10, 20, 30, 40, 50)
print(num[1:4])
print(num[::-1])
```

```
(20, 30, 40)
(50, 40, 30, 20, 10)
```

---

## 3. Tuples are Immutable

**This is the whole point of a tuple. Nothing can be replaced, added, or removed after it is created.**

```python
t = ("a", "b", "c", "d")
t[0] = 99
```

```
TypeError: 'tuple' object does not support item assignment
```

The list methods that change things simply do not exist:

```python
t.append("e")
```

```
AttributeError: 'tuple' object has no attribute 'append'
```

No `append`, no `insert`, no `extend`, no `remove`, no `pop`, no `sort`, no `reverse`, no `clear`.

### A tuple has only two methods

| Method | What it does |
|---|---|
| `count(x)` | how many times `x` appears |
| `index(x)` | position of the first `x` |

```python
city_names = ("mumbai", "bangalore", "delhi", "vivek", "bangalore")

print(city_names.count("bangalore"))
print(city_names.index("bangalore"))
```

```
2
1
```

That is it. Two methods, because every other list method changes the list.

### How to "change" a tuple

You cannot. What you do instead is convert it to a list, edit that, and convert it back:

```python
city_names = ("mumbai", "bangalore", "delhi", "vivek", "bangalore")

temp = list(city_names)      # tuple -> list
temp[0] = "UP"               # edit the list
city_names = tuple(temp)     # list -> tuple

print(city_names)
```

```
('UP', 'bangalore', 'delhi', 'vivek', 'bangalore')
```

The original tuple was never modified — a brand new tuple was built and the name `city_names` was pointed at it.

### `sorted()` works, but gives back a list

```python
numbers = (10, 20, 54, 34)
sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(type(sorted_numbers))
```

```
[10, 20, 34, 54]
<class 'list'>
```

`sorted()` always returns a **list**, whatever you feed it. Wrap it if you want a tuple back:

```python
print(tuple(sorted(numbers)))
```

```
(10, 20, 34, 54)
```

> **Note:** `numbers.sort()` does not exist on a tuple. `sort()` sorts in place, and a tuple has no "in place".

**Q → Try changing an item and read the error. Then do the same change through `list()` and `tuple()`.**

```python
t = (10, 20, 30)
# t[0] = 99                  # TypeError: 'tuple' object does not support item assignment

temp = list(t)
temp[0] = 99
t = tuple(temp)
print(t)
```

```
(99, 20, 30)
```

---

## 4. Unpacking

**Unpacking means taking the values out of a tuple and putting them into individual variables in one line.**

```python
point = (10, 20)
x, y = point

print(x)
print(y)
```

```
10
20
```

The number of variables must match the number of items:

```python
a, b = (1, 2, 3)
```

```
ValueError: too many values to unpack (expected 2)
```

### Swapping variables

This is the trick you will use most often:

```python
a = 5
b = 9

a, b = b, a

print(a)
print(b)
```

```
9
5
```

The right side `b, a` builds a tuple first, then it is unpacked into the left side. No temporary variable needed.

It works on whole tuples too:

```python
point = (10, 30, 40)
point1 = (50, 60, 70)

point, point1 = point1, point

print(point)
print(point1)
```

```
(50, 60, 70)
(10, 30, 40)
```

### Star unpacking — `*rest`

When you only care about the first item and want the rest in one go:

```python
first, *rest = (1, 2, 3, 4)

print(first)
print(rest)
print(type(rest))
```

```
1
[2, 3, 4]
<class 'list'>
```

`rest` collects everything left over, and it comes back as a **list**, not a tuple.

**Q → Unpack `(2025, "September", 9)` into `year`, `month`, `day`. Then swap two of them.**

```python
dummy = (2025, "September", 9)

year, month, day = dummy
print(year, month, day)

year, month = month, year
print(year, month, day)
```

```
2025 September 9
September 2025 9
```

---

## 5. Immutable Tuple, Mutable Item

**A tuple locks its slots, not the objects sitting in them.**

```python
t = (1, 2, [3, 4])
t[2].append(89)

print(t)
```

```
(1, 2, [3, 4, 89])
```

No error. This surprises everyone the first time.

Read it slowly. `t[2]` is a **list**, and lists are mutable, so `append()` on it is perfectly legal. The tuple still holds the same three items in the same three slots — the third item just happens to have changed inside itself.

What is still blocked is replacing a slot:

```python
t[1] = 99
```

```
TypeError: 'tuple' object does not support item assignment
```

> **The rule:** a tuple stops you from changing *which* objects it holds. It cannot stop you from changing *those objects* if they are mutable themselves.

---

## 6. Tuple vs List

| | Tuple | List |
|---|---|---|
| Brackets | `( )` | `[ ]` |
| Changeable | No (immutable) | Yes (mutable) |
| Methods | only `count()`, `index()` | `append()`, `remove()`, `sort()` … |
| Speed / memory | slightly faster, lighter | slightly heavier |
| Use it when | the data must stay fixed | the data may change or grow |

**When to pick a tuple:** coordinates `(10, 20)`, an RGB colour `(255, 0, 0)`, a date `(2025, 9, 9)`, a database row, returning several values from a function. Things that belong together and should not be edited by accident.

**When to pick a list:** a shopping cart, a to-do list, scores you keep appending to. Anything that grows, shrinks, or gets sorted.

Immutability is a feature here, not a limitation. If the data is not supposed to change, a tuple makes an accidental change an error instead of a silent bug.

---

## Quick Recap

- **`( )`** makes a tuple, **`[ ]`** makes a list. A tuple is **immutable**.
- **The comma makes the tuple, not the brackets.** `(5,)` is a tuple, `(5)` is an `int`. And `10, 20` is already a tuple without any brackets.
- **Indexing and slicing** are identical to lists. `t[0]`, `t[-1]`, `t[1:3]`, `t[::-1]`. Slicing returns a **new** tuple.
- **`t[0] = x` is a `TypeError`.** No `append` / `remove` / `sort` / `reverse` either.
- **Only two methods:** `count()` and `index()`.
- **To "change" a tuple:** `list(t)` → edit → `tuple(temp)`.
- **`sorted(t)` returns a LIST**, not a tuple. Wrap it in `tuple()` if you need one.
- **Unpacking:** `x, y = point`. Counts must match or it is a `ValueError`.
- **Swap:** `a, b = b, a`.
- **`first, *rest = (1,2,3,4)`** → `rest` is a **list**.
- **A mutable item inside a tuple can still be changed** — `t = (1, 2, [3, 4])` then `t[2].append(5)` works fine.

---

## Interview Questions

**1. List vs tuple, and when would you pick a tuple?**

A list is mutable — you can change, add, or remove items. A tuple is immutable — once created, its items cannot be changed.

Use a **list** when the data may change or grow. Use a **tuple** when the data should stay fixed. A tuple is also slightly faster and lighter, and it protects the data from being edited by mistake.

**2. `t = (1, 2, [3, 4])` and then `t[2].append(5)` — error or not?**

**No error.** The result is `(1, 2, [3, 4, 5])`.

A tuple stops you from replacing, adding, or removing *its* elements. But if one of those elements is a mutable object like a list, that object can still be changed from the inside. The tuple's slots never moved — only the list living in slot 2 grew.

`t[2] = [9]` **would** raise `TypeError`, because that is replacing a slot.

**3. Why does `("hi")` not give a tuple?**

Because brackets alone mean grouping, the same as in `(2 + 3) * 4`. The **comma** is what creates a tuple. `("hi")` is just the string `"hi"`; `("hi",)` is a one item tuple.

**4. Can a tuple be a dictionary key?**

Yes — as long as everything inside it is immutable. Dictionary keys must be hashable, and tuples of immutable items are. A list can never be a key. But `(1, 2, [3])` cannot be a key either, because it contains a list.
