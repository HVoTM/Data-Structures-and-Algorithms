def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def hybridSort(L, T):
    if len(L) > T:
        middle = len(L) // 2
        left = L[:middle]
        right = L[middle:]
        left = hybridSort(left, T)
        right = hybridSort(right, T)
        L = mergeSort(left + right)
    else:
        bubbleSort(L)
    return L

# Example usage:
L = [5, 1, 4, 51, 121, 23, 90, 2]
T = 5
result = hybridSort(L, T)
print(result)
