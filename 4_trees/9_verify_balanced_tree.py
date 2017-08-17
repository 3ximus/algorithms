'''Verify if a binary tree is height balanced

A binary tree is balanced if
1. At any given node the heigh of left and right subtrees is not greater than 1
2. At any given node the left and right subtree are balanced themselves


In this algorithm "unbalance" is used to track of unbalanced nodes

1. This algorithm starts by checking if current node is a leaf, in wich case we return False if unbalance is not lower than 1
2. If the current node only has a left subtree we recurse on it and give it an unbalanced value of +1
3. If the current node only has a right subtree we recurse on it and give it an unbalanced value of +1
4. If a node has both subtree we recurse on both subtrees and return their values

Time complexity is O(n)
Space complexity is O(n)
'''

from binary_tree import node

def verify_balanced_tree(root, unbalance=0):
	if not root.left and not root.right:
		return True if unbalance < 1 else False
	if root.right and not root.left and unbalance == 0:
		return verify_balanced_tree(root.right, unbalance + 1)
	if root.left and not root.right and unbalance == 0:
		return verify_balanced_tree(root.left, unbalance + 1)
	return verify_balanced_tree(root.left) and verify_balanced_tree(root.right)

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
	print(verify_balanced_tree(root))

	''' creates tree
			  1
		  2       3
		4   5   6   7
	'''

	n2 = node(2, node(4), node(5))
	n3 = node(3, node(6), node(7))
	root = node(1, n2, n3)
	root.print_tree()
	print(verify_balanced_tree(root))