'''Insertion Sort

Insertion sort is a simple sorting algorithm in which sorting is done by picking one array element at a time and inserting it into already sorted subarray.
This algorithm is
	1: An in-place comparison sort.
	2: A stable sorting algorithm i.e. after sorting, the order of elements with same value is not changed.
	3: An online sorting algorithm i.e. it can sort a list as and when it receives it.

Time complexity O(n^2)
Space complexity O(1)
'''


def insertion_sort(array, compare=lambda x, y: x > y):
	'''Sort an array using insertion sort.

	Parameters:
		- compare -- function that receives 2 values and returns a boolean that orders a swap between the values
	'''
	if not array or len(array) < 2:
		return
	for k in range(1, len(array)):
		j = k - 1
		saved = array[k]
		while j >= 0 and compare(array[j], saved):
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = saved


# ---------------------------- MAIN

if __name__ == '__main__':
	'''Creates the array
		9  3  4  7  2  5  1  6  8  0
	'''
	array = [9, 3, 4, 7, 2, 5, 1, 6, 8, 0]
	print(array)
	insertion_sort(array)
	print('Crescent order:', array)
	insertion_sort(array, lambda x, y: x < y)
	print('Decrescent order:', array)
