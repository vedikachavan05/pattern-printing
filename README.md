# ⭐ Python Pattern Printing Assignment

Practice these 12 patterns using nested loops, conditions, and spaces.

## Q1. Solid Square

**Expected Output:**

```
* * * *
* * * *
* * * *
* * * *
```

## Q2. Right-Angled Triangle

**Expected Output:**

```
*
* *
* * *
* * * *
* * * * *
```

## Q3. Inverted Right-Angled Triangle

**Expected Output:**

```
* * * * *
* * * *
* * *
* *
*
```

## Q4. Increasing Number Triangle

**Expected Output:**

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

## Q5. Repeated Row Number Triangle

**Expected Output:**

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

## Q6. Right-Aligned Triangle

**Expected Output:**

```
        *
      * *
    * * *
  * * * *
* * * * *
```

## Q7. Star Pyramid

**Expected Output:**

```
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
```

## Q8. Inverted Star Pyramid

**Expected Output:**

```
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
```

## Q9. Diamond Pattern

**Expected Output:**

```
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
```

## Q10. Hollow Square

**Expected Output:**

```
* * * * *
*       *
*       *
*       *
* * * * *
```

## Q11. Hollow Right-Angled Triangle

**Expected Output:**

```
*
* *
*   *
*     *
* * * * *
```

## Q12. Butterfly Pattern

**Expected Output:**

```
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
```

---

# 💡 Quick Tricks & Logic Revision

### 1. Loop basics

- `i` → Outer loop (rows).
- `j` → Inner loop (columns).
- `print("*", end=" ")` → Stay on the same line.
- `print()` → Move to the next line.

### 2. Loop ranges

| Requirement                      | Range               |
| -------------------------------- | ------------------- |
| Increasing from 0                | `range(n)`          |
| Increasing from 1                | `range(1, n+1)`     |
| Decreasing                       | `range(n, 0, -1)`   |
| Reverse without repeating middle | `range(n-1, 0, -1)` |

### 3. Pattern formulas

| Pattern logic              | Formula   |
| -------------------------- | --------- |
| Increasing stars (0-based) | `i+1`     |
| Increasing stars (1-based) | `i`       |
| Leading spaces             | `n-i`     |
| Pyramid stars              | `2*i-1`   |
| Butterfly middle spaces    | `2*(n-i)` |

### 4. Hollow pattern conditions

**Hollow Square**

- Top: `i == 0`
- Bottom: `i == n-1`
- Left: `j == 0`
- Right: `j == n-1`

**Hollow Triangle**

- Left: `j == 0`
- Right: `j == i`
- Bottom: `i == n-1`

### 5. Important observations

- `i` represents the row; `j` represents the column.
- `range(i+1)` → last value of `j` is `i`.
- `range(i+2)` → last value of `j` is `i+1`.
- Diamond = Pyramid + Inverted Pyramid (without repeating the middle row).
- Butterfly = Two mirrored triangles + middle spaces.
- Hollow pattern = Print stars on boundaries and spaces inside.

**Practice goal:** Understand the loop range, count the stars and spaces, and identify the boundaries before writing the program.
