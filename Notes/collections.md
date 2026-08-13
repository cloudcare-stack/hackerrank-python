# Python `collections` Module

The `collections` module provides specialized container data types that extend Python's built-in containers such as `dict`, `list`, and `tuple`.

## Import

```python
import collections
```

Or import a specific tool:

```python
from collections import Counter
```

---

# 1. `Counter`

`Counter` counts how many times each item appears.

```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]

count = Counter(numbers)

print(count)
```

Output:

```text
Counter({3: 3, 2: 2, 1: 1})
```

Think of a `Counter` like a dictionary:

```python
{
    1: 1,
    2: 2,
    3: 3
}
```

The **key** is the item.

The **value** is how many times the item appears.

### Access a Count

```python
print(count[3])
```

Output:

```text
3
```

If the item does not exist, `Counter` returns `0` instead of an error:

```python
print(count[10])
```

Output:

```text
0
```

---

## Updating a Counter

Add counts:

```python
count.update([2, 3, 3])
```

Subtract counts:

```python
count.subtract([2, 3])
```

---

## Useful Counter Methods

### `.most_common()`

Returns the most common elements:

```python
count.most_common()
```

Get the two most common:

```python
count.most_common(2)
```

### `.elements()`

Returns elements repeated according to their counts:

```python
list(count.elements())
```

### `.total()`

Returns the total of all counts:

```python
count.total()
```

---

# 2. `defaultdict`

A `defaultdict` automatically creates a default value when a missing key is accessed.

```python
from collections import defaultdict

scores = defaultdict(int)

scores["Alice"] += 10
scores["Bob"] += 5
```

Instead of raising a `KeyError`, missing integer values start at:

```text
0
```

Common defaults:

```python
defaultdict(int)   # 0
defaultdict(list)  # []
defaultdict(set)   # set()
```

Example:

```python
groups = defaultdict(list)

groups["A"].append("Alice")
groups["A"].append("Alex")
groups["B"].append("Bob")
```

---

# 3. `deque`

`deque` means **double-ended queue**.

It allows fast additions and removals from both ends.

```python
from collections import deque

numbers = deque([1, 2, 3])
```

Add to the right:

```python
numbers.append(4)
```

Add to the left:

```python
numbers.appendleft(0)
```

Remove from the right:

```python
numbers.pop()
```

Remove from the left:

```python
numbers.popleft()
```

Other useful methods:

```python
numbers.extend([4, 5])
numbers.extendleft([-1, 0])
numbers.rotate(1)
numbers.rotate(-1)
numbers.clear()
```

---

# 4. `namedtuple`

`namedtuple` creates tuple-like objects whose values can be accessed by name.

```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "grade"])

student = Student("Alice", 95)
```

Access using indexes:

```python
student[0]
student[1]
```

Or use names:

```python
student.name
student.grade
```

This makes the code easier to read.

---

# 5. `ChainMap`

`ChainMap` combines multiple dictionaries into one searchable view.

```python
from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

combined = ChainMap(dict1, dict2)

print(combined["a"])
print(combined["c"])
```

The dictionaries remain separate, but `ChainMap` lets you search them together.

---

# Quick Reference

| Collection    | Purpose                                  |
| ------------- | ---------------------------------------- |
| `Counter`     | Count occurrences of items               |
| `defaultdict` | Dictionary with automatic default values |
| `deque`       | Fast queue/stack from both ends          |
| `namedtuple`  | Tuple with named fields                  |
| `ChainMap`    | Search multiple dictionaries together    |

---

# HackerRank Example — `Counter`

For the shoe-shop problem:

```python
from collections import Counter

shoes = int(input())

sizes = Counter(map(int, input().split()))

customers = int(input())

earnings = 0

for _ in range(customers):
    size, price = map(int, input().split())

    if sizes[size] > 0:
        earnings += price
        sizes[size] -= 1

print(earnings)
```

## How It Works

This line:

```python
sizes = Counter(map(int, input().split()))
```

converts the shoe sizes into counts.

For example:

```text
2 3 4 5 6 6 6 7
```

becomes approximately:

```python
Counter({
    6: 3,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    7: 1
})
```

Then:

```python
if sizes[size] > 0:
```

checks whether that shoe size is still available.

If it is sold:

```python
earnings += price
sizes[size] -= 1
```

The money is added to the earnings, and the inventory for that shoe size decreases by one.

---

# Easy Way to Remember

```text
Counter     → count things
defaultdict → automatic defaults
deque       → add/remove from both ends
namedtuple  → tuple with names
ChainMap    → combine dictionary views
```
