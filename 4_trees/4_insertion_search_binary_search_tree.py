'''Insert and search a given value in a binary search tree

In the BST insertion algorithm, every new key is inserted as a leaf node. The algorithm basically searches for the correct position of the new node in the BST.

If insert(currentNode, key) is called then -
1. If currentNode is null, then either this is an empty tree or we have reached the correct position in the tree for this key.
We create a new node with this key and make currentNode reference point to this new node.
2. If the value of key is less than currentNode value, then we know that correct position for this key is in the left sub-tree of currentNode. We also know that the left sub-tree would be modified after inserting this key. Therefore we make a recursive call as -  currentNode.left = insert(currentNode.left, key)
3. If the value of key is greater than currentNode value, then we know that correct position for this key is in the right sub-tree of currentNode. We also know that the right sub-tree would be modified after inserting this key. Therefore we make a recursive call as -  currentNode.right = insert(currentNode.right, key)
4. Insertion of key would be completed in above steps. In this step, we return reference of currentNode to the calling function to make it visible the changes that have occurred in the tree(due to insertion of new key) rooted at currentNode.

Note how this algorithm handles insertion of duplicates keys. If the key value matches the currentNode value, then this algorithm does no action and simply returns reference of currentNode thereby avoiding insertion of duplicate keys.

BST search algorithm - Search algorithm is very similar to insertion algorithm. If function call - search(currentNode, key) is made for searching key into the tree rooted at currentNode, then

1. If currentNode is null, then we return null since we are searching in an empty tree.
2. If key is equal to the currentNode's value, then we know that we have found the key at this currentNode itself and we return reference to currentNode.
3. If key is less than currentNode's value, we search for key in the left sub-tree.
4. If key is greater than currentNode's value, we search for key in the right sub-tree.

Check out function search(BinarySearchTreeNode node, int key) in the code snippet for implementation.

Time complexity is O(n)
Amortized time complexity is O(log(n))
'''

from binary_tree import node


def insert(root, value):
	pass

def search(root, value):
	pass

if __name__ == '__main__':
    ''' creates tree
              4
          2       6
        1   3   5   7
    '''
    n1 = node(1)
    n3 = node(3)
    n5 = node(5)
    n7 = node(7)
    n2 = node(2, n1, n3)
    n6 = node(6, n5, n7)
    root = node(4, n2, n6)

    root.print_tree()
