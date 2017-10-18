'''Leaders in Array

A leader is an element which is larger than all the elements in the array to its right

Time complexity  O(n)
Space complexity O(1)
'''


def find_leaders(array):
	'''Find leaders in a given array'''
	leader = array[len(array) - 1]
	yield leader
	for i in range(len(array) - 2, -1, -1):
		if array[i] > leader:
			leader = array[i]
			yield leader


# ---------------------------- MAIN


if __name__ == '__main__':
	array = [98, 23, 54, 12, 20, 7, 27]
	print("Array:", array)
	print("Leaders:")
	for leader in find_leaders(array):
		print(leader)
