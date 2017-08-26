'''Heap Sort

Heap sort is an in-place comparison sort.
Heap sort is not a stable sort i.e. it does not ensure the order of same array elements after sorting.

Definition:
A max-heap is a complete binary tree in which the value at root is greater than or equal to the values of left and right children of the root and all the heap nodes follow this property.
Since a max heap is a complete binary tree, it can be represented by an array such that:
1. Element at index 0 is the root.
2. F or any node of the heap at index i, including the root node (i=0):
Index of Left child = 2*i+1
Index of Right child = 2*i+2
Parent of the node = (i-1)/2

Time Complexity O(nlog(n))
Space Complexity O(1)
'''

def heapify(array, i, heapsize, compare):
	'''Transform an array into a max heap'''
	l = 2 * i + 1
	r = 2 * i + 2
	# replace current with max between left and right child
	larger = i
	if l < heapsize and compare(array[l], array[i]):
		larger = l
	if r < heapsize and compare(array[r], array[larger]):
		larger = r
	if larger != i:
		array[larger], array[i] = array[i], array[larger]
		heapify(array, larger, heapsize, compare)


def heap_sort(array, compare=lambda x, y: x > y):
	'''Sort an array using heap sort.

	Parameters:
		- compare -- function that receives 2 values and returns a boolean that orders a swap between the values
	'''
	if not array or len(array) < 2:
		return
	# Build Max Heap
	# heapify all internal nodes (excluding leafs) start from parent of the last index (last leaf node)
	for i in range(int((len(array) - 2) / 2), -1, -1):
		heapify(array, i, len(array), compare)

	heapsize = len(array)
	for i in range(len(array) - 1, 0, -1):
		array[0], array[i] = array[i], array[0]
		heapsize -= 1
		heapify(array, 0, heapsize, compare)


# ---------------------------- MAIN

if __name__ == '__main__':
	'''Creates the array
		9  3  4  7  2  5  1  6  8  0
	'''
	array = [9, 3, 4, 7, 2, 5, 1, 6, 8, 0]
	print(array)
	heap_sort(array)
	print('Crescent order:', array)
	heap_sort(array, lambda x, y: x < y)
	print('Decrescent order:', array)
