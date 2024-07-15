

# write your code here
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def conver_to_BTS(nums):
    if not nums:
        return None


    mid = len(nums) // 2
    
    root = TreeNode(nums[mid])
    root.left = conver_to_BTS(nums[:mid])
    root.right = conver_to_BTS(nums[mid + 1:])

    return root


def print_BTS(root):
    if not root:
        return []
    
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()
    
    return result







