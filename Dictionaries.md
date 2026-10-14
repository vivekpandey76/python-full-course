# Dictionaries

Notes for Part 11 of the course. Code first, short explanations, nothing extra.

---

## 1. What is a Dictionary?

**A dictionary stores data as `key: value` pairs inside `{ }`. You look up a value by its key, not by a position.**

```python
student = {
    "name": "Vivek",
    "age": 25,
    "city": "Mumbai"
}

print(student)
print(len(student))
```

```
{'name': 'Vivek', 'age': 25, 'city': 'Mumbai'}
3
```

`len()` counts the pairs, not the keys and values separately.

Think of it like a real dictionary: you search for a **word** (key) and get its **meaning** (value).

| Rule | What it means |
|---|---|
| Key-value pairs | every item is `key: value` |
| Keys are unique | the same key cannot appear twice |
| Order kept | items stay in the order you added them (Python 3.7+) |
| Mutable | you can add, change and remove items |

### Two ways to make an empty dictionary

```python
a = {}
b = dict()

print(type(a))
print(type(b))
```

```
<class 'dict'>
<class 'dict'>
```

Remember from the Sets notes: `{}` is an empty **dict**, not an empty set.

---

## 2. Keys: Unique and Immutable

### Duplicate keys: the last one wins

```python
user = {
    "firstName": "Vivek",
    "lastName": "Pandey",
    "firstName": "Virat"
}

print(user)
```

```
{'firstName': 'Virat', 'lastName': 'Pandey'}
```

No error. The second `"firstName"` simply overwrites the first.

### What can be a key?

Keys must be **immutable**: strings, numbers, booleans, tuples. Values can be **anything**.

```python
data = {
    "name": "Vivek",
    12: "a number key",
    ("x", "y"): "a tuple key",
    "skills": ["python", "sql"]     # a list as a VALUE is fine
}

print(data[12])
print(data[("x", "y")])
```

```
a number key
a tuple key
```

A list as a **key** fails:

```python
data = {["a", "b"]: "test"}
```

```
TypeError: unhashable type: 'list'
```

Same rule as sets: if it can change, it cannot be a key.

---

## 3. Accessing Values: `[]` vs `get()`

```python
student = {"name": "Vivek", "age": 25, "city": "Mumbai"}

print(student["name"])
print(student.get("age"))
```

```
Vivek
25
```

Both work when the key exists. The difference shows when it **does not**:

```python
print(student["phone"])
```

```
KeyError: 'phone'
```

```python
print(student.get("phone"))
print(student.get("phone", "not found"))
```

```
None
not found
```

| Way | Key exists | Key missing |
|---|---|---|
| `d[key]` | returns value | `KeyError`, program stops |
| `d.get(key)` | returns value | returns `None` |
| `d.get(key, default)` | returns value | returns `default` |

> **Which one to use:** use `get()` when the key might be missing. Use `[]` when the key must exist and a missing key is a real bug.

The default goes in as the second argument. `student.get("phone", default="x")` is an error, because `get()` does not accept `default=` as a keyword.

**Q → From the student dict print `name`, then safely get `"phone"` with default `"not found"`.**

```python
print(student["name"])
print(student.get("phone", "not found"))
```

```
Vivek
not found
```

---

## 4. Adding and Changing Items

**The same syntax does both. If the key exists, it changes. If not, it is added.**

```python
student = {"name": "Vivek", "age": 25}

student["age"] = 26            # key exists, value changes
student["city"] = "Mumbai"     # new key, pair is added

print(student)
```

```
{'name': 'Vivek', 'age': 26, 'city': 'Mumbai'}
```

### `update()`: change or add many at once

```python
d = {"name": "Vivek", "age": 25}
d.update({"name": "Virat", "domain": "CS"})

print(d)
```

```
{'name': 'Virat', 'age': 25, 'domain': 'CS'}
```

`"name"` already existed, so it changed. `"domain"` was new, so it was added.

**Q → Merge `{"a": 1, "b": 2}` with `{"b": 20, "c": 3}`. What happens to `"b"`?**

```python
d = {"a": 1, "b": 2}
d.update({"b": 20, "c": 3})
print(d)
```

```
{'a': 1, 'b': 20, 'c': 3}
```

`"b"` becomes `20`. When both have the same key, the new value wins.

---

## 5. Removing Items

| Way | What it does | If key is missing |
|---|---|---|
| `pop(key)` | removes the key and **returns its value** | `KeyError` |
| `pop(key, default)` | same, but returns `default` if missing | no error |
| `popitem()` | removes and returns the **last** pair | `KeyError` if empty |
| `del d[key]` | removes the key, returns nothing | `KeyError` |
| `clear()` | removes everything | |

```python
student = {"name": "Vivek", "age": 25, "city": "Mumbai", "marks": 80}

city = student.pop("city")
print(city)
print(student)

last = student.popitem()
print(last)
print(student)

del student["age"]
print(student)

student.clear()
print(student)
```

```
Mumbai
{'name': 'Vivek', 'age': 25, 'marks': 80}
('marks', 80)
{'name': 'Vivek', 'age': 25}
{'name': 'Vivek'}
{}
```

Notice that `popitem()` returns a **tuple** `(key, value)`.

**Q → Add `"marks": 80`, change age to `26`, then pop `"city"` and print what was removed.**

```python
student = {"name": "Vivek", "age": 25, "city": "Mumbai"}

student["marks"] = 80
student["age"] = 26
removed = student.pop("city")

print(removed)
print(student)
```

```
Mumbai
{'name': 'Vivek', 'age': 26, 'marks': 80}
```

---

## 6. `keys()`, `values()`, `items()`

```python
student = {"name": "Vivek", "age": 25, "city": "Mumbai"}

print(student.keys())
print(student.values())
print(student.items())
```

```
dict_keys(['name', 'age', 'city'])
dict_values(['Vivek', 25, 'Mumbai'])
dict_items([('name', 'Vivek'), ('age', 25), ('city', 'Mumbai')])
```

| Method | Gives you |
|---|---|
| `keys()` | all keys |
| `values()` | all values |
| `items()` | all pairs as `(key, value)` tuples |

### Checking with `in`

`in` checks **keys only**, not values:

```python
print("name" in student)
print("Vivek" in student)
print("Vivek" in student.values())
```

```
True
False
True
```

---

## 7. Looping Through a Dictionary

### Loop over keys (the default)

```python
student = {"name": "Vivek", "age": 25}

for k in student:
    print(k)
```

```
name
age
```

Looping over a dict directly gives you the keys. `for k in student.keys()` does the same thing.

### Loop over values

```python
for v in student.values():
    print(v)
```

```
Vivek
25
```

### Loop over both (most used)

```python
for k, v in student.items():
    print(k, "=", v)
```

```
name = Vivek
age = 25
```

Each item is a tuple `(key, value)`, and `k, v` unpacks it, just like tuple unpacking.

**Q → Loop over `{"math": 90, "sci": 75, "eng": 85}` and print `math -> 90` for each.**

```python
subjects = {"math": 90, "sci": 75, "eng": 85}

for k, v in subjects.items():
    print(f"{k} -> {v}")
```

```
math -> 90
sci -> 75
eng -> 85
```

---

## 8. Nested Dictionaries

**A dictionary can hold another dictionary as a value. Chain the keys to go deeper.**

```python
students = {
    "vivek": {
        "age": 25,
        "marks": {"math": 99, "sci": 88}
    }
}

print(students["vivek"]["age"])
print(students["vivek"]["marks"]["math"])
```

```
25
99
```

Read it left to right: open `"vivek"`, then open `"marks"`, then take `"math"`.

**Q → Make 2 students with age and city. Print the city of the second one, then change it.**

```python
students = {
    1: {"age": 25, "city": "Mumbai"},
    2: {"age": 27, "city": "Delhi"}
}

print(students[2]["city"])
students[2]["city"] = "Pune"
print(students)
```

```
Delhi
{1: {'age': 25, 'city': 'Mumbai'}, 2: {'age': 27, 'city': 'Pune'}}
```

---

## 9. Dictionary Comprehension

**Build a dictionary in one line. Same idea as list comprehension, with `key: value` instead of one item.**

```python
{key: value for item in iterable}
```

### Squares of 1 to 5

The loop way:

```python
squares = {}
for i in range(1, 6):
    squares[i] = i * i

print(squares)
```

The comprehension way:

```python
squares = {i: i * i for i in range(1, 6)}
print(squares)
```

Both print:

```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

> **Common mistake:** writing `squares[1] = i * i` in the loop. That uses the fixed key `1` every time, so you end up with only `{1: 25}`. The key must be the loop variable `i`.

### With a condition

**Q → From `{"a": 10, "b": 25, "c": 40}` keep only values above 20.**

```python
d = {"a": 10, "b": 25, "c": 40}

result = {k: v for k, v in d.items() if v > 20}
print(result)
```

```
{'b': 25, 'c': 40}
```

---

## 10. Dictionary vs List vs Tuple vs Set

| | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Brackets | `[ ]` | `( )` | `{ }` | `{key: value}` |
| Access by | index | index | not possible | key |
| Order kept | Yes | Yes | No | Yes |
| Duplicates | Allowed | Allowed | Not allowed | Keys no, values yes |
| Changeable | Yes | No | Yes | Yes |

**Pick a dictionary when:** each value has a label. A student's name, age and city, a word and its count, a username and its password. If you find yourself remembering "index 2 is the city", you want a dictionary.

---

## Quick Recap

- **`{"key": value}`** makes a dictionary. `{}` or `dict()` makes an empty one.
- **Keys are unique.** A duplicate key overwrites the earlier one.
- **Keys must be immutable.** A list as a key is a `TypeError`. Values can be anything.
- **`d[key]`** raises `KeyError` if missing. **`d.get(key, default)`** is the safe way.
- **`d[key] = value`** adds a new key or changes an existing one.
- **`update()`** merges another dict. Same keys get the new value.
- **Remove:** `pop(key)` returns the value, `popitem()` removes the last pair, `del d[key]` just deletes, `clear()` empties it.
- **`keys()`, `values()`, `items()`** give you the parts. `in` checks keys only.
- **`for k, v in d.items()`** is the standard loop.
- **Nested dicts:** chain keys like `d["a"]["b"]`.
- **Comprehension:** `{k: v for k, v in d.items() if condition}`.

---

## Interview Questions

**1. What is the difference between `d[key]` and `d.get(key)`?**

Both return the value if the key exists. If it is missing, `d[key]` raises `KeyError` and `d.get(key)` returns `None` (or the default you pass).

**2. Can a list be a dictionary key? Why not?**

No. Keys must be immutable (hashable) so Python can find them fast. A list can change, so it raises `TypeError: unhashable type: 'list'`. Use a tuple instead.

**3. What happens if you use the same key twice?**

```python
d = {"a": 1, "a": 2}
print(d)
```

```
{'a': 2}
```

No error. The last value wins.

**4. Count how many times each character appears in a string.**

```python
text = "banana"
count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

print(count)
```

```
{'b': 1, 'a': 3, 'n': 2}
```

`count.get(ch, 0)` returns `0` the first time a character is seen, so no `KeyError`. This pattern comes up in interviews often.

**5. Swap the keys and values of a dictionary.**

```python
d = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in d.items()}
print(swapped)
```

```
{1: 'a', 2: 'b', 3: 'c'}
```

This only works cleanly when the values are unique. If two keys share a value, one of them is lost.
