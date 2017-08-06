'''Insert and search a given value in a binary search tree

In the BST insertion algorithm, every new key is inserted as a leaf node, in the following steps starting at the root:
    1. If the current node is None, then either this is an empty tree or we have reached the correct position in the tree for this key. We create a new node with this key and return it.
    2. If the value to be inserted is less than the node value, then we know that the correct position for this key is in the left sub-tree, therefore we make a recurseive call setting the left subtree to the returned node of the insert function.
    2. If the value to be inserted is greater than the node value, then we know that the correct position for this key is in the right sub-tree, therefore we make a recurseive call setting the right subtree to the returned node of the insert function.
    4. To complete the insertion we return the node that was changed in order to update the whole insertion path on the tree

The algorithm handles insertion of duplicate keys by ignoring these and returning the unchanged tree

The BST search algorithm is very similar to insertion algorithm.

1. If the current node is None, then we return None since we are searching in an empty tree.
2. If key is equal to the node's value, then we know that we have found the key and we return reference to current node.
3. If key is less than node's value, we search for key in the left sub-tree, by making a recursive call.
4. If key is greater than node's value, we search for key in the right sub-tree, by making a recursive call.

Time complexity is O(n)
Amortized time complexity is O(log(n))
Space Complexity is O(d) d: depth of BST
'''

from binary_tree import node


def insert(root, value):
    '''Insert value in a tree rooted at root'''
    if not root: return node(value)
    if value < root.value: root.left = insert(root.left, value)
    if value > root.value: root.right = insert(root.right, value)
    return root

def search(root, value):
    '''Search value in a tree rooted at root'''
    if not root: return None
    if value == root.value: return root
    return search(root.left, value) if value < root.value else search(root.right, value)

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
