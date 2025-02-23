# Common concepts to unentangle during coding interviews

## Defining the range for sliding window in Python

The reason for defining the range as `range(len(s) + 1 - k)` instead of just `range(len(s) - k)` has to do with how Python's slicing and range mechanics work. Let’s break this down step by step mathematically.

### 1. Length of the String
Suppose the length of the string $s$ is $n$, i.e., $n = \text{len}(s)$.

### 2. Length of Each Substring
We are considering substrings of length \$k $.

### 3. Last Valid Starting Index
To extract a substring of length $ k $ from $ s $, the starting index $ i$ must satisfy:

$$
i + k \leq n
$$

This ensures that the substring does not extend beyond the end of the string. Rearranging the inequality:

$$
i \leq n - k
$$

This means the last valid starting index is $ n - k$. But as we compute that, we only leave out the valid sub-array/subtring/window of the last starting index with that index. With Python, indexing starts from 0 so we need to increment it by 1

$$
n - k + 1 = \text{len}(s) + 1 - k
$$

This ensures that the loop iterates over all valid starting indices, from $ 0 $ to $ n - k$ inclusive.

### 4. Why Not `len(s) - k`?
If you write `range(len(s) - k)`, the range would generate indices from $ 0 $ to $ n - k - 1 $, which would exclude the last valid starting index $ n - k $. Therefore, the loop would miss the last substring of length $ k $, leading to incorrect results.

### Example
Consider $ s = "hello" $ and $ k = 2 $:

- $ \text{len}(s) = 5 $
- Last valid starting index: $ n - k = 5 - 2 = 3 $

If you use `range(len(s) - k)`, the range is `range(3)`, generating indices $ 0, 1, 2 $, and skipping the last valid index $ 3 $.

If you use `range(len(s) + 1 - k)`, the range is `range(4)`, generating indices $ 0, 1, 2, 3 $, correctly covering all valid starting indices.

### Correctness
Thus, to ensure all substrings of length $ k $ are considered, the loop must iterate over the range:

$$
\text{range(len(s) + 1 - k)}
$$