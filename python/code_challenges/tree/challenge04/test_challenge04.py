# Write your test here
from challenge04 import TreeNode,find_max_value


def test_single_node_tree():
    root1 = TreeNode(10)
    assert find_max_value(root1) == 10
    
def test_multiple_nodes_tree():
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.right = TreeNode(20)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(30)
    assert find_max_value(root2) == 30

    
