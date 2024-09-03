
"""
Leetcode: 199 Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

    1
  /  \
 2    3
  \
   4
"""
from collections import deque
from typing import List, Optional

from Tnode import Tnode


def right_side_view(root: Optional[Tnode]) -> List[int]:
  q = deque([root] if root else [])

  res = []
  if root:
    res.append(root.data)
  while q:
    for i in range(len(q)):
      node = q.popleft()
      # TIP: swap the order of appending to queue if you want left side view
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    if q:
      res.append(q[len(q)-1].data)
  return res

if __name__ == '__main__':
  root = Tnode(1)
  root.left = Tnode(2)
  root.right = Tnode(3)

  root.left.right = Tnode(4)
  print(right_side_view(root))
