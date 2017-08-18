''' Bubble Sort

Bubble sort is an in-place comparison sort. Bubble sort algorithm compares each pair of adjacent elements and swaps them if they are in the wrong order. The pass through the array is repeated until no swaps are needed, which indicates that the array is sorted.

Time complexity O(n^2)
Space complexity O(1)
'''


def bubble_sort(array, compare=lambda x, y: x > y):
	'''Sort an array using bubble sort.

	Parameters:
		- compare -- function that receives 2 values and returns a boolean that orders a swap between the values
	'''
	if not array or len(array) < 2:
		return
	swap = True
	while swap:
		swap = False
		for i in range(len(array) - 1):
			if compare(array[i], array[i + 1]):
				array[i], array[i + 1] = array[i + 1], array[i]
				swap = True


if __name__ == '__main__':
	'''Creates the array
		9  3  4  7  2  5  1  6  8  0
	'''
	array = [9, 3, 4, 7, 2, 5, 1, 6, 8, 0]
	print(array)
	bubble_sort(array)
	print('Crescent order:', array)
	bubble_sort(array, lambda x, y: x < y)
	print('Decrescent order:', array)
