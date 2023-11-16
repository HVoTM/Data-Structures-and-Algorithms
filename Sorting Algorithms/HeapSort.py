"""
Pseudocode

HeapSort(A, n)
    Build-Max-Heap(A,n)
    for i = n downto 2
        exchange A[1] with A[i]
        A.heap_size = A.heapsize -1
        Max-Heapify(A,1)

Time complexity: O(nlogn)
"""

# Implementation of heapsort

# Heapify function assimilates the methods to build itself a MaxHeap, in this case to build a Binary Tree from the array
# Then rearrange the position to maintain the heap property
def heapify(arr, n, i):
    largest = i # Use given i as the root
    left_child = 2 * i + 1 # Assign the children accordingly
    right_child = 2 * i + 2
    
    # Start with left to right, since order of filling says so
    # Check if left child exists and is greater than the root we set out
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if right child exists and is greater than the root we set out, if left child is larger than root
    # but right child is larger than right child, then we just overwrite largest with rightchild index
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Swap the root with the largest element, and heapify the affected sub-tree recursively
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    # Working the way from
    for i in range(n // 2 - 1, -1, -1): # range(start, stop, step)
        heapify(arr, n, i)

    # Extract elements from the heap one by one from n-1 to 0
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap, tracing from n back to 1

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", list(arr))