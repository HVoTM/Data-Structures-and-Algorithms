# Sliding Window Techniques

Two types:
## Fixed Size Sliding Window
General steps:
- Find the size of the window required, say K
- Compute the result for 1st window, i.e. include the first K elements of the data structure
- Then use a loop to slide the window by 1 and keep computing the result window by window

## Variable Size Sliding Window
- Increase our right pointer one by one till our condition is true
- At any step if our condition does not match, we shrink the size of our window by increasing left pointer
- Again, when our condition satisfies, we start increasing the right pointer and follow step 1
- We folllow these steps until we reach to the end of the array

## How to identify Sliding Window Problems:
- These problems generally require Finding Maximum/Minimum Subarray, Substrings which satisfy some specific condition.
- The size of the subarray or substring ‘K’ will be given in some of the problems.
- These problems can easily be solved in O(N^2) time complexity using nested loops, using sliding window we can solve these in O(n) Time Complexity.
- Required Time Complexity: *O(N)* or *O(Nlog(N))*
- Constraints: N <= 10^6 , If N is the size of the Array/String.

# Resources
- GeeksforGeeks - Sliding Window Technique: https://www.geeksforgeeks.org/window-sliding-technique/
