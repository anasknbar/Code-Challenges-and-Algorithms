# Write your test here
import pytest
from challenge01 import Node, Tree, printTree

def test_buildTree():
    
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    root1 = Tree(preorder1, inorder1)
    assert printTree(root1) == [3, 9, 20, None, None, 15, 7]

   
    preorder2 = [-1]
    inorder2 = [-1]
    root2 = Tree(preorder2, inorder2)
    assert printTree(root2) == [-1]


