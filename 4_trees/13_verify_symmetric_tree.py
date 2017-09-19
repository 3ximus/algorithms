'''Verify if a binary tree symmetric

A symmetric binary tree is a tree in which at the root node the tree is a mirror of itself

Time complexity: O(n)
Space complexity: O(n)
'''

from binary_tree import node


def mirror(root1, root2):
	'''Verify if 2 binary trees are mirror of each other'''
	if not root1 and not root2:
		return True
	if not root1 or not root2:
		return False
	if root1.value == root2.value:
		return mirror(root1.left, root2.right) and mirror(root1.right, root2.left)
	return False


def symmetric(root):
	'''Verify if a binary tree is symmetric'''
	return mirror(root, root)


# ---------------------------- MAIN

if __name__ == '__main__':
	''' creates tree
               4
          2        2
        1   3    3   1
      4      5  5      4
	'''

	n1 = node(2, node(1, node(4)), node(3, None, node(5)))
	n2 = node(2, node(3, node(5)), node(1, None, node(4)))
	root = node(4, n1, n2)

	root.print_tree()
	print(symmetric(root))

	# --------------------------

	''' creates tree
               4
          2        2
        1   3    3   1
      4      5  4      5
	'''

	n1 = node(2, node(1, node(4)), node(3, None, node(5)))
	n2 = node(2, node(3, node(4)), node(1, None, node(5)))
	root = node(4, n1, n2)

	root.print_tree()
	print(symmetric(root))
