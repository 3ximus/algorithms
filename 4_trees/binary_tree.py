'''Binary Tree node class and traversal functions

A node object holds a value, and optional left and/or right child
'''

class node:
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
		ret += spacing + (chr(self.value + (10121 if self.value < 11 else 9440)) if unicode else str(self.value)) + '\n'
		if self.left: # left branch
			ret += self.left.__str__(spacing = spacing[:-2] + ('│ ' if spacing[-2:] == '┌─' else '  ') + '└─',unicode=unicode)

		return ret

	def print_tree(self, unicode=True):
		'''Print subtree starting from this node'''
		print(str(self.__str__(unicode=unicode))[:-1])

# ------------------
# Traverse Functions
# ------------------

def post_order_traversal(root):
	'''Traverse tree in a post-order fashion'''
	if not root: return
	# yield from is equivalent to for i in post_order_traversal(root): yield i , in python > 3.3
	yield from post_order_traversal(root.left)
	yield from post_order_traversal(root.right)
	yield root

def pre_order_traversal(root):
	'''Traverse tree in a pre-order fashion'''
	if not root: return
	yield root
	yield from pre_order_traversal(root.left)
	yield from pre_order_traversal(root.right)

def in_order_traversal(root):
	'''Traverse tree in an in-order fashion'''
	if not root: return
	yield from in_order_traversal(root.left)
	yield root
	yield from in_order_traversal(root.right)

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
	n5 = node(5, None, node(7, node(9, node(10, None, node(11)), None), None))
	n3 = node(3, node(4, node(6, None, node(8)), None), n5)
	root =  node(1, node(2), n3)
	print("Tree:")
	root.print_tree()
	print("Post Order Traversal:")
	for n in post_order_traversal(root):
		print(n.value, end=', ')
	print()
