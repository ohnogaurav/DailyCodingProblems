
#  Sets and Second Largest Element

## What I Learned
- **Set in Python**: A collection of unique, unordered elements.
  - **Usage**: Remove duplicates from lists.
  - **Syntax**: `set(iterable)`
  - **Time Complexity**: O(n) on average for operations like insertion and lookup.

## Example: Remove Duplicates
```python
arr = [4, 5, 4, 7, 8]
unique_arr = list(set(arr))  # [4, 5, 7, 8]
```

## Problem: Find Second Largest Element
### Solution
1. Convert list to set to remove duplicates.
2. Sort the set and access the second last element.
3. Handle cases with less than 2 unique elements.

### Code
```python
arr = list(map(int, input().split()))
arr.sort()
narr = list(set(arr))
try:
    print(narr[-2])
except IndexError:
    print(-1)
```

### Example Input/Output
- Input: `4 5 4 7 8`
- Output: `7`

---

