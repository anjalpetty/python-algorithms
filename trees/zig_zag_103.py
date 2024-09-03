
"""
Leetcode: 103 Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

     3
    / \
   9   20
      / \
    15   7

output:
[[3],[9,20],[15,7]]
"""
from collections import deque
from typing import Optional, List
from Tnode import Tnode


def zigzag_level_order(root: Optional[Tnode]) -> List[List[int]]:

  res = []
  queue = deque([root] if root else [])
  while queue:
    level = []
    for i in range(len(queue)):
      node = queue.popleft()
      level.append(node.data)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    level = list(reversed(level)) if len(res) % 2 else level
    res.append(level)
  return res

if __name__ == '__main__':
  root = Tnode(3)
  root.left = Tnode(9)
  root.right = Tnode(20)

  root.right.left = Tnode(15)
  root.right.right = Tnode(7)

  print(zigzag_level_order(root))
