# Python `itertools`

The `itertools` module is part of Python's **standard library**. It provides functions for creating and working with **iterators** efficiently.

```python
import itertools
```

You can also import individual functions:

```python
from itertools import product, permutations, combinations
```

---

# 1. Infinite Iterators

These functions can continue producing values indefinitely.

## `count()`

Generates numbers starting from a value and continuing by a specified step.

### Syntax

```python
itertools.count(start=0, step=1)
```

### Example

```python
from itertools import count

for num in count(10, 2):
    print(num)

    if num >= 16:
        break
```

Output:

```text
10
12
14
16
```

Think of it as:

```text
start → add step → add step → add step → ...
```

---

## `cycle()`

Repeats the elements of an iterable forever.

### Syntax

```python
itertools.cycle(iterable)
```

### Example

```python
from itertools import cycle

colors = cycle(["red", "green", "blue"])

print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
```

Output:

```text
red
green
blue
red
```

The sequence starts over when it reaches the end.

---

## `repeat()`

Repeats the same object.

### Syntax

```python
itertools.repeat(object, times)
```

### Example

```python
from itertools import repeat

print(list(repeat("Hello", 3)))
```

Output:

```text
['Hello', 'Hello', 'Hello']
```

If `times` is omitted, it repeats forever.

---

# 2. Combinatoric Iterators

These functions create different combinations or arrangements of values.

## `product()`

Creates the **Cartesian product** of iterables.

It pairs every value from one iterable with every value from another.

### Syntax

```python
itertools.product(*iterables, repeat=1)
```

### Example

```python
from itertools import product

a = [1, 2]
b = [3, 4]

print(*product(a, b))
```

Output:

```text
(1, 3) (1, 4) (2, 3) (2, 4)
```

Think of it as nested loops:

```python
for x in a:
    for y in b:
        print((x, y))
```

### Using `repeat`

```python
print(*product([1, 2], repeat=2))
```

Output:

```text
(1, 1) (1, 2) (2, 1) (2, 2)
```

**Remember:**

> `product()` = every possible pairing, like nested `for` loops.

---

## `permutations()`

Creates different **ordered arrangements** of elements.

### Syntax

```python
itertools.permutations(iterable, r=None)
```

### Example

```python
from itertools import permutations

print(*permutations("ABC", 2))
```

Output:

```text
('A', 'B') ('A', 'C') ('B', 'A') ('B', 'C') ('C', 'A') ('C', 'B')
```

Order matters:

```text
(A, B) ≠ (B, A)
```

**Remember:**

> `permutations()` = arrangements where **order matters**.

---

## `combinations()`

Creates unique combinations of a specified length.

### Syntax

```python
itertools.combinations(iterable, r)
```

### Example

```python
from itertools import combinations

print(*combinations("ABC", 2))
```

Output:

```text
('A', 'B') ('A', 'C') ('B', 'C')
```

Notice:

```text
('A', 'B')
```

exists, but:

```text
('B', 'A')
```

does not.

**Remember:**

> `combinations()` = selections where **order does not matter**.

---

## `combinations_with_replacement()`

Works like `combinations()`, but allows an element to be selected more than once.

### Syntax

```python
itertools.combinations_with_replacement(iterable, r)
```

### Example

```python
from itertools import combinations_with_replacement

print(*combinations_with_replacement("ABC", 2))
```

Output:

```text
('A', 'A') ('A', 'B') ('A', 'C') ('B', 'B') ('B', 'C') ('C', 'C')
```

**Remember:**

> `combinations_with_replacement()` = combinations + repeated values allowed.

---

# 3. Iterator-Building Functions

## `accumulate()`

Creates accumulated results.

By default, it calculates running totals.

### Syntax

```python
itertools.accumulate(iterable, func=operator.add, *, initial=None)
```

### Example

```python
from itertools import accumulate

numbers = [1, 2, 3, 4]

print(list(accumulate(numbers)))
```

Output:

```text
[1, 3, 6, 10]
```

Because:

```text
1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

You can also provide another function:

```python
from itertools import accumulate
import operator

print(list(accumulate([1, 2, 3, 4], operator.mul)))
```

Output:

```text
[1, 2, 6, 24]
```

---

## `batched()`

Groups elements into batches of a specified size.

### Syntax

```python
itertools.batched(iterable, n)
```

### Example

```python
from itertools import batched

print(list(batched("ABCDEFG", 3)))
```

Output:

```text
[('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
```

Useful when processing data in chunks.

---

## `chain()`

Combines several iterables into one continuous iterator.

### Syntax

```python
itertools.chain(*iterables)
```

### Example

```python
from itertools import chain

a = [1, 2]
b = [3, 4]

print(list(chain(a, b)))
```

Output:

```text
[1, 2, 3, 4]
```

**Remember:**

> `chain()` = connect iterables together.

---

## `chain.from_iterable()`

Flattens one level of nested iterables.

### Example

```python
from itertools import chain

numbers = [[1, 2], [3, 4], [5, 6]]

print(list(chain.from_iterable(numbers)))
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

---

## `compress()`

Filters data using corresponding true/false selector values.

### Syntax

```python
itertools.compress(data, selectors)
```

### Example

```python
from itertools import compress

letters = ["A", "B", "C", "D"]
selectors = [1, 0, 1, 0]

print(list(compress(letters, selectors)))
```

Output:

```text
['A', 'C']
```

`1` / `True` → keep it
`0` / `False` → skip it

---

## `dropwhile()`

Drops elements while a condition is `True`.

Once the condition becomes `False`, it returns that element and everything after it.

### Example

```python
from itertools import dropwhile

numbers = [1, 2, 3, 6, 2, 1]

print(list(dropwhile(lambda x: x < 5, numbers)))
```

Output:

```text
[6, 2, 1]
```

Important: it does **not** continue filtering later values.

---

## `filterfalse()`

Keeps elements where a condition is `False`.

### Example

```python
from itertools import filterfalse

numbers = [1, 2, 3, 4, 5, 6]

print(list(filterfalse(lambda x: x % 2 == 0, numbers)))
```

Output:

```text
[1, 3, 5]
```

This is roughly the opposite of `filter()`.

---

## `groupby()`

Groups **consecutive** elements that have the same key.

### Example

```python
from itertools import groupby

letters = "AAABBCCAAA"

for key, group in groupby(letters):
    print(key, list(group))
```

Output:

```text
A ['A', 'A', 'A']
B ['B', 'B']
C ['C', 'C']
A ['A', 'A', 'A']
```

Important:

> `groupby()` groups consecutive matching values. It does not automatically collect identical values from different parts of the iterable.

Data is often sorted first when grouping by a key.

---

## `islice()`

Slices an iterator.

It works similarly to:

```python
list[start:stop:step]
```

### Syntax

```python
itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop, step)
```

### Example

```python
from itertools import islice

numbers = range(10)

print(list(islice(numbers, 2, 7)))
```

Output:

```text
[2, 3, 4, 5, 6]
```

Useful because normal slicing does not work with every iterator.

---

## `pairwise()`

Returns consecutive overlapping pairs.

### Example

```python
from itertools import pairwise

numbers = [1, 2, 3, 4]

print(list(pairwise(numbers)))
```

Output:

```text
[(1, 2), (2, 3), (3, 4)]
```

**Remember:**

```text
A B C D
↓ ↓
AB BC CD
```

---

## `starmap()`

Works similarly to `map()`, but automatically unpacks arguments from tuples.

### Example

```python
from itertools import starmap

numbers = [(2, 3), (3, 2), (4, 2)]

print(list(starmap(pow, numbers)))
```

Equivalent to:

```python
pow(2, 3)
pow(3, 2)
pow(4, 2)
```

Output:

```text
[8, 9, 16]
```

---

## `takewhile()`

Keeps elements while a condition remains `True`.

It stops completely when the condition becomes `False`.

### Example

```python
from itertools import takewhile

numbers = [1, 2, 3, 6, 2, 1]

print(list(takewhile(lambda x: x < 5, numbers)))
```

Output:

```text
[1, 2, 3]
```

Compare:

```text
takewhile() → TAKE while True
dropwhile() → DROP while True
```

---

## `tee()`

Creates multiple independent iterators from one iterable.

### Syntax

```python
itertools.tee(iterable, n=2)
```

### Example

```python
from itertools import tee

numbers = [1, 2, 3]

a, b = tee(numbers)

print(list(a))
print(list(b))
```

Output:

```text
[1, 2, 3]
[1, 2, 3]
```

This is useful when you need to iterate over the same input independently.

---

## `zip_longest()`

Works like `zip()`, but continues until the **longest** iterable is exhausted.

### Example

```python
from itertools import zip_longest

a = [1, 2, 3]
b = ["A", "B"]

print(list(zip_longest(a, b)))
```

Output:

```text
[(1, 'A'), (2, 'B'), (3, None)]
```

You can choose another fill value:

```python
print(list(zip_longest(a, b, fillvalue="X")))
```

Output:

```text
[(1, 'A'), (2, 'B'), (3, 'X')]
```

---

# Quick Reference

| Function                          | Purpose                                |
| --------------------------------- | -------------------------------------- |
| `count()`                         | Generate an infinite number sequence   |
| `cycle()`                         | Repeat an iterable forever             |
| `repeat()`                        | Repeat the same value                  |
| `accumulate()`                    | Running calculations/totals            |
| `batched()`                       | Divide values into batches             |
| `chain()`                         | Join multiple iterables                |
| `chain.from_iterable()`           | Flatten one level of nested iterables  |
| `compress()`                      | Filter using selectors                 |
| `dropwhile()`                     | Drop values while condition is true    |
| `filterfalse()`                   | Keep values where condition is false   |
| `groupby()`                       | Group consecutive values               |
| `islice()`                        | Slice an iterator                      |
| `pairwise()`                      | Create consecutive pairs               |
| `starmap()`                       | Map a function over unpacked arguments |
| `takewhile()`                     | Keep values while condition is true    |
| `tee()`                           | Create multiple iterators              |
| `zip_longest()`                   | Zip until the longest iterable ends    |
| `product()`                       | Cartesian product                      |
| `permutations()`                  | Ordered arrangements                   |
| `combinations()`                  | Unordered selections                   |
| `combinations_with_replacement()` | Unordered selections with repeats      |

---

# Functions to Know First for HackerRank

I would learn these first:

```python
product()
permutations()
combinations()
combinations_with_replacement()
```

Then:

```python
groupby()
accumulate()
```

These appear naturally in problems involving combinations, arrangements, grouping, and running calculations.

---

# Easy Memory Trick

```text
product()        → every possible pairing

permutations()   → order matters
                   AB ≠ BA

combinations()   → order does NOT matter
                   AB = BA

combinations_with_replacement()
                 → combinations + repeats allowed

accumulate()     → running result

chain()          → join together

groupby()        → group neighbors

islice()         → slice an iterator

pairwise()       → neighboring pairs

takewhile()      → TAKE while True

dropwhile()      → DROP while True

filterfalse()    → keep False

zip_longest()    → zip to longest
```
