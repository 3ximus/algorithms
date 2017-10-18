'''Count frequencies of array elements in range 1 to n

Given an array of length n count the frequencies of all elements from 1 to n

Time complexity  O(n)
Space complexity O(1)
'''

def count_frequencies(array):
	'''Reverse a linked list in an iterative fashion'''
	n = len(array)
	for i in range(n):
		array[i] -= 1
	for i in range(n):
		array[array[i] % n] += n
	for i in range(n):
		yield (i+1), int(array[i]/n)
		array[i] = array[i] % n + 1



# ---------------------------- MAIN

if __name__ == '__main__':
	'''
	Demo:
	 - creates array
	      [ 2, 3, 3, 4, 3, 1, 6 ]
	'''
	array = [2, 3, 3, 4, 3, 1, 6]
	print("Array:")
	print(array)
	print("Counts:")
	for i, v in count_frequencies(array):
		print(i, '->', v)
