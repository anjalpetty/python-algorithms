"""
Leetcode: 226 Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

input
         4
      /    \
    2       7
  /  \     / \
 1    3   6   9

output
         4
      /    \
    7       2
  /  \     / \
 9    6   3   1
"""
from typing import Optional
from Tnode import Tnode

def invert_tree(tnode: Optional[Tnode]) -> Tnode:
  if not tnode:
    return None

  tnode.left, tnode.right = tnode.right, tnode.left
  invert_tree(tnode.left)
  invert_tree(tnode.right)

  return tnode

def print_tree(tnode: Optional[Tnode]):
  queue = [tnode]

  while len(queue) > 0:
    size = len(queue)
    for i in range(size):
      curr: Tnode = queue.pop(0)
      print(curr.data, end=" ")
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
    print("")

if __name__ == '__main__':
  root = Tnode(4)
  root.left = Tnode(2)
  root.right = Tnode(7)

  root.left.left = Tnode(1)
  root.left.right = Tnode(3)

  root.right.left = Tnode(6)
  root.right.right = Tnode(9)

  print_tree(root)
  invert_tree(root)
  print("--------")
  print_tree(root)
