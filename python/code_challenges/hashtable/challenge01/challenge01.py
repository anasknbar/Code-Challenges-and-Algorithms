# Write here the code challenge solution

class TreeNode:
    '''tree node class'''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    '''function to determine if there are two elements in a binary search tree sumation is equal to a given integer k.'''
    def find(node, k, prev):
        if not node:
            return False
        if k - node.val in prev:
            return True
        prev.add(node.val)
        return find(node.left, k, prev) or find(node.right, k, prev)

    prev = set()
    return find(root, k, prev)


