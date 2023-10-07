"""
INSERTION-SORT is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
The array is virtually split into a sorted and unsorted part. Values from the unsorted part are picked and placed at the 
correct position in the sorted part.

pseudocode:

INSERTION-SORT (A,n)
for i = 2 to n
    key = A[i]
    // Insert A[i] into the sorted subarray A[1: i - 1]
    j = i -1
    while j > 0 and A[j] > key
        A[i+j] = A[j]
        j = j -1
    A[j + 1] = key
    
"""

# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i - 1
		while j >= 0 and key < arr[j] :
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("%d" %arr[i])

# This code is contributed by Mohit Kumra
