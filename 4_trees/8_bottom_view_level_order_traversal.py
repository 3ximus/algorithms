'''Bottom view of binary tree using level order traversal

Return the nodes present in a bottom view of a binary tree from left-most end. A node will be in the bottom-view if it is the bottommost node at its horizontal distance from root.
Horizontal distance from root to itself is 0. Horizontal distance of right child of root node is 1 and horizontal distance of left child of root node is -1.

Horizontal distance of node 'n' from root = horizontal distance of its parent from root + 1, if node 'n' is right child of its parent.
Horizontal distance of node 'n' from root = horizontal distance of its parent from root - 1, if node 'n' is left child of its parent.

If more than one nodes are at the same horizontal distance and are the bottom-most nodes for  that horizontal distance, then you can choose to include either of the nodes in the bottom view.

Time complexity is O(n)
Space complexity is O(n)
'''

from binary_tree import node


def bottom_view(root):
	hd = 0  # horizontal distance
	queue = [(root, hd), ]
	mapping = {hd: root}
	while queue != []:
		node, hd = queue.pop(0)
		mapping[hd] = node
		if node.left:
			queue.append((node.left, hd - 1))
		if node.right:
			queue.append((node.right, hd + 1))
	for key in sorted(mapping.keys()):  # print keys in order
		yield mapping[key]


# ---------------------------- MAIN

if __name__ == '__main__':
	''' Creates tree:
               1
           2          3
        4     5    6      7
          8  9       10     11
	'''

	n3 = node(3, node(6, None, node(10)), node(7, None, node(11)))
	n2 = node(2, node(4, None, node(8)), node(5, node(9)))
	root = node(1, n2, n3)
	root.print_tree()
	for n in bottom_view(root):
		print(n.value, end=', ')
	print('\n')

	''' creates tree
			  1
		  2       3
		4   5   6   7
	'''

	n2 = node(2, node(4), node(5))
	n3 = node(3, node(6), node(7))
	root = node(1, n2, n3)
	root.print_tree()
	for n in bottom_view(root):
		print(n.value, end=', ')
	print()
