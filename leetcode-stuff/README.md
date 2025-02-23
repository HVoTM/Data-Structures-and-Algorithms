# NOTES ON LEETCODE, WHITEBOARD-CODING INTERVIEW, and EVERYTHING WITH TECHNICAL INTERVIEW
- If you are working on preparing some coding questions for the Company that you want to get into, follow [this github repo](https://github.com/xizhang20181005/Leetcode_company_frequency
)

# Common built-in Python methods to use

## List Comprehension
**Syntax**: newlist = [*expression* for *item* in *iterable** if *condition == True*]

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

# else - if 
newlist = [x if x != "banana" else "orange" for x in fruits]

# Other use cases
"Iterable"
newlist = [x for x in range(10)]
```
## Strings/ arrays
- [Python's string methods](https://docs.python.org/2/library/stdtypes.html#string-methods)
- ord() : 
    + input: string, character
    + output: return the integet that represents that character in Unicode format

- reverse array: arr[::-1]

- [enumerate()](https://www.geeksforgeeks.org/enumerate-in-python/): 

- `isalpha()`, `isnumeric()`, `isalnum()`, `isdigit()`
    + `isdigit()`, `isnumeric()`
    + 

- **NOTEWORTHY**: returning a reverse array by using : `arr[::-1]`
    + explanation: Python slice behavior so `arr[start_index : stop_index : increment]`

- `pop()`: pop the i-th-indexed value with `nums.pop(i)`

- `lower()`, `upper()`, 

- `strip()`, `replace()`, `split()`, `join()`

- `zip()`

## Other mapping functions
- `filter()`

- `map()`

- `reduce()`

## math built-in library
- `ceil(), floor(), sum()`

## Python's dictionary
- `items()`
- `values()`
- `keys()`

## Python's set
- `get()`

## Python's tuple
- Tuple Comparison: https://stackoverflow.com/questions/5292303/how-does-tuple-comparison-work-in-python
    + in short, tuples are compared position by position, the first item of the first tuple is compared to the first item of the second tuple; if they are equal, then consider the second item, and so on
## Python's collections

## [Python's heapq](https://docs.python.org/3/library/heapq.html)
- `heapify()`: 
- `heappop()`: used to pop the top value (root)
- `heappush()`: used to insert a new value into the binary heap

## functools
- lru_cache: used in memoization for dynamic programming
```py
@lru_cache(None)
def dynamic_prog_solver():

```
## Python Keywords - https://www.w3schools.com/python/python_ref_keywords.asp
- break
- continue
- pass
- for, in, 


## Pandas/DataFrame
- head()
- drop_duplicates(subset=[], keep=)
- dropna(subset=[])
- [`df.rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html)
- fillna()
- concat()

# Resources
- NeetCode's LeetCode solution reference
https://github.com/neetcode-gh/leetcode/tree/main
- LeetCode Company Interview questions
https://github.com/xizhang20181005/Leetcode_company_frequency
