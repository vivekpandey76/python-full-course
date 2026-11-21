# File Handling

Notes for Part 17 of the course. Code first, short explanations, nothing extra.

File handling is how Python stores, reads, updates and manages data in files such as `.txt`, `.csv`, `.json` and `.log`. Variables disappear when the program stops. Files keep the data saved.

---

## 1. `open()`, Modes & `with`

```python
file = open("dummy.txt", "r")
print(file.read())
file.close()
```

`open(filename, mode)` opens a file and gives you a file object. You must call `close()` when you are done, or the file stays locked and unsaved data can be lost.

### Modes

| Mode | Does | File missing? | Old content |
|---|---|---|---|
| `"r"` | read | `FileNotFoundError` | kept |
| `"w"` | write | creates it | **erased** |
| `"a"` | append (add at the end) | creates it | kept |

`"r"` is the default, so `open("dummy.txt")` is the same as `open("dummy.txt", "r")`.

```python
open("nofile.txt", "r")
```

```
FileNotFoundError: [Errno 2] No such file or directory: 'nofile.txt'
```

### `with` — always use it

```python
with open("dummy.txt", "r") as f:
    print(f.read())
# file is closed here automatically
```

`with` closes the file for you when the block ends, even if an error happens inside. No `close()` needed.

**Q → Which mode for: reading a saved report? Saving a fresh report? Adding a new entry to a log?**

| Task | Mode | Why |
|---|---|---|
| Reading a saved report | `"r"` | only reading, the file already exists |
| Saving a fresh report | `"w"` | start clean, old report should be replaced |
| Adding a new entry to a log | `"a"` | keep old entries, add the new one at the end |

> **Common mistake:** using `"w"` for a log file. Every run wipes all the old entries.

---

## 2. Write & Append

```python
with open("dummy.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
```

`write()` does **not** add a new line. Add `\n` yourself, or everything ends up on one line.

**Q → Shopping app: save Milk, Bread, Eggs to `cart.txt`, each on a new line. Run it twice. Why only 3 items?**

```python
products = ["Milk", "Bread", "Eggs"]

with open("cart.txt", "w") as f:
    for item in products:
        f.write(item + "\n")
```

`cart.txt` after running it twice:

```
Milk
Bread
Eggs
```

Only 3 items because `"w"` **erases** the file every time it opens it. The second run wiped the first run's items, then wrote the same 3 again.

**Q → Now add "Butter" to `cart.txt` using `"a"` mode.**

```python
with open("cart.txt", "a") as f:
    f.write("Butter\n")
```

`cart.txt`:

```
Milk
Bread
Eggs
Butter
```

`"a"` keeps the old items and adds `Butter` at the end.

---

## 3. Read

| Method | Returns |
|---|---|
| `f.read()` | the whole file as one string |
| `f.readline()` | the next single line (with `\n`). Returns `""` at the end of the file |
| `f.readlines()` | a list of all lines, e.g. `["Milk\n", "Bread\n", "Eggs\n"]` |
| `for line in f:` | one line at a time |

```python
with open("cart.txt", "r") as f:
    print(f.read())
```

```
Milk
Bread
Eggs
Butter

```

- `line.strip()` removes the `\n` and extra spaces from both ends of a line.
- `for line in f:` is best for big files. `readlines()` loads the whole file into memory at once.
- The file object remembers where it stopped. After `f.read()`, a second `f.read()` gives `""` because you are already at the end.

**Q → Read `cart.txt` and print each item like `Item: Milk`.**

```python
with open("cart.txt", "r") as f:
    for line in f:
        print("Item: " + line.strip())
```

```
Item: Milk
Item: Bread
Item: Eggs
Item: Butter
```

Without `strip()` you get an empty line after every item, because `print()` adds its own new line on top of the `\n` already in the line.

**Q → Print only the first item of `cart.txt` using `readline()`.**

```python
with open("cart.txt", "r") as f:
    print(f.readline().strip())
```

```
Milk
```

Call `readline()` again to get `Bread`, and so on.

**Q → Use `readlines()` to print how many items are in `cart.txt`.**

```python
with open("cart.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    print("Items:", len(lines))
```

```
['Milk\n', 'Bread\n', 'Eggs\n', 'Butter\n']
Items: 4
```

---

## 4. JSON Files

**JSON is how apps and APIs store and send data.** It looks like a Python dictionary. Use the built-in `json` module.

| Function | Does |
|---|---|
| `json.dump(data, f, indent=4)` | save Python data to a file |
| `json.load(f)` | read a file back into Python data |

`indent=4` makes the file readable. Without it, everything is written on one line.

| Python | JSON |
|---|---|
| `dict` | object `{}` |
| `list` | array `[]` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

**Q → Save `{"theme": "dark", "language": "English"}` to `settings.json`. Load it, change theme to `"light"`, and save it again.**

```python
import json

settings = {"theme": "dark", "language": "English"}

# save
with open("settings.json", "w") as f:
    json.dump(settings, f, indent=4)

# load
with open("settings.json", "r") as f:
    settings = json.load(f)

print(type(settings))
print(settings)

# change and save again
settings["theme"] = "light"

with open("settings.json", "w") as f:
    json.dump(settings, f, indent=4)
```

```
<class 'dict'>
{'theme': 'dark', 'language': 'English'}
```

`settings.json`:

```json
{
    "theme": "light",
    "language": "English"
}
```

`json.load()` gives back a real `dict`, so you change it like any dictionary. To update a JSON file: **load → change → dump**. Use `"w"` for the final save so the old content is replaced, not added to.

> **Common mistake:** `json.dump()` / `json.load()` take a file. `json.dumps()` / `json.loads()` (with an **s**) work with a **string**.

---

## 5. Where It's Used in Real Life

| Use | Example |
|---|---|
| File uploads | reading uploaded CSV, Excel or text files |
| Data migration | reading data from one file and moving it into a database |
| Log management | saving errors and debugging information |
| ETL pipelines | **E**xtract data from files, **T**ransform it, **L**oad it into databases |
| Report generation | creating CSV, JSON or text reports |

---

## Quick Revision

- `"r"` read | `"w"` write, **erases** | `"a"` append, keeps old content
- Always use `with open(...) as f:`. It closes the file for you.
- `write()` does not add `\n`. Add it yourself.
- `read()` → string | `readline()` → one line | `readlines()` → list | `for line in f` → best for big files
- `line.strip()` removes the `\n`.
- JSON: `json.dump(data, f, indent=4)` to save, `json.load(f)` to read. Update = load → change → dump.

---

## Interview Questions

**1. What is the difference between `"w"` and `"a"` mode?**

Both create the file if it does not exist. `"w"` erases the old content first. `"a"` keeps it and adds new content at the end.

**2. Why use `with open()` instead of `open()` and `close()`?**

`with` closes the file automatically when the block ends, even if an error happens. With plain `open()`, an error before `close()` leaves the file open.

**3. What is the difference between `read()`, `readline()` and `readlines()`?**

`read()` returns the whole file as one string. `readline()` returns the next line. `readlines()` returns a list of all lines.

**4. How do you read a 10 GB log file without running out of memory?**

Loop over the file object with `for line in f:`. It reads one line at a time. `read()` and `readlines()` load the whole file into memory.

**5. What happens if you open a file that does not exist in `"r"` mode?**

Python raises `FileNotFoundError`. In `"w"` or `"a"` mode the file is created instead.

**6. What is the difference between `json.dump()` and `json.dumps()`?**

`json.dump()` writes Python data into a file. `json.dumps()` returns it as a JSON string. Same for `json.load()` (from a file) and `json.loads()` (from a string).
