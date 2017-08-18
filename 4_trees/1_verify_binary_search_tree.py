'''Verify if a binary tree is a binary search tree

In a binary search tree, the root is greater than all nodes of the left sub tree. So root value forms an upper bound on left sub tree values.

Similarly, since the root is less than all the nodes of the right sub tree, root value forms a lower bound on the right sub tree values.

This can be used for checking if a binary tree is a binary search tree or not.
1. We set lower and upper bounds, preferibly to infinity values
2. If root.data <= lower || root.data >= upper, return false.
3. Recursively check the left sub tree and right sub tree,
	for the left sub tree, pass upper as root.data because for a BST, root forms an upper bound for left sub tree node values,
	for the right sub tree, pass lower as root.data because for a BST, root forms a lower bound for right sub tree node values.

Time complexity: O(n)
'''

from binary_tree import node


MIN_VALUE = -2**32  # hypothetic minimum integer value
MAX_VALUE = 2**32  # hypothetic maximum integer value


def check_bst(root, lower, upper):
	'''Verify if a binary tree is a binary search tree'''
	if not root:
		return True
	if root.value <= lower or root.value >= upper:  # its not a bst
		return False
	return check_bst(root.left, lower, root.value) and check_bst(root.right, root.value, upper)


# ---------------------------- MAIN

if __name__ == '__main__':
	''' creates tree
              4
          2       6
        1   3   5   7
	'''

	n2 = node(2, node(1), node(3))
	n6 = node(6, node(5), node(7))
	root = node(4, n2, n6)

	root.print_tree()
	print(check_bst(root, MIN_VALUE, MAX_VALUE))

	# --------------------------

	''' creates tree
              5
          2       6
        1   3   4   7
	'''

	n2 = node(2, node(4), node(5))
	n3 = node(3, node(6), node(7))
	root = node(1, n2, n3)

	root.print_tree()
	print(check_bst(root, MIN_VALUE, MAX_VALUE))
