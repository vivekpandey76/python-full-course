# Strings

Notes for Part 7 of the course. Simple explanations, real examples, nothing extra.

---

## 1. What is a String?

**A string is text written inside quotes.**

Python accepts three kinds of quotes:

```python
name = 'Vivek'          # single quotes
name = "Vivek"          # double quotes
words = '''hello
vivek
pandey'''               # triple quotes -> keeps the line breaks
print(words)
```

```
hello
vivek
pandey
```

Single and double quotes are identical in behaviour. Pick one and stay consistent — the only real reason to switch is when the text itself contains a quote:

```python
print("It's fine")      # no escaping needed
print('It\'s fine')     # same result, more work
```

Triple quotes are for **multi-line** text. With normal quotes a line break is an error.

### `len()` — how long is it?

```python
name = "vivek pandey"
print(name)
print(len(name))
```

```
vivek pandey
12
```

`len()` counts **every** character, spaces included. That is 11 letters plus 1 space.

---

## 2. Indexing

**Every character has a position number, and counting starts at 0, not 1.**

```python
language = "PYTHON"
```

| Character | P | Y | T | H | O | N |
|---|---|---|---|---|---|---|
| **Index** | 0 | 1 | 2 | 3 | 4 | 5 |

```python
language = "PYTHON"

print(language[0])      # first character
print(language[2])      # third character
```

```
P
T
```

The third character is `language[2]`, not `language[3]`. This off-by-one is the thing to get used to.

Asking for a position that does not exist is an error:

```python
language = "PYTHON"
print(language[10])
```

```
IndexError: string index out of range
```

Six characters means valid indexes are `0` to `5`. The last index is always `len() - 1`.

---

## 3. Negative Indexing

**Negative numbers count from the end. The last character is `-1`.**

| Character | P | Y | T | H | O | N |
|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| **Negative index** | -6 | -5 | -4 | -3 | -2 | -1 |

There is no `-0`, so the end starts at `-1`.

```python
name = "PYTHON"

print(name[-1])              # clean way
print(name[len(name) - 1])   # same result, the long way
```

```
N
N
```

Both print `N`. The first one is what you actually write.

---

## 4. Slicing

**Slicing takes a piece of the string.**

```python
s[start : end : step]
```

- `start` is **included**
- `end` is **never included**
- `step` is the jump size, default `1`

That is the same rule as `range()` from Part 6 — if you remember `range(1, 11)` to reach 10, you already know slicing.

```python
name = "PYTHON"
print(name[1:3])
```

```
YT
```

Index 1 and 2, not 3. `end` is left out.

### Leaving parts empty

```python
s = "PROGRAMMING"

print(s[:3])      # from the beginning
print(s[7:])      # till the end
print(s[:])       # full copy
print(s[::2])     # every 2nd character
print(s[::-1])    # reversed
```

```
PRO
MING
PROGRAMMING
PORMIG
GNIMMARGORP
```

| Slice | Meaning |
|---|---|
| `s[:3]` | start is missing → begin at 0 |
| `s[7:]` | end is missing → go to the last character |
| `s[:]` | both missing → the whole string |
| `s[::2]` | skip every other character |
| `s[::-1]` | negative step → walk backwards, i.e. reverse |

`s[::-1]` is the standard way to reverse a string in Python. It comes back in the palindrome question.

### Same job, slicing vs a loop

Print every 2nd character of `"PYTHON"` → `P`, `T`, `O`.

```python
language = "PYTHON"

# with slicing
print(language[::2])

# with a for loop
for i in range(0, len(language), 2):
    print(language[i])
```

```
PTO
P
T
O
```

> **Careful with `range(0, len(language) - 1, 2)`.** On `"PYTHON"` (6 characters) it happens to give the right answer, but on a 7-character word it drops the last character. Write `len(language)` — the stop value is already excluded, so you do not subtract 1 as well.

---

## 5. String Operations

Three operators do most of the everyday work.

| Operator | Does | Example | Result |
|---|---|---|---|
| `+` | joins strings (concatenation) | `"Hello" + " " + "World"` | `Hello World` |
| `*` | repeats a string | `"Ha" * 3` | `HaHaHa` |
| `in` | checks if text exists inside | `"Py" in "Python"` | `True` |

```python
language = "PYTHON"

if "ON" in language:
    print("YES PRESENT")
```

```
YES PRESENT
```

`in` gives back `True` or `False`, so it drops straight into an `if`.

> `+` only joins string with string. `"Age: " + 18` is a `TypeError` — you need `str(18)`, or better, an f-string from section 8.

### Full name with a divider line

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(first_name + " " + last_name)
print("-" * 30)
```

**Sample run** — user enters `Vivek` and `Pandey`:

```
Vivek Pandey
------------------------------
```

`"-" * 30` beats typing 30 dashes: no miscounting, and changing it to 50 is a one-character edit.

---

## 6. Important String Methods

A **method** is a function attached to the string, called with a dot: `name.upper()`.

```python
name = "Vivek pandey"

print(name.upper())
print(name.lower())
print(name.replace("pandey", "mishra"))
print(name.find("v"))
print(name.count("e"))
print(name.startswith("V"))
print(name.endswith("y"))
```

```
VIVEK PANDEY
vivek pandey
Vivek mishra
2
2
True
True
```

| Method | What it does |
|---|---|
| `upper()` / `lower()` | changes the case |
| `strip()` | removes extra spaces from **both ends** |
| `replace(a, b)` | replaces every `a` with `b` |
| `find(x)` | index of `x`, or `-1` if not found |
| `count(x)` | how many times `x` appears |
| `startswith()` / `endswith()` | `True` or `False` |

Two details worth noticing above:

- `name.find("v")` gives `2`, not `0`. Index 0 holds a capital `V` — string methods are case-sensitive.
- `find()` returns `-1` when nothing matches instead of crashing, so check for `-1` rather than assuming a hit.

```python
print("banana".count("a"))
print("Vivek pandey".find("z"))
```

```
3
-1
```

### Cleaning up messy input

```python
name = "  Vivek  "
print(name.strip().upper())
```

```
VIVEK
```

The methods chain left to right: `strip()` returns `"Vivek"`, and `.upper()` runs on that result. Real `input()` almost always needs a `strip()` — users add stray spaces.

---

## 7. `split()` and `join()`

**`split()` turns a string into a list. `join()` turns a list back into a string.** They are opposites.

```python
sentence = "CodeWithVivek is my channel"

splitSentence = sentence.split()
print(splitSentence)
print("-".join(splitSentence))
```

```
['CodeWithVivek', 'is', 'my', 'channel']
CodeWithVivek-is-my-channel
```

- `split()` with nothing inside breaks on **spaces**
- `split(",")` breaks on commas instead
- With `join()`, the glue is whatever string sits **before** the dot

```python
print("a,b,c".split(","))
print("-".join(['a', 'b', 'c']))
print(" ".join(['a', 'b', 'c']))
```

```
['a', 'b', 'c']
a-b-c
a b c
```

### Sentence to list of words

```python
sentence = "Python is awesome"
sentence_list = sentence.split()
print(sentence_list)
```

```
['Python', 'is', 'awesome']
```

Once it is a list, the `for` loop from Part 6 can walk through it word by word.

---

## 8. f-strings

**The clean way to put variables inside text. Put an `f` before the quote and the variable in `{ }`.**

```python
name = "Vivek Pandey"
age = 18

print(f"My name is {name} and I am {age} years old")
```

```
My name is Vivek Pandey and I am 18 years old
```

Anything inside `{ }` gets calculated:

```python
name = "Vivek"
print(f"Hello {name}, you are {2024 - 2000} years old")
```

```
Hello Vivek, you are 24 years old
```

Compare the three ways of doing the same thing:

```python
print("My name is " + name + " and I am " + str(age) + " years old")   # + needs str()
print("My name is", name, "and I am", age, "years old")                # commas add spaces for you
print(f"My name is {name} and I am {age} years old")                   # f-string
```

The f-string wins: no `str()` conversions, no counting spaces, and you can read the final sentence right there in the code. Use it by default.

---

## 9. String Immutability

**A string cannot be changed after it is created. It can only be replaced.**

```python
s = "cat"
s[0] = "b"
```

```
TypeError: 'str' object does not support item assignment
```

Building a **new** string works fine:

```python
name = "Vivek Pandey"

print(name[1:])
print("P" + name[1:])
```

```
ivek Pandey
Pivek Pandey
```

`name[1:]` drops the first character, then `+` glues a new one in front. The original `name` is untouched — nothing was edited, a new string was made.

This is why **every string method returns a new string**:

```python
name = "vivek"

name.upper()          # result thrown away
print(name)

name = name.upper()   # result stored
print(name)
```

```
vivek
VIVEK
```

`name.upper()` on its own does nothing useful. You have to assign the result back. This is the single most common string mistake.

---

## Practice 1

Check if a word is a palindrome (`madam`, `level`).

A palindrome reads the same forwards and backwards, so: **original string == reversed string**.

```python
text = input("Enter a word: ").lower()

if text == text[::-1]:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")
```

**Sample run** — user enters `madam`:

```
Word is a palindrome
```

**Sample run** — user enters `madams`:

```
Word is not a palindrome
```

`.lower()` first, otherwise `"Madam"` fails — `"Madam"` reversed is `"madaM"`, and `M` is not `m`.

---

## Practice 2

Take a sentence and print every word on a new line.

```python
sentence = input("Enter your sentence: ")
sentence_list = sentence.split()

for val in sentence_list:
    print(val)
```

**Sample run** — user enters `Python is awesome`:

```
Python
is
awesome
```

Two steps: `split()` makes the list, the `for` loop prints one item per turn.

> **Do not loop over the sentence directly.** `for val in sentence` walks through it **character by character**, so you would get `P`, `y`, `t`, `h`... one letter per line. The `split()` is what turns letters into words.

---

## Quick Recap

- A **string** is text in quotes. `'...'` and `"..."` are the same; `'''...'''` allows multiple lines.
- **`len()`** gives the length, counting spaces.
- **Indexing starts at 0.** The last character is `len() - 1`, or just `-1`.
- **Negative indexes** count from the end: `-1` is last, `-2` second last. There is no `-0`.
- **Slicing** is `s[start:end:step]` — `start` included, **`end` excluded**, same as `range()`.
- `s[:3]` from the start, `s[3:]` till the end, `s[::2]` every 2nd, **`s[::-1]` reverses**.
- **`+`** joins, **`*`** repeats, **`in`** checks membership and gives `True` / `False`.
- Methods worth knowing: `upper()`, `lower()`, `strip()`, `replace()`, `find()`, `count()`, `startswith()`, `endswith()`. They are all **case-sensitive**, and `find()` returns `-1` when there is no match.
- **`split()`** string → list, **`join()`** list → string. `split()` breaks on spaces by default.
- **f-strings** (`f"... {name} ..."`) are the default way to mix variables into text — no `str()` needed.
- **Strings are immutable.** Methods never edit the original, they return a new string — so write `name = name.upper()`.
