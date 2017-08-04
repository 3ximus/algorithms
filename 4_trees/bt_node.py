'''Binary Tree node class

A node object holds a value, and optional left and/or right child
'''

class bt_node:
	'''Binary Tree Node'''
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self, unicode=True, spacing='  '):
		'''Returns subtree starting from this node

		Use the unicode flag to use unicode numbers (unicode characters are still used for the branches)
		'''
		ret = ''
		if self.right: # right branch
			ret += self.right.__str__(spacing = spacing[:-2] + ('│ ' if spacing[-2:] == '└─' else '  ') + '┌─', unicode=unicode)
		ret += '\n' + spacing + (chr(self.value + (10121 if self.value < 11 else 9440)) if unicode else str(self.value))
		if self.left: # left branch
			ret += self.left.__str__(spacing = spacing[:-2] + ('│ ' if spacing[-2:] == '┌─' else '  ') + '└─',unicode=unicode)

		return ret

	def print_tree(self, unicode=True):
		'''Print subtree starting from this node'''
		print(str(self.__str__(unicode=unicode)))



if __name__ == '__main__':
	'''
	Demo:
	 - creates tree

	    1
	 2      3
	      4    5
	    6         7
	      8     9
	          10
	            11

	'''
	n5 = bt_node(5, None, bt_node(7, bt_node(9, bt_node(10, None, bt_node(11)), None), None))
	n3 = bt_node(3, bt_node(4, bt_node(6, None, bt_node(8)), None), n5)
	root =  bt_node(1, bt_node(2), n3)
	root.print_tree()
