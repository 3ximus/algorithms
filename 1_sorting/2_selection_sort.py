'''Selection Sort

Selection sort is an in-place comparison sort. The algorithm divides the input array into two parts:
1: the subarray of items already sorted, which is built up from left to right, and
2: the subarray of items remaining to be sorted that occupy the rest of the array.

Initially, the sorted subarray is empty and the unsorted subarray is the entire input array. The algorithm proceeds by finding the smallest element in the unsorted subarray, swapping it with the leftmost unsorted element (putting it in sorted order), and moving the subarray boundaries one element to the right.

Time complexity O(n^2)
Space complexity O(1)
'''

def selection_sort(array, compare=lambda x,y: x > y):
	'''Sort an array using selection sort.

	Parameters:
		- compare -- function that receives 2 values and returns a boolean that orders a swap between the values
	'''
	if not array or len(array) < 2 : return
	i = 0
	for i in range(len(array)):
		minimum_index = i
		for j in range(i+1, len(array)):
			if compare(array[minimum_index], array[j]):
				minimum_index = j
		if i != minimum_index and array[i] != array[minimum_index]:
			array[i], array[minimum_index] = array[minimum_index], array[i]

if __name__ == '__main__':
	'''Creates the array
		9  3  4  7  2  5  1  6  8  0
	'''
	array = [ 9, 3, 4, 7, 2, 5, 1, 6, 8, 0 ]
	print(array)
	selection_sort(array)
	print('Crescent order:', array)
	selection_sort(array, lambda x,y: x < y)
	print('Decrescent order:', array)

