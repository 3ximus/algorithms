'''Reverse a linked list in an iterative fashion

Time complexity  O(n)
Space complexity O(1)
'''

from linked_list import node


def reverse_list(head):
	'''Reverse a linked list in an iterative fashion'''
	p = c = None # previous and current node
	n = head # next node
	while n:
		c = n
		n = n.next
		c.next = p
		p = c
	return c


if __name__ == '__main__':
	'''
	Demo:
	 - creates list
		1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> X
	'''
	head = node(1, node(2, node(3, node(4, node(5, node(6, node(7, node(8, node(9, node(10))))))))))
	print("List:")
	head.print_list()
	new_head = reverse_list(head)
	print("Reversed List:")
	new_head.print_list()
