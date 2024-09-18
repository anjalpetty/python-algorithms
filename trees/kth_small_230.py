
"""
Leetcode: 230 Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

    3
  /  \
 1    4
  \
   2

Tip: process like in order traversal and return the k-th element
"""

from typing import Optional

from Tnode import Tnode


def kth_small(root: Optional[Tnode], k: int) -> int:
  n = 0
  stack = []
  curr = root
  while curr or stack:
    while curr:
      stack.append(curr)
      curr = curr.left

    curr = stack.pop()
    n += 1
    if n == k:
      return curr.data
    curr = curr.right

if __name__ == '__main__':
  root = Tnode(3)
  root.left = Tnode(1)
  root.right = Tnode(4)

  root.left.right = Tnode(2)
  print("kth small:", kth_small(root, 1))

  root = Tnode(5)
  root.left = Tnode(3)
  root.right = Tnode(6)

  root.left.left = Tnode(2)
  root.left.right = Tnode(4)
  root.left.left.left = Tnode(1)
  print("kth small:", kth_small(root, 3))
