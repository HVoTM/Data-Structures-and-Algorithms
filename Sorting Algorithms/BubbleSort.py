# Optimized Python program for implementation of Bubble Sort

'''
procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped := false
        for i := 1 to n-1 inclusive do
            { if this pair is out of order }
            if A[i-1] > A[i] then
                { swap them and remember something changed }
                swap(A[i-1], A[i])
                swapped := true
            end if
        end for
    until not swapped
end procedure

'''
def BubbleSort(arr):
	n = len(arr)
	for i in range(n):
		swapped = False
		
		# Traverse the array from 0 to n - i - 1
		# Swap if element is greater than the next one
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]: 
				arr[j], arr[j+1] = arr[j+1], arr[j] # Here we use tuple assignment, for quicker presentation
				swapped = True

		if swapped == False:
			break

	return 

if __name__ == "__main__":
	arr = [64, 34, 25, 12, 22, 11, 90, 123, 1231, 3, 344, 59]

	BubbleSort(arr)

	print("Sorted array:")
	for i in range(len(arr)):
		print("%d" % arr[i], end=" ")

"""
Evaluation: 
Time Complexity is O(n^2), which is high.

This algorithm is mostly used for educational purposes in computer science.

Other variations include Cocktail shaker sort (bi-directional sort), Odd-even sort(parallel)

If parraleliz
"""