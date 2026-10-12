# Sets

Notes for Part 10 of the course. Code first, short explanations, nothing extra.

---

## 1. What is a Set?

**A set stores many values in one variable, written inside `{ }`. It keeps only unique values and has no order.**

```python
numbers = {1, 2, 3, 2, 1}

print(numbers)
print(len(numbers))
```

```
{1, 2, 3}
3
```

The duplicates `2` and `1` were thrown away automatically. You did not have to do anything.

Three things to remember about a set:

| Rule | What it means |
|---|---|
| No duplicates | every value appears only once |
| No order | items can come out in any order, no index positions |
| Mutable | you can add and remove items |

### No order means the print order can change

```python
fruits = {"apple", "banana", "mango"}
print(fruits)
```

```
{'mango', 'apple', 'banana'}
```

You may see a different order on your machine, or even on the next run. That is normal. Never rely on the order of a set.

### Empty set: `{}` is NOT a set

```python
a = {}
b = set()

print(type(a))
print(type(b))
```

```
<class 'dict'>
<class 'set'>
```

Empty curly brackets make a **dictionary**. For an empty set you must write `set()`.

### Converting a list into a set

This is the fastest way to remove duplicates:

```python
marks = [90, 80, 90, 70, 80]
unique_marks = set(marks)

print(unique_marks)
```

```
{80, 90, 70}
```

**Q → Make a set from `[5, 5, 6, 7, 7, 7]`, print it and its `len()`. Then make an empty set and check its `type()`.**

```python
nums = set([5, 5, 6, 7, 7, 7])
print(nums)
print(len(nums))

empty = set()
print(type(empty))
```

```
{5, 6, 7}
3
<class 'set'>
```

---

## 2. No Indexing, No Slicing

**A set has no positions, so `s[0]` does not work.**

```python
s = {10, 20, 30}
print(s[0])
```

```
TypeError: 'set' object is not subscriptable
```

Slicing like `s[1:3]` fails the same way.

### So how do you read the items?

Use a loop:

```python
s = {10, 20, 30}

for item in s:
    print(item)
```

```
10
20
30
```

Or check if something is inside with `in`:

```python
s = {10, 20, 30}

print(20 in s)
print(99 in s)
```

```
True
False
```

> **Note:** `in` on a set is much faster than `in` on a list. With a big list, Python checks items one by one. With a set, it jumps straight to the answer. This is a big reason sets are used in real code.

---

## 3. Only Immutable Items Allowed

**Items inside a set must be things that cannot change: numbers, strings, tuples, booleans.**

```python
s = {1, "hello", (2, 3)}
print(s)
```

```
{1, (2, 3), 'hello'}
```

A list cannot go inside a set, because a list can change:

```python
s = {1, [2, 3]}
```

```
TypeError: unhashable type: 'list'
```

"Unhashable" just means "this item can change, so a set cannot store it".

### Watch out: `True` and `1` are the same to a set

```python
s = {1, True, 0, False}
print(s)
```

```
{0, 1}
```

Python treats `True` as `1` and `False` as `0`, so they count as duplicates.

---

## 4. Adding Items

| Method | What it does |
|---|---|
| `add(x)` | adds one item |
| `update(x)` | adds many items from a list, tuple, or another set |

```python
s = {1, 2}

s.add(3)
print(s)

s.add(2)          # already there, nothing happens
print(s)

s.update([4, 5, 6])
print(s)
```

```
{1, 2, 3}
{1, 2, 3}
{1, 2, 3, 4, 5, 6}
```

Adding a value that already exists gives no error. It is just ignored.

---

## 5. Removing Items

| Method | What it does | If item is missing |
|---|---|---|
| `remove(x)` | removes `x` | `KeyError` |
| `discard(x)` | removes `x` | does nothing, no error |
| `pop()` | removes and returns a random item | `KeyError` if set is empty |
| `clear()` | removes everything | |

```python
s = {10, 20, 30, 40}

s.remove(10)
print(s)

s.discard(20)
print(s)

s.discard(999)    # not there, no error
print(s)
```

```
{40, 20, 30}
{40, 30}
{40, 30}
```

Now `remove()` with a missing item:

```python
s = {10, 20}
s.remove(999)
```

```
KeyError: 999
```

> **Which one to use:** use `discard()` when you are not sure the item exists. Use `remove()` when it must exist and you want an error if it does not.

### `pop()` removes a random item

```python
s = {"a", "b", "c"}
x = s.pop()

print(x)
print(s)
```

```
b
{'c', 'a'}
```

Since a set has no order, you cannot choose which item `pop()` takes.

### `clear()`

```python
s = {1, 2, 3}
s.clear()
print(s)
```

```
set()
```

An empty set prints as `set()`, not `{}`.

**Q → Start with `{1, 2, 3}`. Add `4`, add `[5, 6]` together, remove `1`, and safely discard `100`.**

```python
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
s.remove(1)
s.discard(100)
print(s)
```

```
{2, 3, 4, 5, 6}
```

---

## 6. Set Operations

**This is where sets shine. You can compare two groups in one line.**

Use these two sets for every example below:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

| Operation | Symbol | Method | Meaning |
|---|---|---|---|
| Union | `a \| b` | `a.union(b)` | everything from both |
| Intersection | `a & b` | `a.intersection(b)` | only common items |
| Difference | `a - b` | `a.difference(b)` | in `a` but not in `b` |
| Symmetric difference | `a ^ b` | `a.symmetric_difference(b)` | in one, but not both |

### Union: everything, no duplicates

```python
print(a | b)
```

```
{1, 2, 3, 4, 5, 6}
```

### Intersection: only what both have

```python
print(a & b)
```

```
{3, 4}
```

### Difference: what `a` has that `b` does not

```python
print(a - b)
print(b - a)
```

```
{1, 2}
{5, 6}
```

Order matters here. `a - b` and `b - a` are different.

### Symmetric difference: everything except the common part

```python
print(a ^ b)
```

```
{1, 2, 5, 6}
```

### Real example

```python
python_students = {"amit", "riya", "karan", "neha"}
java_students = {"riya", "neha", "rahul"}

print(python_students & java_students)   # in both classes
print(python_students - java_students)   # only python
print(python_students | java_students)   # all students
```

```
{'riya', 'neha'}
{'amit', 'karan'}
{'amit', 'riya', 'karan', 'neha', 'rahul'}
```

(Your order may be different.)

**Q → Given `x = {1, 2, 3}` and `y = {2, 3, 4}`, print the common items and the items only in `x`.**

```python
x = {1, 2, 3}
y = {2, 3, 4}

print(x & y)
print(x - y)
```

```
{2, 3}
{1}
```

---

## 7. Subset and Superset

**Checks if one set is fully inside another.**

```python
small = {1, 2}
big = {1, 2, 3, 4}

print(small.issubset(big))     # is small fully inside big?
print(big.issuperset(small))   # does big contain all of small?
```

```
True
True
```

`isdisjoint()` checks if two sets have nothing in common:

```python
print({1, 2}.isdisjoint({3, 4}))
print({1, 2}.isdisjoint({2, 3}))
```

```
True
False
```

---

## 8. Frozenset

**A frozenset is a set that cannot be changed. Think of it as the "tuple version" of a set.**

```python
fs = frozenset([1, 2, 3, 2])
print(fs)

fs.add(4)
```

```
frozenset({1, 2, 3})
AttributeError: 'frozenset' object has no attribute 'add'
```

Still unique, still no order, but no `add`, `remove`, or `update`. Union, intersection and the rest still work, because they return a new set instead of changing this one.

You will rarely need it. Just know it exists.

---

## 9. Set vs List vs Tuple

| | List | Tuple | Set |
|---|---|---|---|
| Brackets | `[ ]` | `( )` | `{ }` |
| Order kept | Yes | Yes | No |
| Duplicates | Allowed | Allowed | Not allowed |
| Indexing `x[0]` | Yes | Yes | No |
| Changeable | Yes | No | Yes |
| `in` check speed | slow on big data | slow on big data | fast |

**Pick a set when:** you need unique values, you want to remove duplicates, you check `in` a lot, or you need to compare two groups (common items, missing items).

**Pick a list when:** order matters or you need positions.

---

## Quick Recap

- **`{1, 2, 3}`** makes a set. Values are **unique** and have **no order**.
- **`{}` is a dict.** Use **`set()`** for an empty set.
- **`set(my_list)`** removes duplicates in one step.
- **No indexing or slicing.** Use a `for` loop or `in`.
- **Only immutable items** inside. A list inside a set is a `TypeError`.
- **`True` equals `1` and `False` equals `0`** inside a set.
- **Add:** `add()` for one item, `update()` for many.
- **Remove:** `remove()` errors if missing, `discard()` does not. `pop()` takes a random item.
- **`|` union, `&` common, `-` difference, `^` not common.**
- **`issubset()`, `issuperset()`, `isdisjoint()`** compare whole sets.
- **`frozenset`** is a set that cannot change.

---

## Interview Questions

**1. How do you remove duplicates from a list?**

```python
nums = [1, 2, 2, 3, 3, 3]
print(list(set(nums)))
```

```
[1, 2, 3]
```

Convert to a set, then back to a list. The catch: the original order is **not guaranteed**. If order matters, use the loop method from the Lists notes, or `list(dict.fromkeys(nums))`.

**2. What is the difference between `remove()` and `discard()`?**

Both delete an item. If the item is not in the set, `remove()` raises `KeyError` and `discard()` silently does nothing.

**3. Why can't you do `s[0]` on a set?**

A set has no order, so there is no "first" item. No positions means no indexing.

**4. Why can't a list go inside a set?**

Set items must be immutable (hashable). A list can change, so Python cannot store it safely. A tuple of numbers or strings works fine.

**5. Find the common items between two lists.**

```python
a = [1, 2, 3, 4]
b = [3, 4, 5]
print(set(a) & set(b))
```

```
{3, 4}
```
