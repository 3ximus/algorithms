'''Linked list

A node object holds a value and a pointer to the next item'''


class node:
	'''Linked list node'''

	def __init__(self, value, next_item=None):
		self.value = value
		self.next = next_item

	def __str__(self):
		ret = ''
		ret += str(self.value) + ' -> ' + str(self.next)
		return ret

	def print_list(self):
		'''Print list starting from this node'''
		print(self)


if __name__ == '__main__':
	'''
	Demo:
	 - creates list
		1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> X
	'''
	head = node(1, node(2, node(3, node(4, node(5, node(6, node(7, node(8, node(9, node(10))))))))))
	print("List:")
	head.print_list()
