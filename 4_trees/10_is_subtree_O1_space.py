'''Check if a binary tree is sub-tree of another binary tree in O(1) space

Given two binary trees a and b, check if tree b is sub-tree of tree a. A sub-tree of tree is a tree
having any one of the nodes 'n' and all the descendants of node 'n'.

1. If subtree is equal to None then return true since None tree is sub-tree for any tree.
2. If condition 1. is not true then check if Root tree is equal to None. If it is then return false since null tree cannot have any sub-tree except null tree for which we have already checked in 1.
3. If both conditions 1. and 2. are not true then check if value of subtree is equal to value of root
4. If condition 3. evaluated to true then we check if left sub-tree of the main subtree matches exactly to left sub-tree of Root tree and right sub-tree of the main subtree matches exactly to right sub-tree of Root tree. If both sub-trees match then we return true since we know that the subtree is a subtree of the root tree
5. If either 3. or 4. evaluate to false then we check if left sub-tree of bigT reeRoot contains smallT ree or right sub-tree of bigT reeRoot contains subtree. For checking this we simply make recursive calls.

Time complexity is O(n^2)
Space complexity is O(1)
'''

from binary_tree import node


def compare_trees(a, b):
	'''Compares 2 trees'''
	if not a and not b:
		return True
	if not a or not b:
		return False
	if a.value == b.value:
		return compare_trees(a.left, b.left) and compare_trees(a.right, b.right)
	else:
		return False


def is_subtree(root, subtree):
	'''Check if subtree is a subtree of root in O(1) space'''
	if not subtree:
		return True
	if not root:
		return False
	if subtree.value == root.value:
		if compare_trees(root, subtree):
			return True
	return is_subtree(root.left, subtree) or is_subtree(root.right, subtree)


# ---------------------------- MAIN

if __name__ == '__main__':
	''' Creates tree:
                1
           2          3
        4     5    6      7
          8         10     11
            9
	'''

	n3 = node(3, node(6, None, node(10)), node(7, None, node(11)))
	n2 = node(2, node(4, None, node(8, None, node(9))), node(5))
	root = node(1, n2, n3)
	print("Root:")
	root.print_tree()

	''' Creates subtree:
           2
        4     5
          8
            9
	'''

	subtree = node(2, node(4, None, node(8, None, node(9))), node(5))
	print("Subtree:")
	subtree.print_tree()

	print("Is Subtree?:", is_subtree(root, subtree))

	''' Creates tree:
           3
         6
           10
	'''

	subtree = node(3, node(6, None, node(10)))
	print("Subtree:")
	subtree.print_tree()

	print("Is Subtree?:", is_subtree(root, subtree))
