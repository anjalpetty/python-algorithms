"""
Leetcode: 104 Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

        3
      /  \
    9    20
        / \
      15   7
"""
from typing import Optional
from Tnode import Tnode


def max_depth(tnode: Optional[Tnode]):
  if tnode is None:
    return 0
  return max(max_depth(tnode.left), max_depth(tnode.right)) + 1

if __name__ == '__main__':
  root = Tnode(3)
  root.left = Tnode(9)
  root.right = Tnode(20)

  root.right.left = Tnode(15)
  root.right.right = Tnode(7)

  print("max depth:", max_depth(root))