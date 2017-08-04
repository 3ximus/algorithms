'''Given a binary tree, remove all nodes which lie on path having sum less than k.

While traversing down we pass sum as a parameter which is the sum of all the nodes on the current path including the current node.
Recursively traverse left and right subtrees passing the sum.
Once we reach a leaf node, we check if its path sum is less than k. If it is, then return null.
While backtracking from recursive steps, find maximum of left and right path sum. If the maximum sum becomes less than k, then we delete the current node by setting it to null.
A node may be part of multiple paths, so we have to delete it only when all paths from it have sum less than k
Please note that by the time we come to delete a node, its children would have already been deleted and hence the current node which we will be deleting will be a leaf node.

Time Complexity is O(n)
Space Complexity is O(1)
'''

from binary_tree import node

def _inner_remove_path(root, k, path_sum=0):
	if not root: return None, path_sum
	root.left, left_path_sum = _inner_remove_path(root.left, k, path_sum + root.value)
	root.right, right_path_sum = _inner_remove_path(root.right, k, path_sum + root.value)
	path_sum = max(left_path_sum, right_path_sum)
	if path_sum < k: root = None
	return root, path_sum

def remove_path(root, k):
	'''Remove all paths in which sum is less than k'''
	root, path_sum = _inner_remove_path(root, k)
	if path_sum < k: return None
	return root

if __name__ == '__main__':
	''' creates tree
			  4
		  2       6
		1   3   5   7
	'''

	n2 = node(2, node(1), node(3))
	n6 = node(6, node(5), node(7))
	root = node(4, n2, n6)

	print('Before path removal:')
	root.print_tree()
	new_root = remove_path(root, 10)
	print('After path removal:')
	new_root.print_tree()
	print('------------')


	''' Creates tree:
	```
	```    1
	``` 2      3
	```      4    5
	```    6         7
	```      8     9
	```          10
	```            11
	```
	'''
	n5 = node(5, None, node(7, node(9, node(10, None, node(11)), None), None))
	n3 = node(3, node(4, node(6, None, node(8)), None), n5)
	root =  node(1, node(2), n3)
	print('Before path removal:')
	root.print_tree()
	new_root = remove_path(root, 24)
	print('After path removal:')
	new_root.print_tree()

