'''Check if a binary tree is sub-tree of another binary tree in O(n) time

Given two binary trees a and b, check if tree b is sub-tree of tree a. A sub-tree of tree is a tree
having any one of the nodes 'n' and all the descendants of node 'n'.

1. Find inorder traversals of subtree and Root tree and store them as a string
2. Find postorder traversals of subtree and Root tree and store them as a string
3. For subtree to be a sub-tree of Root tree, the string for inorder traversal of subtree should be a substring of the string for inorder traversal of Root tree. And the same for postorder traversal strings.


The time complexity of this algorithm is O(n) since traversal string can be formed in O(n) time and substring check could also be done in O(n) time (e.g. KPM or Boyer-Moore)

Time complexity is O(n)
Space complexity is O(n)
'''

from binary_tree import node, in_order_traversal, post_order_traversal


def is_subtree(root, subtree):
	'''Check if subtree is a subtree of root in O(n) time'''
# in_order_traversal and post_order_traversal return an iterable with all the nodes, so we map them to get
#   the node value and convert it to a string in each item of the iterable
	inorder_root_string = ''.join(map(lambda x: str(x.value), in_order_traversal(root)))
	inorder_subtree_string = ''.join(map(lambda x: str(x.value), in_order_traversal(subtree)))
	if inorder_subtree_string in inorder_root_string:  # TODO use KPM algorithm
		postorder_root_string = ''.join(map(lambda x: str(x.value), post_order_traversal(root)))
		postorder_subtree_string = ''.join(map(lambda x: str(x.value), post_order_traversal(subtree)))
		if postorder_subtree_string in postorder_root_string:  # TODO use KPM algorithm
			return True
	return False


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
