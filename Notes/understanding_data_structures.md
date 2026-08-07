# Understanding Data Structures

Data structures are ways to organize and store data so it can be accessed and modified efficiently. Python provides several built-in data structures that are easy to use.

---

# Lists

A **list** is an ordered collection of items. Lists are mutable, meaning you can change, add, or remove items after the list is created.

### Creating a List

```python
fruits = ["apple", "banana", "orange"]
```

### Accessing Items

```python
print(fruits[0])      # apple
print(fruits[-1])     # orange
```

### Adding Items

```python
fruits.append("grape")
print(fruits)
```

Output:

```
['apple', 'banana', 'orange', 'grape']
```

### Removing Items

```python
fruits.remove("banana")
print(fruits)
```

### Useful List Methods

| Method | Description |
|---------|-------------|
| append() | Adds an item to the end |
| insert() | Inserts an item at a specific position |
| remove() | Removes an item by value |
| pop() | Removes an item by index |
| sort() | Sorts the list |
| reverse() | Reverses the list |
| len() | Returns the number of items |

---

# Tuples

A **tuple** is similar to a list, but it is immutable. Once created, it cannot be changed.

### Creating a Tuple

```python
coordinates = (10, 20)
```

### Accessing Values

```python
print(coordinates[0])
```

Output

```
10
```

### Why Use Tuples?

- Store data that should not change
- Faster than lists
- Can be used as dictionary keys

Example:

```python
person = ("Colin", 28, "Arizona")
```

---

# Sets

A **set** stores unique values. Duplicate values are automatically removed.

### Creating a Set

```python
numbers = {1, 2, 3, 3, 4}
print(numbers)
```

Output

```
{1, 2, 3, 4}
```

### Adding Values

```python
numbers.add(5)
```

### Removing Values

```python
numbers.remove(2)
```

### Common Operations

```python
A = {1,2,3}
B = {3,4,5}

print(A | B)   # Union
print(A & B)   # Intersection
print(A - B)   # Difference
```

Output

```
{1,2,3,4,5}
{3}
{1,2}
```

---

# Dictionaries

A **dictionary** stores data as key-value pairs.

### Creating a Dictionary

```python
student = {
    "name": "Colin",
    "age": 28,
    "major": "Computer Science"
}
```

### Accessing Values

```python
print(student["name"])
```

Output

```
Colin
```

### Adding or Updating

```python
student["gpa"] = 3.8
student["age"] = 29
```

### Looping Through a Dictionary

```python
for key, value in student.items():
    print(key, value)
```

### Useful Dictionary Methods

| Method | Description |
|---------|-------------|
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| get() | Gets a value safely |
| pop() | Removes a key |

---

# Boolean Variables

A **Boolean** has only two possible values:

- True
- False

### Examples

```python
is_student = True
has_job = False

print(is_student)
print(has_job)
```

### Comparison Operators

```python
print(5 > 3)
print(10 == 5)
print(8 != 4)
```

Output

```
True
False
True
```

### Logical Operators

```python
print(True and False)
print(True or False)
print(not True)
```

Output

```
False
True
False
```

---

# Combining Data Structures

Python data structures can be combined together.

### List of Dictionaries

```python
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 21}
]

print(students[0]["name"])
```

Output

```
Alice
```

---

### Dictionary with Lists

```python
classroom = {
    "students": ["Alice", "Bob", "Charlie"],
    "teacher": "Mrs. Smith"
}

print(classroom["students"][1])
```

Output

```
Bob
```

---

### Dictionary of Lists

```python
grades = {
    "Math": [90, 85, 88],
    "Science": [95, 91, 87]
}

print(grades["Math"])
```

Output

```
[90, 85, 88]
```

---

### Nested Dictionaries

```python
employee = {
    "name": "John",
    "address": {
        "city": "Phoenix",
        "state": "Arizona"
    }
}

print(employee["address"]["city"])
```

Output

```
Phoenix
```

---

# Summary

| Data Structure | Ordered | Mutable | Allows Duplicates | Syntax |
|---------------|---------|---------|-------------------|--------|
| List | ✅ Yes | ✅ Yes | ✅ Yes | `[]` |
| Tuple | ✅ Yes | ❌ No | ✅ Yes | `()` |
| Set | ❌ No | ✅ Yes | ❌ No | `{}` |
| Dictionary | ✅ Keys | ✅ Yes | Keys: ❌ Values: ✅ | `{key: value}` |

---

# When to Use Each

- **List** → A collection that changes over time.
- **Tuple** → Data that should never change.
- **Set** → Remove duplicates or perform set operations.
- **Dictionary** → Store related information using keys.
- **Boolean** → Make decisions with `if`, `while`, and comparisons.