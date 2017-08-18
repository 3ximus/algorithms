''' Delete a node in a binary search tree

To delete a node/key from the given binary search tree, we need to consider two cases.

First case: if the node to be deleted is a leaf node or has only one child.

	a. Leaf node deletion: simply make parent node pointer None by returning None
	b. Deletion of node with only one child: we return the value of the opposite node when one of them is None

Second case: if the node to be deleted has both children.

	We copy the value of the inorder successor (or inorder predecessor) to the node to be deleted and delete the inorder sucessor node (right subtree) - the inorder predecessor could be implemented by finding the highest value on the left subtree and deleting it the same way

The function calls itself when it didn't find the key to be deleted, and updates the respective branch to whatever the function returns.

Note that the leaf node deletion is handled automaticly by the deletion of nodes with one child (returns None)

Time Complexity is O(n)
Amortized Time Complexity is O(logn)
Space Complexity is O(d) d: depth of BST
'''

from binary_tree import node


def inOrderSuccessor(node):
	if not node.left:
		return node.value
	return inOrderSuccessor(node.left)


def delete(root, value):
	'''Delete node with given value from tree rooted at root (in case node has 2 children use inorder sucessor)'''
	if not root:
		return None
	if value == root.value:  # handle removal
		if not root.left:
			return root.right
		elif not root.right:
			return root.left
		else:  # node has both children
			min_value = inOrderSuccessor(root.right)
			root.value = min_value
			root.right = delete(root.right, min_value)
	if value < root.value:
		root.left = delete(root.left, value)
	else:
		root.right = delete(root.right, value)
	return root


# ---------------------------- MAIN

if __name__ == '__main__':
	''' creates tree
             4
          2        7
        1        6
               5
	'''

	n2 = node(2, node(1), None)
	n7 = node(7, node(6, node(5), None), None)
	root = node(4, n2, n7)

	root.print_tree()
	print("Deleting 5")
	delete(root, 5)
	root.print_tree()
	print("Deleting 7")
	delete(root, 7)
	root.print_tree()
	print("Deleting 4")
	delete(root, 4)
	root.print_tree()
