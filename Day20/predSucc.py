def find_successor(root, key):
    successor = None
    curr = root

    while curr:
        if key < curr.key:
            successor = curr          # potential successor
            curr = curr.left
        else:
            curr = curr.right

    return successor
def find_predecessor(root, key):
    predecessor = None
    curr = root

    while curr:
        if key > curr.key:
            predecessor = curr        # potential predecessor
            curr = curr.right
        else:
            curr = curr.left

    return predecessor
