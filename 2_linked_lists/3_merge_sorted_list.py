'''Merge two sorted linked lists

Time complexity  O(n+m)
Space complexity O(1)
'''

from linked_list import node


def merge_lists(head1, head2):
	'''Merge two linked lists'''
	if not head1:
		return head2
	if not head2:
		return head1

	ptr1 = head1
	ptr2 = head2

	if ptr1.value < ptr2.value:
		merged_head = ptr1
		ptr1 = ptr1.next
	else:
		merged_head = ptr2
		ptr2 = ptr2.next

	merged_tail = merged_head
	while ptr1 or ptr2:
		if not ptr2 or ptr1.value < ptr2.value:
			merged_tail.next = ptr1
			ptr1 = ptr1.next
		elif not ptr2 or ptr1.value >= ptr2.value:
			merged_tail.next = ptr2
			ptr2 = ptr2.next
		merged_tail = merged_tail.next
	return merged_head


# ---------------------------- MAIN

if __name__ == '__main__':
	'''
	Demo:
	 - creates lists
		1 -> 2 -> 4 -> 5 -> 7 -> 9 -> 10 -> X
		3 -> 6 -> 8 -> X
	'''
	head1 = node(1, node(2, node(4, node(5, node(7, node(9, node(10)))))))
	head2 = node(3, node(6, node(8)))
	print("List1:")
	head1.print_list()
	print("List2:")
	head2.print_list()

	merged_head = merge_lists(head1, head2)
	print("Merged List:")
	merged_head.print_list()
