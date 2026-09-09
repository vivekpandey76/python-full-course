# Lists

Notes for Part 8 of the course. Code first, short explanations, nothing extra.

---

## 1. What is a List?

**A list stores many values in one variable, written inside `[ ]`.**

```python
marks = [90, 85, 70]
empty = []
mixed = [1, "vivek", 3.5, True]      # allowed, but normally keep one type

print(marks)
print(len(marks))
```

```
[90, 85, 70]
3
```

Items are comma separated, the order is fixed, and duplicates are allowed.

**Q → Make a list of your 3 favourite movies, print the list and its length.**

```python
movies = ["Bahubali", "Bahubali 2", "Mirzapur"]
print(movies)
print(len(movies))
```

```
['Bahubali', 'Bahubali 2', 'Mirzapur']
3
```

---

## 2. Accessing Items (Indexing)

**Same rule as strings — counting starts at 0.**

```python
fruits = ["apple", "banana", "cherry", "mango"]
#            0         1         2        3
#           -4        -3        -2       -1

print(fruits[0])
print(fruits[-1])
```

```
apple
mango
```

Going past the end is an error:

```python
print(fruits[10])
```

```
IndexError: list index out of range
```

**Q → Print the first and the last item of a list without using `len()`.**

```python
names = ["Vivek", "virat", "vishal", "vikas", "virat"]
print(names[0])
print(names[-1])
```

```
Vivek
virat
```

`-1` is why you never need `len()` for the last item.

---

## 3. Slicing

**`list[start : end : step]` — `start` included, `end` never included.**

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:4])      # index 1, 2, 3
print(nums[:3])       # from the start
print(nums[3:])       # till the end
print(nums[::2])      # every 2nd item
print(nums[::-1])     # reversed
```

```
[20, 30, 40]
[10, 20, 30]
[40, 50]
[10, 30, 50]
[50, 40, 30, 20, 10]
```

Slicing gives a **new** list. The original is untouched.

**Q → From `[10, 20, 30, 40, 50]` print the middle three items, then the full list reversed.**

```python
nums = [10, 20, 30, 40, 50]
print(nums[1:4])
print(nums[::-1])
```

```
[20, 30, 40]
[50, 40, 30, 20, 10]
```

---

## 4. Lists are Mutable

**This is the big difference from strings: a list can be changed after it is created.**

```python
name = "Vivek"
name[0] = "P"
```

```
TypeError: 'str' object does not support item assignment
```

The same thing on a list just works:

```python
names = ["Vivek", "virat", "vishal"]
names[1] = "virat kohli"
print(names)
```

```
['Vivek', 'virat kohli', 'vishal']
```

**Q → Make a list of 3 subjects and replace the 2nd one.**

```python
subjects = ["English", "Hindi", "Marathi"]
subjects[1] = "Science"
print(subjects)
```

```
['English', 'Science', 'Marathi']
```

---

## 5. Adding Items

| Method | What it does |
|---|---|
| `append(x)` | adds **one** item at the end |
| `insert(i, x)` | adds `x` at position `i` |
| `extend([a, b])` | adds **all** items of another list |

```python
names = ["Vivek", "virat", "vishal"]

names.append("vikas")
names.insert(1, "Mukul")
names.extend(["Gaurav", "Pravesh"])

print(names)
```

```
['Vivek', 'Mukul', 'virat', 'vishal', 'vikas', 'Gaurav', 'Pravesh']
```

### `append` vs `extend`

```python
nums = [1, 2, 3]
nums.append([4, 5])
print(nums)

nums = [1, 2, 3]
nums.extend([4, 5])
print(nums)
```

```
[1, 2, 3, [4, 5]]
[1, 2, 3, 4, 5]
```

`append` puts the **whole list inside** as one item. `extend` adds the items **separately**.

**Q → Start with an empty list, take 3 numbers from the user in a loop and append them.**

```python
numbers = []

for i in range(3):
    num = int(input("Enter number: "))
    numbers.append(num)

print(numbers)
```

**Sample run** — user enters `10`, `20`, `30`:

```
[10, 20, 30]
```

---

## 6. Removing Items

| Method | Works on | What it does |
|---|---|---|
| `remove(x)` | **value** | removes the first matching value, error if not found |
| `pop()` | index | removes the last item **and returns it** |
| `pop(i)` | index | removes the item at index `i` |
| `del list[i]` | index | deletes by index |
| `clear()` | — | empties the list |

```python
names = ["Vivek", "virat", "vishal", "vikas", "virat"]

names.remove("virat")     # only the FIRST virat goes
print(names)

last = names.pop()
print(last)
print(names)

del names[1]
print(names)

names.clear()
print(names)
```

```
['Vivek', 'vishal', 'vikas', 'virat']
virat
['Vivek', 'vishal', 'vikas']
['Vivek', 'vikas']
[]
```

`remove()` works on the **value**, `pop()` and `del` work on the **index**. That is the only thing people mix up here.

**Q → From `["a","b","c","d"]` remove `"b"` by value and remove the last item using `pop()`.**

```python
x = ["a", "b", "c", "d"]
x.remove("b")
x.pop()
print(x)
```

```
['a', 'c']
```

---

## 7. Important List Methods

```python
names = ["Vivek", "virat", "vishal", "vikas", "virat"]

print(names.count("virat"))     # how many times
print(names.index("virat"))     # position of the first one
print("Vivek" in names)         # membership -> True / False
```

```
2
1
True
```

`index()` gives an error if the value is not there, so `in` is the safe way to check first:

```python
if "Vishal" in names:
    print("Yes it belongs")
```

Number-only lists get three more:

```python
numbers = [10, 9, 87, 45]

print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

```
87
9
151
```

`reverse()` flips the **original** list — it does not return a new one:

```python
numbers.reverse()
print(numbers)
```

```
[45, 87, 9, 10]
```

**Q → From `marks = [45, 90, 78, 90]` print highest, lowest, total, average, and how many times 90 appears.**

```python
marks = [45, 90, 78, 90]

print(max(marks))
print(min(marks))
print(sum(marks))
print(sum(marks) / len(marks))
print(marks.count(90))
```

```
90
45
303
75.75
2
```

---

## 8. Sorting

```python
numbers = [10, 9, 87, 45]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
```

```
[9, 10, 45, 87]
[87, 45, 10, 9]
```

`sorted()` leaves the original alone and hands back a new list:

```python
numbers = [10, 9, 87, 45]
sortedList = sorted(numbers)

print(sortedList)
print(numbers)
```

```
[9, 10, 45, 87]
[10, 9, 87, 45]
```

> **Common mistake:** `numbers = numbers.sort()` makes `numbers` become `None`. `sort()` changes the list and returns nothing — never assign its result.

Sorting works on strings too (A to Z), but a mixed list like `[1, "a"]` gives a `TypeError`.

---

## 9. Nested Lists

**A list inside a list. Read it as `[row][column]`.**

```python
matrix = [[1, 2, 3], [4, 5, 6]]

print(matrix[0])
print(matrix[0][1])
print(matrix[1][2])
```

```
[1, 2, 3]
2
6
```

---

## 10. List Copying

**`b = a` is not a copy.** Both names point to the same list, so changing one changes both:

```python
a = [10, 20, 30, 40]
b = a
b[1] = 35

print(a)
print(b)
```

```
[10, 35, 30, 40]
[10, 35, 30, 40]
```

Three ways to make a **real** copy:

```python
x = [10, 20, 30, 40]

y = x.copy()
z = list(x)
w = x[:]

y[1] = 35
z[1] = 98

print(x)
print(y)
print(z)
```

```
[10, 20, 30, 40]
[10, 35, 30, 40]
[10, 98, 30, 40]
```

`x` never moved. That is the difference between a copy and a second name.

---

## 11. List Comprehension

**A short way to build a list in one line.**

```
[ expression for item in iterable if condition ]
```

```python
squares = [i * i for i in range(1, 6)]
print(squares)

nums = [1, 2, 3, 4, 5, 6]
evens = [i for i in nums if i % 2 == 0]
print(evens)
```

```
[1, 4, 9, 16, 25]
[2, 4, 6]
```

It is the same as a `for` loop with `append()`, only shorter. Use it while it still reads like English — not for everything.

**Q → From 1 to 20 make a list of numbers divisible by 3, once with a `for` loop and once with a comprehension.**

```python
numbers = []
for i in range(1, 21):
    if i % 3 == 0:
        numbers.append(i)

print(numbers)

numbers = [i for i in range(1, 21) if i % 3 == 0]
print(numbers)
```

```
[3, 6, 9, 12, 15, 18]
[3, 6, 9, 12, 15, 18]
```

Four lines became one. Same output.

---

## Practice 1 — Second Largest Number

Find the second largest number in a list, **without using `sort()`**.

```python
numbers = [10, 20, 4, 45, 45, 99]

largest = float("-inf")
secondLargest = float("-inf")

for num in numbers:
    if num > largest:
        secondLargest = largest
        largest = num
    elif num > secondLargest and num != largest:
        secondLargest = num

print(largest)
print(secondLargest)
```

```
99
45
```

Walk the list once holding two values. When a new biggest shows up, the old biggest slides down into second place. The `num != largest` is what stops a duplicate `45` from filling both slots.

`float("-inf")` is just "smaller than any number", so the very first item always wins the first comparison.

> **Do not start with `largest = numbers[0]` and `secondLargest = numbers[0]`.** On a list that is already descending, like `[99, 45, 10]`, both start at `99` and `45` never gets past the `> secondLargest` check — you would print `99` twice.

---

## Practice 2 — Remove Duplicates, Keep the Order

```python
numbers = [1, 2, 2, 3, 1, 4]
updatedNumbers = []

for num in numbers:
    if num not in updatedNumbers:
        updatedNumbers.append(num)

print(updatedNumbers)
```

```
[1, 2, 3, 4]
```

Start with an **empty** list, loop through the original, and append an item only if it is `not in` the new list. The order survives because you append in the order you meet them.

---

## Quick Recap

- **`[ ]`** makes a list. Index starts at **0**, last item is **`-1`**.
- **Slicing** `list[start:end:step]` — `end` excluded. `[::-1]` reverses. Slicing returns a **new** list.
- **Lists are mutable**, strings are not. `list[0] = x` works, `string[0] = x` is a `TypeError`.
- **`append()`** one item, **`extend()`** many items, **`insert(i, x)`** at a position.
- **`remove()`** by value, **`pop()`** and **`del`** by index. `clear()` empties it.
- **`count()`**, **`index()`**, **`in`**, and `max()` / `min()` / `sum()` on number lists.
- **`sort()`** changes the original and returns `None`. **`sorted()`** returns a new list.
- **`reverse()`** changes the original, `[::-1]` gives a new list.
- **`b = a` is not a copy** — use `a.copy()`, `list(a)`, or `a[:]`.
- **`[x for x in list if condition]`** is a loop + `append()` in one line.
