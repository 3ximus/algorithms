'''Check if all internal nodes of a BST have only one child without building the tree

Given preorder traversal array for a BST

Time complexity is O(n)
Space complexity is O(1)
'''


def check_one_child_node(preorder):
	'''Check if all internal nodes of a BST have only one child'''
	maximum = minimum = preorder[-1]
	# traverse in reverse order (ignoring last element)
	for i in range(len(preorder) - 2, -1, -1):
		if not (preorder[i] < minimum or preorder[i] > maximum):
			return False
		maximum = max(preorder[i], maximum)
		minimum = min(preorder[i], minimum)
	return True


# ---------------------------- MAIN

if __name__ == '__main__':
	preorder1 = [9, 8, 5, 7, 6]
	print(check_one_child_node(preorder1))
	preorder2 = [8, 5, 4, 7, 6]
	print(check_one_child_node(preorder2))



