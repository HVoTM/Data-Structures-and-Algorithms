# Python3 code to implement binary search

def binarysearch(arr, x, l ,r):

    if r >= l:
    
        mid = l + (r - l)// 2
        # If key is equal to the middle index, return
        if x == arr[mid]:
            return mid
        
        # If not, compare with two halves using recursion
        elif x < arr[mid]:
            return binarysearch(arr, x, l, mid - 1)
        
        else:
            return binarysearch(arr, x, mid + 1, r)

    # Element not in the array
    else:
        return -1

# Main Code
if __name__ == "__main__":
    arr = [1, 4, 7, 10, 13, 20]
    x = 20

    # Function call
    result = binarysearch(arr, x, 0, len(arr)-1)

    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)