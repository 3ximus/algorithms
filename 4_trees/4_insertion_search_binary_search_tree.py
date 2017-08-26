'''Insert and search a given value in a binary search tree

Time complexity is O(n)
Amortized time complexity is O(log(n))
Space Complexity is O(d) d: depth of BST
'''

from binary_tree import node


def insert(root, value):
	'''Insert value in a tree rooted at root'''
	if not root:
		return node(value)
	if value < root.value:
		root.left = insert(root.left, value)
	if value > root.value:
		root.right = insert(root.right, value)
	return root


def search(root, value):
	'''Search value in a tree rooted at root'''
	if not root:
		return None
	if value == root.value:
		return root
	return search(root.left, value) if value < root.value else search(root.right, value)


# ---------------------------- MAIN

if __name__ == '__main__':
	''' creates tree
              4
          2       6
        1       5
	'''

	n2 = node(2, node(1), None)
	n6 = node(6, node(5), None)
	root = node(4, n2, n6)

	root.print_tree()
	print("Insert 7")
	insert(root, 7)
	root.print_tree()
	print("Insert 3")
	insert(root, 3)
	root.print_tree()

	print("---------\nSearching 3")
	found_node = search(root, 3)
	found_node.print_tree()

	print("Searching 6")
	found_node = search(root, 6)
	found_node.print_tree()
