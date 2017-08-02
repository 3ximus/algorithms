'''Binary Tree node class

A node object holds a value, and optional left and/or right child
'''

class bt_node:
	'''Binary Tree Node'''
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
