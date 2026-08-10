# 🐍 Python String Printing & Formatting

A quick reference for printing strings and inserting values into strings.

---

# 1. `print()` — Display Output

The `print()` function displays information on the screen.

```python
print("Hello World")
```

**Output:**

```text
Hello World
```

You can also print variables:

```python
name = "Colin"

print(name)
```

**Output:**

```text
Colin
```

---

# 2. Printing Multiple Values

Separate values with commas.

```python
name = "Colin"
age = 30

print("Name:", name)
print("Age:", age)
```

**Output:**

```text
Name: Colin
Age: 30
```

You can also put several values in one `print()`:

```python
name = "Colin"
score = 95

print("Name:", name, "Score:", score)
```

**Output:**

```text
Name: Colin Score: 95
```

💡 `print()` automatically adds spaces between values separated by commas.

---

# 3. f-Strings ⭐

**f-strings** are one of the easiest ways to insert variables into a string.

Put `f` before the string:

```python
name = "Colin"

print(f"Hello {name}")
```

**Output:**

```text
Hello Colin
```

The variable goes inside:

```text
{ }
```

### Multiple Variables

```python
name = "Colin"
score = 95

print(f"{name} scored {score} points.")
```

**Output:**

```text
Colin scored 95 points.
```

### Expressions Inside f-Strings

You can also perform calculations:

```python
a = 10
b = 5

print(f"Total: {a + b}")
```

**Output:**

```text
Total: 15
```

---

# 4. `.format()`

Another way to insert values into a string is `.format()`.

```python
name = "Colin"

print("Hello {}".format(name))
```

**Output:**

```text
Hello Colin
```

### Multiple Values

```python
name = "Colin"
score = 95

print("{} scored {} points.".format(name, score))
```

**Output:**

```text
Colin scored 95 points.
```

---

# 5. Numbered `.format()` Placeholders

You can specify which value goes where.

```python
print("{0} likes {1}".format("Colin", "Python"))
```

**Output:**

```text
Colin likes Python
```

The indexes work like a list:

```text
0 → Colin
1 → Python
```

You can reuse them:

```python
print("{0} likes {1}. {0} is learning every day.".format("Colin", "Python"))
```

**Output:**

```text
Colin likes Python. Colin is learning every day.
```

---

# 6. Named `.format()` Placeholders

You can give placeholders names.

```python
print("Name: {name}, Score: {score}".format(name="Colin", score=95))
```

**Output:**

```text
Name: Colin, Score: 95
```

---

# 7. Old `%` String Formatting

Older Python code may use `%`.

### `%s` — String

```python
name = "Colin"

print("Hello %s" % name)
```

**Output:**

```text
Hello Colin
```

### `%d` — Integer

```python
age = 30

print("Age: %d" % age)
```

### Multiple Values

```python
name = "Colin"
score = 95

print("%s scored %d points." % (name, score))
```

**Output:**

```text
Colin scored 95 points.
```

💡 You may see `%` formatting in older HackerRank problems or Python 2 code.

---

# 8. Formatting Decimal Numbers

Suppose:

```python
price = 12.34567
```

To display **2 decimal places** with an f-string:

```python
print(f"{price:.2f}")
```

**Output:**

```text
12.35
```

Using `.format()`:

```python
print("{:.2f}".format(price))
```

**Output:**

```text
12.35
```

---

# 9. Formatting Percentages

```python
score = 0.8567

print(f"{score:.2%}")
```

**Output:**

```text
85.67%
```

---

# 10. Formatting Large Numbers

Use `,` to add thousands separators.

```python
number = 1000000

print(f"{number:,}")
```

**Output:**

```text
1,000,000
```

---

# 11. `sep=` — Change the Separator

Normally:

```python
print("Python", "Java", "C++")
```

**Output:**

```text
Python Java C++
```

Change the separator:

```python
print("Python", "Java", "C++", sep="-")
```

**Output:**

```text
Python-Java-C++
```

Another example:

```python
print("08", "09", "2026", sep="/")
```

**Output:**

```text
08/09/2026
```

---

# 12. `end=` — Change the Ending

Normally, `print()` moves to a new line.

```python
print("Hello")
print("World")
```

**Output:**

```text
Hello
World
```

Using `end=`:

```python
print("Hello", end=" ")
print("World")
```

**Output:**

```text
Hello World
```

---

# 13. Escape Characters

Escape characters start with `\`.

### `\n` — New Line

```python
print("Hello\nWorld")
```

**Output:**

```text
Hello
World
```

### `\t` — Tab

```python
print("Name\tScore")
print("Colin\t95")
```

**Output:**

```text
Name    Score
Colin   95
```

### `\"` — Double Quote

```python
print("He said \"Hello\"")
```

**Output:**

```text
He said "Hello"
```

### `\\` — Backslash

```python
print("C:\\Users\\Colin")
```

**Output:**

```text
C:\Users\Colin
```

---

# 14. Alignment

### Left Align

```python
name = "Python"

print(f"{name:<10}|")
```

```text
Python    |
```

### Right Align

```python
print(f"{name:>10}|")
```

```text
    Python|
```

### Center

```python
print(f"{name:^10}|")
```

```text
  Python  |
```

Remember:

```text
<  Left
>  Right
^  Center
```

---

# 15. HackerRank Example

HackerRank problems often require exact output formatting.

```python
name = "Python"
score = 95

print(f"{name}: {score}")
```

**Output:**

```text
Python: 95
```

Sometimes you may need:

```python
print(name, score)
```

or:

```python
print(name, score, sep=": ")
```

All three approaches can produce different output depending on the formatting requirements.

⚠️ On HackerRank, spaces, newlines, and punctuation matter.

---

# ⭐ Quick Cheat Sheet

| Syntax           | Purpose                        |
| ---------------- | ------------------------------ |
| `print(x)`       | Display output                 |
| `print(a, b)`    | Print multiple values          |
| `f"{x}"`         | Insert value using f-string    |
| `"{}".format(x)` | Insert value using `.format()` |
| `"%s" % x`       | Old-style string formatting    |
| `f"{x:.2f}"`     | 2 decimal places               |
| `f"{x:.2%}"`     | Percentage                     |
| `f"{x:,}"`       | Thousands separator            |
| `sep="-"`        | Change separator               |
| `end=" "`        | Change line ending             |
| `\n`             | New line                       |
| `\t`             | Tab                            |
| `:<10`           | Left align                     |
| `:>10`           | Right align                    |
| `:^10`           | Center                         |

---

# 🧠 Which Formatting Should I Use?

For modern Python, prefer:

```python
name = "Colin"
score = 95

print(f"{name} scored {score}")
```

You should still understand:

```python
"{}".format(value)
```

and:

```python
"%s" % value
```

because you may encounter them in HackerRank exercises and older Python code.

### Easy Way to Remember

```text
Modern Python
f"{variable}"

Older Style
"{}".format(variable)

Old Style / Python 2
"%s" % variable
```
