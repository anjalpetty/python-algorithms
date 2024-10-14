"""
Leetcode: 98 Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

Example 1:
    2
  /  \
1     3
Input: root = [2,1,3]
Output: true

Example 2:
       5
     /   \
   1      4
         /  \
       3     6
Input: root = [5,1,4,null,null,3,6]
Output: false
"""

from Tnode import Tnode

def max_value(node):
  if node is None:
    return float('-inf')
  return max(node.data, max_value(node.left), max_value(node.right))

def min_value(node):
  if node is None:
    return float('inf')
  return min(node.data, min_value(node.left), min_value(node.right))

def check_bst(root):
  if root is None:
    return True

  if root.left and max_value(root.left) >= root.data:
    return False
  if root.right and min_value(root.right) <= root.data:
    return False

  return check_bst(root.left) and check_bst(root.right)

if __name__ == '__main__':
  root = Tnode(2)
  root.left = Tnode(1)
  root.right = Tnode(3)
  print(check_bst(root))

  root = Tnode(5)
  root.left = Tnode(1)
  root.right = Tnode(4)
  root.right.left = Tnode(3)
  root.right.right = Tnode(6)
  print(check_bst(root))