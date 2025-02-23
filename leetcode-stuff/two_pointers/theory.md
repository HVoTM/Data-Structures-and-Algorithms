# Two-Pointer Technique 
> O(N) time and O(1) space
>> time: loop runs at most n times since we have the two pointers approach from both sides as we pass the array into it
>> space: we just need extra constant variable left, right

- The idea of the technique is to begin with two corners of the given array. We use two index variables:
    - **left** and **right** to traverse from both corners
- Initialize for 0-indexed object: left = 0, right = len(array) - 1
- Run a loop while _**left < right**_, do the following inside the loop: 
    - Compute the current sum, sum = arr[left] + arr[right]
    - If the sum equals the target, we’ve found the pair.
    - If the sum is less than the target, move the left pointer to the right to increase the sum.  
    - If the sum is greater than the target, move the right pointer to the left to decrease the sum.

## We need to prove that we never miss a valid pair.

- **Case 1 ( When we increment left)**
In this case we simply ignore current arr[left] and move to the next element by doing left++. We do this when arr[left] + arr[right] is smaller than the target. 
The reason this step is safe is, if arr[left] is giving a smaller value than sum, then it will given even much less values for the elements before arr[right]. 
Now how about the elements after arr[right]? Note that we moved right when we were sure that no pair can be formed with the current right (arr[right] was too high),
so arr[left] can not form a pair with those values also.

- **Case 2 (When we decrement right)** 
We can use the same reasoning (as we discussed for left) to prove that we never miss out a valid pair.