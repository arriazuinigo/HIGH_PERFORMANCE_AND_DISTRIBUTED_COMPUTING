# Recursive Programming - Exercises 1–5

---

## Source Code for the Exercises

---

### Exercise 1:
Implement a recursive function `remainder(n, d)` that computes the remainder of the division of `n` by `d`, using only subtraction and recursive calls.

a. Clearly identify the base case(s).  
b. Clearly state the recursive case.  
c. Compute the time complexity and space complexity in terms of `n` and `d`, and justify your answers.

```python
def remainder(n, d):
    # Base case: if n < d, the remainder is n
    if n < d:
        return n
    # Recursive case: subtract d from n and continue
    else:
        return remainder(n - d, d)

# Test examples
print("remainder(10, 3) =", remainder(10, 3))  # Expected: 1
print("remainder(17, 5) =", remainder(17, 5))  # Expected: 2
print("remainder(20, 4) =", remainder(20, 4))  # Expected: 0
print("remainder(7, 3) =", remainder(7, 3))    # Expected: 1

# Time & Space Complexity: Both O(n/d), since the recursion depth equals
# the number of times we can subtract d from n before n becomes less than d.
```

---

### Exercise 2:
Implement a recursive function `is_palindrome(s)` using Python slicing (e.g., `s[1:-1]`) that returns `True` if `s` is a palindrome and `False` otherwise.

a. Clearly identify the base case(s).  
b. Clearly state the recursive rule.  
c. Compute the time complexity and space complexity (in terms of recursion stack depth) and justify your answers.

```python
### Exercise 2 code:

def is_palindrome(s):
    # Base case 1: empty string is a palindrome
    # Base case 2: single character is always a palindrome
    if len(s) <= 1:
        return True
    # If first and last characters don't match, not a palindrome
    if s[0] != s[-1]:
        return False
    # Recursive case: check the inner substring using slicing s[1:-1]
    return is_palindrome(s[1:-1])

# Test examples
print("is_palindrome('madam') =", is_palindrome("madam"))                  # Expected: True
print("is_palindrome('racecar') =", is_palindrome("racecar"))              # Expected: True
print("is_palindrome('hello') =", is_palindrome("hello"))                  # Expected: False
print("is_palindrome('a') =", is_palindrome("a"))                          # Expected: True
print("is_palindrome('') =", is_palindrome(""))                            # Expected: True
print("is_palindrome('Madam'.lower()) =", is_palindrome("Madam".lower()))  # Expected: True

# --- Complexity Analysis ---
#
# Let n = len(s)
#
# Time Complexity: O(n^2)
#   - There are O(n/2) recursive calls (each call strips 2 characters via s[1:-1]).
#   - Each call to s[1:-1] creates a NEW string copy of size n-2, n-4, ..., 1.
#     Python string slicing is O(k) where k is the length of the new string.
#   - Total work: n + (n-2) + (n-4) + ... + 1  ≈  n^2/4  ->  O(n^2)
#
# Space Complexity: O(n^2)
#   - Call stack depth: O(n/2) = O(n) frames.
#   - Each frame holds a string slice of size n, n-2, n-4, ..., 1.
#   - Total memory across all frames: n + (n-2) + ... + 1  ≈  n^2/4  ->  O(n^2)
#   - Dominant cost is the string copies, NOT just the stack depth.
```

---

### Exercise 3:
The following algorithm is an optimized version of `is_palindrome`. Instead of using slicing, it uses two indices (`left` and `right`) to compare characters from the ends toward the center.

Analyze this implementation and compute its time and space complexity. Explain why it is more efficient than the slicing-based version from Exercise 2.

```python
def is_palindrome(s, lt, rt):
    # Base case
    if lt >= rt:
        return True
    # If mismatch, not a palindrome
    if s[lt] != s[rt]:
        return False
    # Recursive call on inner substring (without slicing)
    return is_palindrome(s, lt + 1, rt - 1)

input_s = "Madam".lower()
left = 0
right = len(input_s) - 1
print(is_palindrome(input_s, left, right))

# --- Complexity Analysis ---
#
# Let n = len(s)
#
# Time Complexity: O(n)
#   - There are at most n/2 recursive calls, each doing O(1) work (index comparison only).
#   - No string copies are created; the original string s is passed by reference.
#   - Total time: O(n)
#
# Space Complexity: O(n)
#   - Call stack depth: O(n/2) = O(n) frames.
#   - Each frame stores only two integer indices (lt, rt) and a reference to s: O(1) per frame.
#   - Total space: O(n) - stack depth only, no string copies.
#
# Why more efficient than Exercise 2:
#   - Exercise 2 creates a new string copy at every recursive call: O(n^2) time and space.
#   - This version passes indices into the same string: O(n) time and O(n) space.
```

---

### Exercise 4:
Given the following code that implements the mutually recursive functions `is_even(n)` and `is_odd(n)`:

a. Complete the code.  
b. Write a short call trace for `is_even(4)` and `is_odd(5)`.  
c. Compute the time complexity and space complexity, and justify your answers.

```python
### Exercise 4 code:

def is_even(n):
    # Base case: 0 is even
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    # Base case: 0 is not odd
    if n == 0:
        return False
    else:
        return is_even(n - 1)

x = is_even(4)   # x is True
y = is_odd(5)    # y is True
print("is_even(4) =", x)
print("is_odd(5)  =", y)


# --- b. Call Traces ---
#
# is_even(4):
#   is_even(4)
#     -> is_odd(3)
#         -> is_even(2)
#             -> is_odd(1)
#                 -> is_even(0)
#                     -> True   <- base case reached
#
# is_odd(5):
#   is_odd(5)
#     -> is_even(4)
#         -> is_odd(3)
#             -> is_even(2)
#                 -> is_odd(1)
#                     -> is_even(0)
#                         -> True   <- base case reached


# --- c. Complexity Analysis ---
#
# Let n be the input value.
#
# Time Complexity: O(n)
#   - Each call reduces n by exactly 1, alternating between is_even and is_odd.
#   - There are exactly n + 1 total function calls before hitting the base case (n == 0).
#   - Each call does O(1) work (one comparison + one recursive call).
#   - Total time = O(n).
#
# Space Complexity: O(n)
#   - The recursion stack grows to depth n + 1 (one frame per call) before unwinding.
#   - Each frame stores only a constant amount of data (the local variable n).
#   - No auxiliary data structures are used.
#   - Total memory is proportional to stack depth: O(n).
```

---

### Exercise 5:
The following function generates all possible k-mers of length `k` from a given list of bases.

a. Explain how the recursion works. Clearly identify the base case and the recursive case.  
b. How many k-mers are generated in terms of `k` and `b` (size of the list of bases)?  
c. Compute the time complexity and justify your answer.  
d. Compute the space complexity and justify your reasoning.

```python
### Exercise 5 code:

def generate_kmers(k, list_bases):
    # Base case: k-mers of length 1 are just the bases themselves
    if k == 1:
        return list_bases
    # Recursive case: get all (k-1)-mers, then extend each by appending every base
    else:
        kmers = []
        prev_kmers = generate_kmers(k - 1, list_bases)
        for mer in prev_kmers:
            for base in list_bases:
                kmers.append(mer + base)
        return kmers

bases = ['A', 'C', 'G', 'T']
k = 2
result = generate_kmers(k, bases)
print("K-mers of length", k, "is:", result)


# --- a. How the recursion works ---
#
# Base case:
#   When k == 1, return list_bases directly.
#   The single-character k-mers are just the bases themselves.
#
# Recursive case:
#   For k > 1, first recursively generate all (k-1)-mers,
#   then extend each one by appending every base in list_bases.
#   This produces all k-mers of length k.


# --- b. Number of k-mers generated ---
#
# Let b = len(list_bases).
# At each level the number of k-mers grows by a factor of b:
#   level 1 -> b^1 k-mers
#   level 2 -> b^2 k-mers
#   level k -> b^k k-mers
#
# Total k-mers = b^k
# Example (DNA: b=4, k=2): 4^2 = 16 k-mers


# --- c. Time Complexity: O(k * b^k) ---
#
# At recursion level i (building i-mers):
#   - There are b^i strings, each of length i.
#   - Appending a base creates a new string of length i: costs O(i) per concatenation.
#   - Total work at level i: b^i * O(i)
#
# Summing over all k levels:
#   sum_{i=1}^{k} i * b^i  ≈  k * b^k   (dominant term)
#
# Time Complexity: O(k * b^k)


# --- d. Space Complexity: O(k * b^k) ---
#
# Call stack depth: k frames -> O(k) stack overhead.
# At each level i, a list of b^i strings of length i is stored in memory.
# All intermediate lists (levels 1 through k) coexist on the call stack
# until the recursion unwinds.
#
# Total memory: sum_{i=1}^{k} i * b^i  ≈  k * b^k
#
# Space Complexity: O(k * b^k)
```
