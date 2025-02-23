"""
SLIDING WINDOW TECHNIQUE
- Defining a **window** or **range** in the input data (arrays or strings) and then moving that window across the data to perform
some operations within the window
- Commonly used in algorithms like:
    + finding SUBARRAYS with a specific sum
    + finding the longest SUBSTRING with unique characters
    + solving problems that require fixed-size window to process elements efficiently

- Using sliding window technique will solve the problem in O(N) (or O(logN)) time instead of O(N^2) time with nested loops

- Concepts:
    + using left and right pointers to indicate the edge of the window -> O(1) time to shift the range and update instead of recalculating
    + compute the necessary operation in that window
    + slide the window given the conditions (fixed vs variable sliding window)
"""
import time
import sys
# O(K*N) solution for finding maximum sum of a subarray of size K
INT_MIN = -sys.maxsize - 1

# code the test the runtime 
def measureRuntime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Function '{func.__name__}' executed in {runtime:.9f} seconds")
        return result
    return wrapper

"Returns maximum sum in a subarray of size K"

@measureRuntime
def bruteForce(arr, n, k):
    # init result
    max_sum = INT_MIN

    # Here we are using a nested loop
    # First loop to be iterating over n - k + 1 variables to account for the k-element groups in this subarray
    # Consider all blocks starting with i
    for i in range(n- k + 1):
        current_sum = 0
        # Second loop to iterate over each element in that corresponding subarray
        # NOTE:  using Python splice would not help reduce the runtime much, I have tried it in LeetCode
        for j in range(k):
            current_sum += arr[i+j]

        # Update result if condition met (a larger sum than the current maximum)
        max_sum = max(current_sum, max_sum)

    return max_sum

@measureRuntime
def slidingWindow(arr, k):
    n = len(arr)

    # n must be greater than k
    if n<=k:
        print("Invalid")
        return -1
    
    # Compute the sum of the first window of size k
    window_sum = sum(arr[:k])

    # First sum available
    max_sum = window_sum 

    # Compute the sums of the remaining windows by removing the first element of previous window and 
    # adding the last element of the current window
    # As we can see, we are only passing the array over in just one loop, hence runtime of O(N)
    # we can access each variable in a list with a constant runtime O(1)
    for i in range(n - k):
        window_sum += -arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(bruteForce(arr, n, k))
print(slidingWindow(arr, k))
