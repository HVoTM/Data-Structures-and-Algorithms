# Implement counting sort
# Integer sorting algorithm to collect objects according to keys that are smaller positive integers

# Works by determining the position of each key value in the output sequence by counting the number of objects with distinct key values
from typing import List

def sort(arr: List[int]) -> List[int]:
    # Determine the largest value in the array
    max_val = max(arr)
    
    # Declare new count array with value 0 and a size of max + 1
    # use this count array to count the number of occurences for each values in the input array
    count = [0] * (max_val + 1)
    # test code: print(count)
    for i in arr:    # wrong: for i in range(len(arr)) because this will use numbered indexes, not the values in the array itself
        count[i] += 1

    # Change the count array by adding the previous counts to produce the cumulative sum of an array
    for j in range(1, len(count)): # range(start, stop, step)
        count[j] += count[j-1]
    
    sorted = [0] * len(arr)
    for k in range(len(arr)-1, -1, -1):
        sorted[count[arr[k]] -1] = arr[k]
        count[arr[k]] -= 1

    return sorted
if __name__ == '__main__':
    arr = [8, 3, 5, 1, 3, 8, 6, 4, 3]
    sorted = sort(arr=arr)
    print(sorted)