# Interview Questions on Lists, Tuples, Dictionaries and Sets

Notes for Part 12 of the course. Common interview questions on Python collections. Code first, short explanations, nothing extra.

---

## 1. List vs Tuple vs Dictionary vs Set

**Each one stores many values. Pick based on whether the data changes, needs order, needs labels, or must be unique.**

| Feature | List | Tuple | Dictionary | Set |
|---|---|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{"a": 1, "b": 2}` | `{1, 2, 3}` |
| Mutable | Yes | No | Yes | Yes |
| Ordered | Yes | Yes | Yes (Python 3.7+) | No |
| Duplicates | Allowed | Allowed | Keys: No, Values: Yes | Not allowed |
| Indexing | `lst[0]` | `tup[0]` | By key `d["a"]` | No |
| Lookup speed | Slow (checks one by one) | Slow (checks one by one) | Fast by key | Fast |
| Can be a dict key | No | Yes (if items are hashable) | No | No (use `frozenset`) |
| Use when | Ordered data you will change | Fixed data that must not change | Data with a label | Unique items or fast `in` check |
| Example | Shopping cart | `(lat, long)` | Student -> marks | Unique visitors |

```python
cart = ["pen", "book", "pen"]          # list: can change, keeps duplicates
location = (28.61, 77.20)              # tuple: fixed pair
marks = {"Aman": 85, "Riya": 92}       # dict: label -> value
visitors = {"u1", "u2", "u1"}          # set: duplicates removed

print(cart)
print(location[0])
print(marks["Riya"])
print(visitors)
```

```
['pen', 'book', 'pen']
28.61
92
{'u1', 'u2'}
```

---

## 2. Count the Frequency of Each Character

**Loop through the string and keep a count in a dictionary.**

```python
s = "hello"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
```

```
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

`freq.get(ch, 0)` returns the current count, or `0` if the character is new. Then we add `1`.

---

## 3. Find Common Elements Between Two Lists

### Brute force: loop and check

**Go through one list and keep each item that is also in the other list.**

```python
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]

result = []
for i in b:
    if i in a:
        result.append(i)

print(result)
```

```
[4, 5]
```

Easy to read, but `i in a` checks `a` one item at a time, so it gets slow for big lists.

### Better: use sets

**Turn both lists into sets and use `&` (intersection).**

```python
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]

common = list(set(a) & set(b))
print(sorted(common))
```

```
[4, 5]
```

`&` keeps only the values present in both sets. `sorted()` is used because sets have no order.

---

## 4. Merge Two Dictionaries and Add Values for Common Keys

**Copy the first dictionary, then add each value from the second one.**

```python
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 15, "d": 40}

result = d1.copy()
for key, value in d2.items():
    result[key] = result.get(key, 0) + value

print(result)
```

```
{'a': 10, 'b': 25, 'c': 45, 'd': 40}
```

If the key already exists, its value is added. If not, `get()` returns `0` and the key is created.

---

## 5. Group Words by Their Length

**Use the length as the key and keep a list of words as the value.**

```python
words = ["cat", "dog", "apple", "hi", "mango", "go"]
groups = {}

for word in words:
    length = len(word)
    if length not in groups:
        groups[length] = []
    groups[length].append(word)

print(groups)
```

```
{3: ['cat', 'dog'], 5: ['apple', 'mango'], 2: ['hi', 'go']}
```

The first time a length shows up, an empty list is created for it. After that, words are just appended.

---

## 6. Check Whether Two Strings Are Anagrams

**Anagrams have the same letters, just in a different order. Sort both and compare.**

```python
print(sorted("listen") == sorted("silent"))
print(sorted("hello") == sorted("world"))
```

```
True
False
```

`sorted("listen")` and `sorted("silent")` both give `['e', 'i', 'l', 'n', 's', 't']`, so they match.

### Another way: count the letters

**Count each letter in both strings (same as Question 2) and compare the two dictionaries.**

```python
s1 = "listen"
s2 = "silent"

frequency1 = {}
frequency2 = {}

for ch in s1:
    frequency1[ch] = frequency1.get(ch, 0) + 1
for ch in s2:
    frequency2[ch] = frequency2.get(ch, 0) + 1

print(frequency1 == frequency2)
```

```
True
```

Two dictionaries are equal when they have the same keys with the same values. Order does not matter.

---

## 7. List Comprehension and Dictionary Comprehension

**A one-line way to build a list or dictionary from a loop.**

```python
squares = [x * x for x in range(5)]
square_map = {x: x * x for x in range(3)}
evens = [x for x in range(10) if x % 2 == 0]

print(squares)
print(square_map)
print(evens)
```

```
[0, 1, 4, 9, 16]
{0: 0, 1: 1, 2: 4}
[0, 2, 4, 6, 8]
```

| Type | Pattern |
|---|---|
| List | `[value for item in items]` |
| Dictionary | `{key: value for item in items}` |
| With filter | add `if condition` at the end |

---

## 8. Set vs Frozenset

**A set can change. A frozenset cannot.**

```python
s = {1, 2}
s.add(3)
print(s)

fs = frozenset([1, 2])
print(fs)

# fs.add(3)   -> AttributeError: frozenset has no add()

groups = {fs: "team A"}   # frozenset works as a dict key
print(groups)
```

```
{1, 2, 3}
frozenset({1, 2})
{frozenset({1, 2}): 'team A'}
```

| | Set | Frozenset |
|---|---|---|
| Can change | Yes | No |
| Can be a dict key | No | Yes |
| Can go inside another set | No | Yes |

---

## 9. Two Sum (Asked in Amazon)

**Find the positions of two numbers that add up to the target.**

### Brute force: try every pair

**Pick each number and add it to every number after it until the sum matches.**

```python
nums = [2, 7, 11, 15]
target = 9

found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            found = True
            break
    if found:
        break
```

```
[0, 1]
```

The pairs it tries, in order: `2 + 7`, `2 + 11`, `2 + 15`, `7 + 11`, ... It stops at the first match.

`j` starts at `i + 1` so the same number is not used twice and no pair is checked twice. The `found` flag is needed because `break` only exits the inner loop.

This works, but with a nested loop the work grows fast as the list gets bigger.

### Better: use a dictionary

**Remember each number you have seen. For every new number, check if the number it needs is already saved.**

```python
nums = [2, 7, 11, 15]
target = 9

seen = {}                            # number -> its index
for i in range(len(nums)):
    num = nums[i]
    need = target - num
    if need in seen:
        print([seen[need], i])
        break
    seen[num] = i
```

```
[0, 1]
```

How it works, step by step:

| i | num | need | seen before check | Found? |
|---|---|---|---|---|
| 0 | 2 | 7 | `{}` | No, save `2: 0` |
| 1 | 7 | 2 | `{2: 0}` | Yes, print `[0, 1]` and stop |

One pass through the list. The dictionary makes each `in` check fast, so we avoid a slow nested loop.
