# Time Complexity Cheat Sheet

## Fastest → Slowest

| Complexity | Name | Example |
|------------|------|---------|
| **O(1)** | Constant | Array access (`arr[i]`) |
| **O(log n)** | Logarithmic | Binary Search |
| **O(√n)** | Square Root | Factor checking |
| **O(n)** | Linear | Single loop |
| **O(n log n)** | Linearithmic | Merge Sort, Heap Sort |
| **O(n²)** | Quadratic | Nested loops |
| **O(n³)** | Cubic | Triple nested loops |
| **O(nᵏ)** | Polynomial | General polynomial algorithms |
| **O(2ⁿ)** | Exponential | Generate all subsets |
| **O(n!)** | Factorial | Generate all permutations |

---

## Easy to Remember

```text
O(1)
 ↓
O(log n)
 ↓
O(√n)
 ↓
O(n)
 ↓
O(n log n)
 ↓
O(n²)
 ↓
O(n³)
 ↓
O(nᵏ)
 ↓
O(2ⁿ)
 ↓
O(n!)
```

---

## Common Examples

### O(1) - Constant
```python
x = arr[3]
```

### O(log n) - Binary Search
Repeatedly divide the search space in half.

### O(n) - Linear
```python
for num in arr:
    print(num)
```

### O(n log n)
- Merge Sort
- Heap Sort
- Average-case Quick Sort

### O(n²) - Quadratic
```python
for i in arr:
    for j in arr:
        print(i, j)
```

### O(2ⁿ) - Exponential
Recursive subset generation.

### O(n!) - Factorial
Generate every permutation of a list.

---

## Interview Tip

Aim for:
- ✅ O(1)
- ✅ O(log n)
- ✅ O(n)
- ✅ O(n log n)

Try to avoid **O(n²)** or worse unless the input size is very small.