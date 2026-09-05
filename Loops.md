# Loops

Notes for Part 6 of the course. Simple explanations, real examples, nothing extra.

---

## 1. Why Loops?

**A loop repeats a block of code so you do not have to write it again and again.**

Printing `"Hello"` five times without a loop:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

Now imagine 1000 times. With a loop it is two lines:

```python
for i in range(5):
    print("Hello")
```

```
Hello
Hello
Hello
Hello
Hello
```

Every loop needs three things:

| Thing | Meaning |
|---|---|
| Start | where the repeating begins |
| Stop | when it should end |
| Move ahead | how it gets to the next turn |

Miss the third one and the loop never ends.

---

## 2. `for`

**Runs the block once for every item it is given.** Use it when the count is known in advance.

```python
name = "PYTHON"

for char in name:
    print(char)
```

```
P
Y
T
H
O
N
```

`char` is just a variable name — it holds one item per turn. The loop ends by itself when the items run out.

Compare it with doing the same thing by hand:

```python
name = "PYTHON"
print(name[0])
print(name[1])
print(name[2])
```

That only works if you already know the length, and it breaks the moment the word changes. The loop does not care.

---

## 3. `range()`

**Generates numbers for a `for` loop. The stop value is never included.**

Three forms:

```python
range(stop)                # 0 up to stop - 1
range(start, stop)         # start up to stop - 1
range(start, stop, step)   # start up to stop - 1, jumping by step
```

```python
for i in range(5):
    print(i, end=" ")
```

```
0 1 2 3 4
```

```python
for i in range(1, 6):
    print(i, end=" ")
```

```
1 2 3 4 5
```

```python
for i in range(1, 10, 2):
    print(i, end=" ")
```

```
1 3 5 7 9
```

> `end=" "` tells `print()` to finish with a space instead of a new line. Default is `end="\n"`.

### Multiplication table

```python
num = int(input("Enter your number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

**Sample run** — user enters `5`:

```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

`range(1, 11)` — not `range(1, 10)`. The stop value is excluded, so to reach 10 you write 11. This is the single most common `range()` mistake.

---

## 4. `while`

**Repeats as long as the condition is `True`.** Use it when the count is *not* known in advance.

```python
i = 1

while i <= 5:
    print(i, end=" ")
    i += 1        # the update line
```

```
1 2 3 4 5
```

The `i += 1` is not optional. Remove it and `i` stays `1`, the condition stays `True`, and the loop runs forever.

### Adding numbers until the user enters 0

```python
num = int(input("Enter your number: "))
total = 0

while num != 0:
    total += num
    num = int(input("Enter your number: "))

print("Total:", total)
```

**Sample run** — user enters `10`, `20`, `5`, `0`:

```
Total: 35
```

**Why not `for` here?** You have no idea how many numbers the user will type. It could be 2, it could be 50. The stop depends on a *condition*, not on a count.

**What if you forget the second `input()` inside the loop?** `num` never changes, the condition stays `True`, and the program hangs. Press `Ctrl + C` to kill it.

---

## 5. `for` vs `while`

| | `for` | `while` |
|---|---|---|
| Use when | count is known | stop depends on a condition |
| Update | automatic | you write it yourself |
| Infinite loop risk | almost none | real |

- "Print marks of 10 students" → `for` (10 is known)
- "Keep asking for the password until it is correct" → `while` (could be 1 try or 20)

---

## 6. Nested Loops

**A loop inside a loop. The inner loop finishes fully for every single turn of the outer loop.**

- **Outer loop** → controls the rows
- **Inner loop** → controls what gets printed in each row

```python
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
```

```
* 
* * 
* * * 
* * * * 
```

Turn by turn:

| Outer `i` | Inner `range(i)` | Row printed |
|---|---|---|
| 1 | 1 turn | `*` |
| 2 | 2 turns | `* *` |
| 3 | 3 turns | `* * *` |
| 4 | 4 turns | `* * * *` |

Two details do the work here:

1. `range(i)` grows with the row number, so each row gets one more star.
2. The bare `print()` sits in the **outer** loop, not the inner one. It ends the row. Indent it one level deeper and every star lands on its own line.

---

## 7. `break`

**Stops the loop immediately and jumps out.**

```python
for i in range(1, 11):
    print(i)
    if i == 5:
        break

print("End")
```

```
1
2
3
4
5
End
```

6 to 10 never ran. `break` exits the loop, not the program — `"End"` still prints.

---

## 8. `continue`

**Skips only the current turn and moves to the next one.**

```python
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")

print()
print("End")
```

```
1 2 4 5 7 8 10 
End
```

3, 6 and 9 are skipped because `i % 3 == 0` for them. The loop itself keeps running — that is the whole difference from `break`.

---

## 9. `pass`

**A placeholder that does nothing.** Used when Python requires a block but the code is not written yet.

An empty block is an error:

```python
for i in range(10):
                    # IndentationError: expected an indented block
print("hello")
```

`pass` fixes it:

```python
for i in range(10):
    pass

print("hello")
```

```
hello
```

It works anywhere a block is required:

```python
if 18 > 20:
    pass
```

The three are easy to mix up:

| Keyword | What it does |
|---|---|
| `pass` | nothing — just fills the block |
| `continue` | skips this turn, loop continues |
| `break` | exits the loop |

---

## 10. Loop `else`

**The `else` block runs only if the loop finished WITHOUT hitting a `break`.**

```python
num = int(input("Enter your number from 1 to 10: "))

for i in range(1, 11):
    if i == num:
        print("Found")
        break
else:
    print("Not Found")
```

**Sample run** — user enters `7`:

```
Found
```

**Sample run** — user enters `50`:

```
Not Found
```

The `else` lines up with `for`, not with `if` — that indentation is what makes it a loop `else`. It saves you from keeping a separate `found = False` flag variable.

---

## Practice 1

Print the sum of the first n numbers.

```python
num = int(input("Enter number: "))
total = 0

for i in range(1, num + 1):
    total += i

print("Sum:", total)
```

**Sample run** — user enters `10`:

```
Sum: 55
```

`num + 1` again — without it the loop stops at 9 and the answer is 45.

> Avoid naming the variable `sum`. That is a built-in function name, and reusing it hides the original.

---

## Practice 2

Reverse a number: `1234` → `4321`.

```python
num = int(input("Enter your number: "))
reverse = 0

while num > 0:
    lastDigit = num % 10
    reverse = reverse * 10 + lastDigit
    num //= 10

print(reverse)
```

**Sample run** — user enters `1234`:

```
4321
```

Two operators from Part 4 do everything: `% 10` pulls off the last digit, `// 10` removes it.

| Turn | `num` | `lastDigit` | `reverse` |
|---|---|---|---|
| 1 | 1234 | 4 | `0 * 10 + 4` = 4 |
| 2 | 123 | 3 | `4 * 10 + 3` = 43 |
| 3 | 12 | 2 | `43 * 10 + 2` = 432 |
| 4 | 1 | 1 | `432 * 10 + 1` = 4321 |

`while` and not `for` — you do not know how many digits the number has.

---

## Practice 3

Count the vowels in a word entered by the user.

```python
name = input("Enter your name: ").lower()
count = 0

for char in name:
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)
```

**Sample run** — user enters `Vivek`:

```
Number of vowels: 2
```

`.lower()` first, otherwise `"A"` would not match `"aeiou"`. `in` checks membership — it reads exactly like English.

---

## Practice 4

Print the reverse pattern:

```
* * * *
* * *
* *
*
```

```python
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

```
* * * * 
* * * 
* * 
* 
```

Same nested loop as section 6 — only the outer `range()` changed. A negative `step` counts down, and `0` as the stop means it ends at `1`.

---

## Quick Recap

- A **loop** repeats a block of code. Every loop needs a start, a stop, and a way to move ahead.
- **`for`** runs once per item. Use it when the count is known.
- **`range(start, stop, step)`** generates numbers for a `for` loop. The **stop value is excluded** — write `range(1, 11)` to reach 10.
- **`while`** repeats while a condition is `True`. Use it when the count is not known.
- A `while` loop needs an **update line** inside it, or it runs forever. `Ctrl + C` stops a runaway program.
- Known count → `for`. Depends on a condition → `while`.
- **Nested loops**: the inner loop finishes completely for every one turn of the outer loop. Outer = rows, inner = what is in each row.
- **`break`** exits the loop immediately. **`continue`** skips only the current turn. **`pass`** does nothing and just fills a required block.
- **Loop `else`** runs only when the loop ended without a `break`. It lines up with `for` / `while`, not with `if`.
- `% 10` gets the last digit, `// 10` removes it — the standard pair for digit-by-digit work.
