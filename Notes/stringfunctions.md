# 🐍 Python String Functions & Methods

A quick reference for common Python string operations.

---

## 1. String Basics

A **string** is a sequence of characters surrounded by quotes.

```python
text = "Hello Python"
name = 'Colin'
```

---

## 2. `len()` — String Length

Returns the number of characters in a string.

```python
text = "Python"

print(len(text))
```

**Output:**

```text
6
```

---

## 3. Change Letter Case

### `.upper()`

Converts all letters to uppercase.

```python
text = "hello"

print(text.upper())
```

**Output:**

```text
HELLO
```

### `.lower()`

Converts all letters to lowercase.

```python
text = "HELLO"

print(text.lower())
```

**Output:**

```text
hello
```

### `.title()`

Capitalizes the first letter of each word.

```python
text = "hello python world"

print(text.title())
```

**Output:**

```text
Hello Python World
```

### `.capitalize()`

Capitalizes only the first character.

```python
text = "hello python"

print(text.capitalize())
```

**Output:**

```text
Hello python
```

---

## 4. Remove Whitespace

### `.strip()`

Removes whitespace from both sides.

```python
text = "  Python  "

print(text.strip())
```

**Output:**

```text
Python
```

### `.lstrip()`

Removes whitespace from the left side.

```python
text = "  Python"

print(text.lstrip())
```

### `.rstrip()`

Removes whitespace from the right side.

```python
text = "Python  "

print(text.rstrip())
```

---

## 5. `.replace()` — Replace Characters or Words

```python
text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)
```

**Output:**

```text
I like Python
```

---

## 6. `.split()` — String → List

Splits a string into pieces.

```python
text = "apple,banana,orange"

fruits = text.split(",")

print(fruits)
```

**Output:**

```text
['apple', 'banana', 'orange']
```

### HackerRank Example

```python
numbers = input().split()

print(numbers)
```

Input:

```text
10 20 30
```

Result:

```text
['10', '20', '30']
```

⚠️ `input().split()` returns **strings**, not integers.

To get integers:

```python
numbers = list(map(int, input().split()))
```

---

## 7. `.join()` — List → String

Joins multiple strings together.

```python
words = ["Hello", "Python", "World"]

result = " ".join(words)

print(result)
```

**Output:**

```text
Hello Python World
```

### Easy Way to Remember

```text
split()
String → List

join()
List → String
```

---

## 8. `.find()` — Find a Character or Word

Returns the index where the value first appears.

```python
text = "Hello Python"

print(text.find("Python"))
```

**Output:**

```text
6
```

If the value does not exist:

```python
print(text.find("Java"))
```

**Output:**

```text
-1
```

---

## 9. `.count()` — Count Occurrences

```python
text = "banana"

print(text.count("a"))
```

**Output:**

```text
3
```

---

## 10. Check the Beginning or Ending

### `.startswith()`

```python
filename = "notes.txt"

print(filename.startswith("notes"))
```

**Output:**

```text
True
```

### `.endswith()`

```python
filename = "notes.txt"

print(filename.endswith(".txt"))
```

**Output:**

```text
True
```

---

# 🔎 String Checking Methods

These methods return either:

```text
True
```

or

```text
False
```

---

## 11. `.isalpha()` — Letters Only

```python
text = "Python"

print(text.isalpha())
```

**Output:**

```text
True
```

But:

```python
"Python3".isalpha()
```

returns:

```text
False
```

---

## 12. `.isdigit()` — Digits Only

```python
number = "12345"

print(number.isdigit())
```

**Output:**

```text
True
```

---

## 13. `.isalnum()` — Letters and Numbers

```python
text = "Python123"

print(text.isalnum())
```

**Output:**

```text
True
```

---

## 14. `.islower()` and `.isupper()`

```python
print("python".islower())
# True

print("PYTHON".isupper())
# True
```

---

# ✂️ String Indexing

Each character has an index.

```text
 P  y  t  h  o  n
 0  1  2  3  4  5
```

You can access individual characters:

```python
word = "Python"

print(word[0])
print(word[1])
print(word[-1])
```

**Output:**

```text
P
y
n
```

💡 `-1` means the **last character**.

---

# ✂️ String Slicing

Syntax:

```python
string[start:end]
```

Example:

```python
word = "Python"

print(word[0:3])
```

**Output:**

```text
Pyt
```

Remember:

```text
Start = included
End   = NOT included
```

### From a Position to the End

```python
print(word[2:])
```

**Output:**

```text
thon
```

### Reverse a String

```python
print(word[::-1])
```

**Output:**

```text
nohtyP
```

---

# 🔍 Check if Text Exists

Use `in`:

```python
text = "I am learning Python"

if "Python" in text:
    print("Found Python")
```

You can also use `not in`:

```python
if "Java" not in text:
    print("Java was not found")
```

---

# ⭐ HackerRank String Cheat Sheet

| Operation         | Purpose                       |
| ----------------- | ----------------------------- |
| `len(s)`          | Get string length             |
| `s.upper()`       | Uppercase                     |
| `s.lower()`       | Lowercase                     |
| `s.title()`       | Title case                    |
| `s.capitalize()`  | Capitalize first character    |
| `s.strip()`       | Remove surrounding whitespace |
| `s.replace(a, b)` | Replace text                  |
| `s.split()`       | String → list                 |
| `" ".join(items)` | List → string                 |
| `s.find(x)`       | Find index                    |
| `s.count(x)`      | Count occurrences             |
| `s.startswith(x)` | Check beginning               |
| `s.endswith(x)`   | Check ending                  |
| `s.isalpha()`     | Letters only?                 |
| `s.isdigit()`     | Digits only?                  |
| `s.isalnum()`     | Letters/numbers only?         |
| `s.islower()`     | Lowercase?                    |
| `s.isupper()`     | Uppercase?                    |
| `s[index]`        | Get one character             |
| `s[start:end]`    | Slice string                  |
| `s[::-1]`         | Reverse string                |
| `x in s`          | Check whether value exists    |

---

# 🧠 Important Difference

## Function

A function receives the string as an argument.

```python
len(text)
```

## String Method

A method comes after the string using `.`

```python
text.upper()
text.lower()
text.split()
text.strip()
```

Think:

```text
FUNCTION
len(text)

METHOD
text.upper()
     ↑
     dot
```

---

# 🎯 Practice

Given:

```python
text = "  hello python  "
```

Try to produce:

```text
HELLO PYTHON
```

One solution:

```python
text = "  hello python  "

text = text.strip()
text = text.upper()

print(text)
```

Or:

```python
print(text.strip().upper())
```

This is called **method chaining**.
