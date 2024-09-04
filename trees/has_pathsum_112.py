
"""
Leetcode: 112. Path Sum
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

           5
        /    \
      4       8
    /        / \
  11       13   4
 /  \            \
7    2            1

input : root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
output: 5 + 4 + 11+ 2 => true
"""
from Tnode import Tnode


def has_path_sum(root: Tnode, target_sum: int) -> bool:
  if not root:
    return False

  if root.data == target_sum:
    return True

  return has_path_sum(root.left, target_sum-root.data) or has_path_sum(root.right, target_sum-root.data)

if __name__ == '__main__':
  root = Tnode(5)
  root.left = Tnode(4)
  root.right = Tnode(8)

  root.left.left = Tnode(11)
  root.left.left.left = Tnode(7)
  root.left.left.right = Tnode(2)

  root.right.left = Tnode(13)
  root.right.right = Tnode(4)
  root.right.right.right = Tnode(1)

  print("has path sum:", has_path_sum(root, 22))
