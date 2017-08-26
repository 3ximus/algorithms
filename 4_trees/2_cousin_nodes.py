'''Given two nodes in a binary tree, check if they are cousins.

Two nodes are cousins if:
1. they are not siblings (children of same parent).
2. they are on the same depth.

How to find if 2 nodes are siblings:
1. If A and B are left and right children of the root, then they are siblings.
2. Else check Step 1 in left and right subtrees.
3. If the condition in Step 1 is not true for any node, then the nodes are not siblings.

Time Complexity is O(n)
Space Complexity is O(1)
'''

from binary_tree import node


def get_depth(root, x, current_depth=1):
	'''Return depth of a node'''
	if not root:
		return 0
	if x == root:
		return current_depth  # found the node, return its depth
	# recurse on the left or right subtree and return the one that's not 0
	return get_depth(root.left, x, current_depth + 1) or get_depth(root.right, x, current_depth + 1)


def are_siblings(root, a, b):
	'''Verify if two nodes are siblings'''
	if not root:
		return False
	if root.left and root.right and root.left in (a, b) and root.right in (a, b):
		return True  # left and right children exist and are a and b
	return are_siblings(root.left, a, b) or are_siblings(root.right, a, b)


def are_cousins(root, a, b):
	'''Verify if two nodes are cousins'''
	if not root:
		return False
	if a == b:
		return False  # nodes cant be the same
	return (not are_siblings(root, a, b)) and get_depth(root, a) == get_depth(root, b)


# ---------------------------- MAIN

if __name__ == '__main__':
	''' creates tree
              4
          2       6
        1   3   5   7
	'''

	n1 = node(1)
	n3 = node(3)
	n5 = node(5)
	n7 = node(7)
	n2 = node(2, n1, n3)
	n6 = node(6, n5, n7)
	root = node(4, n2, n6)

	root.print_tree()
	print('1 and 3: ', are_cousins(root, n1, n3))
	print('7 and 2: ', are_cousins(root, n7, n2))
	print('1 and 5: ', are_cousins(root, n1, n5))
