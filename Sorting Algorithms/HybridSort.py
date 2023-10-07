# Python program for implementation of MergeSort
def mergesort(arr):
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
    return merge(mergesort(left), mergesort(right))


# Python implementation of QuickSort
# Function to find the partition position
def partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quicksort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quicksort(array, pi + 1, high)

# Optimized Python program for implementation of Bubble Sort


def bubbleSort(arr):
	n = len(arr)
	
	# Traverse through all array elements
	for i in range(n):
		swapped = False

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# Traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if (swapped == False):
			break

# Implementation of HybridSort

def hybridsort(l, big, small, threshold):
	if len(l) > threshold:
		if big == 1:
			# Finding the middle index, then divide it by two halves
			mid = len(l)//2
			left = l[:mid]
			right = l[mid:]
			hybridsort(left, big, small, threshold)
			hybridsort(right, big, small, threshold)
			l = mergesort(left + right)
		else:
			quicksort(l, 0, len(l) - 1)
	else:
		bubbleSort(l)
	return l

if __name__ == '__main__':
	array = [10, 7, 8, 16, 66, 21, 45, 12, 47]

	# Function call
	result = hybridsort(array, 1, 3, 5)
	print('Sorted array: ')
	for x in result:
		print(x, end = " ")