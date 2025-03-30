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

- reverse array: arr[::-1] // explained: start:default, step: default, step: -1, so move back

- [enumerate()](https://www.geeksforgeeks.org/enumerate-in-python/): 

- `isalpha()`, `isnumeric()`, `isalnum()`, `isdigit()`
    + `isdigit()`, `isnumeric()`
    + 

- **NOTEWORTHY**: returning a reverse array by using : `arr[::-1]`
    + explanation: Python slice behavior so `arr[start_index : stop_index : increment]`

- `pop()`: pop the i-th-indexed value with `nums.pop(i)`

- `lower()`, `upper()`: changing lowercase or uppercase of the strings

- `strip()`, `replace()`, `join()`

- [`split()`](https://docs.python.org/3/library/stdtypes.html#str.split): returns a list of words in a string, using *sep* as the delimiter string. Default of sep is a single space
```py
'1,2,3'.split(',')
```
- `zip()`: returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together
    + Syntax: `zip(iterator1, iterator2, iterator3, ...)`
    + example:
        ```py
        a = ("John", "Charles", "Mike")
        b = ("Jenny", "Christy", "Monica", "Vicky")

        x = zip(a, b)
        ```

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

### [defaultdict](https://www.geeksforgeeks.org/defaultdict-in-python/#)
- A Container-like dictionaries present in the module collections
- Difference with the normal python's dictionaries: provides a default value for the key that does not exist and never raise a KeyError
- **Syntax**: collections.defaultdict(*defaul_factory*)
    - __*default_factory*__: function returning the default valuye for the dictionary. Factory function could be int, list, str, or any other callable oject

```py
from collections import defaultdict
 
# Defining the dict
d = defaultdict(int)
 
L = [1, 2, 3, 4, 2, 4, 1, 2]
 
# Iterate through the list
# for keeping the count
for i in L:
     
    # The default value is 0
    # so there is no need to 
    # enter the key first
    d[i] += 1
     
print(d)
```

### deque - double-ended queue

### Counter
- A container-like object that is similar to dictionary, but its keys are the elements and its values are of each element' frequency.

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

## Lambda functions [TODO]

## Python's [enum](https://docs.python.org/3/library/enum.html)

# Resources
- It may be helpful to read through Python's ==built-in type== documentation: https://docs.python.org/3/library/stdtypes.html
- NeetCode's LeetCode solution reference
https://github.com/neetcode-gh/leetcode/tree/main
- LeetCode Company Interview questions
https://github.com/xizhang20181005/Leetcode_company_frequency

- Everything you need to know about using Python:
    - [The Python Standard Library](https://docs.python.org/3/library/index.html): built-in functions, built-in types, common libraries in use of python
    - [The Python Language Reference](https://docs.python.org/3/reference/index.html): know how to implement syntax and "core-semantics" of the languages
    - [Python Tutorial](https://bugs.python.org/file47781/Tutorial_EDIT.pdf): by our Benevolent Dictator for Life - Guido Van Rossum