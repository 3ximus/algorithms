'''Level order traversal of a binary tree

1. Create a queue and add root node to it
2. While the queue is not empty do steps 3-5
3. Take node from the queue and return it
4. If the node has a left child add it to the queue
5. If the node has a right child add it to the queue

Time complexity is O(n)
Space complexity is O(n)
'''

from binary_tree import node

def level_order_traversal(root):
	queue = [root,]
	while queue != []:
		node = queue[0]
		if node.left: queue.append(node.left)
		if node.right: queue.append(node.right)
		del queue[0]
		yield node


if __name__ == '__main__':
	''' Creates tree:

	    1
	 2       3
	      4     5
	    6          7
	      8      9
	           10

	'''
	n5 = node(5, None, node(7, node(9, node(10), None), None))
	n3 = node(3, node(4, node(6, None, node(8)), None), n5)
	root =  node(1, node(2), n3)
	root.print_tree()
	for node in level_order_traversal(root):
		print(node.value, end=', ')
	print()
