'''Verify if a binary tree is a binary search tree

In a BST, the root is greater than all bt_nodes of the left sub tree. So root value forms an upper bound on left sub tree values.

Similarly, since the root is less than all the bt_nodes of the right sub tree, root value forms a lower bound on the right sub tree values.

This can be used for checking if a binary tree is a binary search tree or not.
1. Initialize, low = MIN_VALUE, high = MAX_VALUE.
2. If root.data <= low || root.data >= high, return false.
3. Recursively check for left sub tree and right sub tree,
    for left sub tree, pass high as root.data because for a BST, root forms an upper bound for left sub tree bt_node values,
    for right sub tree, pass low as root.data because for a BST, root forms a lower bound for right sub tree bt_node values.

Time complexity: O(n)
'''
from bt_node import bt_node

MIN_VALUE = -2**32 # hypothetic minimum integer value
MAX_VALUE = 2**32 # hypothetic maximum integer value

def check_bst(root, lower, upper):
    '''Verify if a binary tree is a binary search tree'''
    if not root: return True # reached a leaf
    if root.value <= lower or root.value >= upper: # its not a bst
        return False
    return check_bst(root.left, lower, root.value) and check_bst(root.right, root.value, upper) # recurse left and right



# ---------------------------- MAIN

if __name__ == '__main__':
    ''' creates tree
              4
          2       6
        1   3   5   7
    '''
    n1 = bt_node(1)
    n3 = bt_node(3)
    n5 = bt_node(5)
    n7 = bt_node(7)
    n2 = bt_node(2, n1, n3)
    n6 = bt_node(6, n5, n7)
    root = bt_node(4, n2, n6)

    print(check_bst(root, MIN_VALUE, MAX_VALUE))

    # --------------------------

    ''' creates tree
              5
          2       6
        1   3   4   7
    '''
    n1 = bt_node(1)
    n3 = bt_node(3)
    n4 = bt_node(4)
    n7 = bt_node(7)
    n2 = bt_node(2, n1, n3)
    n6 = bt_node(6, n4, n7)
    root = bt_node(5, n2, n6)

    print(check_bst(root, MIN_VALUE, MAX_VALUE))