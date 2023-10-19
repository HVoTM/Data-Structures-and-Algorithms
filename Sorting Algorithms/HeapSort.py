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