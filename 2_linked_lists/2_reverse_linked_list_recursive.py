'''Reverse a linked list in an recursive fashion

Time complexity  O(n)
Space complexity O(1)
'''

from linked_list import node


def reverse_list(head):
	'''Reverse a linked list in an recursive fashion'''
	if not head:
		return None
	if not head.next:
		return head
	new_head = reverse_list(head.next)
	head.next.next = head
	head.next = None
	return new_head


# ---------------------------- MAIN

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
