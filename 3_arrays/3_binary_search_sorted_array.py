'''Binary Search in a Sorted Array

Find and element in a sorted array using binary search

Time complexity  O(log n)
Space complexity O(1)
'''


def binary_search(array, value):
	'''Find value in a sorted array'''
	start = 0
	end = len(array) - 1
	while start <= end:
		mid = int((start + end) / 2)
		if array[mid] == value:
			return mid
		elif array[mid] < value:
			start = mid + 1
		else:
			end = mid - 1
	return None


# ---------------------------- MAIN


if __name__ == '__main__':
	'''
	Demo:
	 - creates array
	      "abc"
	'''
	array = [5, 11, 22, 34, 56, 69, 77, 83, 99, 104, 198, 230, 290, 341, 402]
	print("Array:", array)
	print("Value 99 found at position:", binary_search(array, 99))
