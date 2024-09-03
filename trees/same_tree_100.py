
"""
Leetcode: 100 Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

     1
   /  \
 2    3

     1
   /  \
 2    3
"""

from typing import Optional
from Tnode import Tnode

def is_same_tree(p: Optional[Tnode], q: Optional[Tnode]) -> bool:
  if p is None and q is None:
    return True

  if p is not None and q is not None and p.data == q.data:
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

  return False

if __name__ == '__main__':
  root1 = Tnode(1)
  root1.left = Tnode(2)
  root1.right = Tnode(3)

  root2 = Tnode(1)
  root2.left = Tnode(2)
  root2.right = Tnode(3)

  print("is same tree:", is_same_tree(root1, root2))
