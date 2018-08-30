class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None

def isPresent(root, val):
    if root.value == val:
        return 1
    if not root.value:
        return 0

    if root.value < val:
        return isPresent(root.left, val)
    else:
        return isPresent(root.right, val)


