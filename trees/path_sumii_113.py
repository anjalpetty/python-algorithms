
"""
Leetcode: 113 Path Sum II
Given the root of a binary tree and an integer target_sum,
return all root-to-leaf paths where the sum of the node values in the path equals target_sum.
Each path should be returned as a list of the node values, not node references.

              5
            /  \
          4     8
        /      / \
      11     13   4
     / \         / \
   7    2       5   1

Input : root = [5,4,8,11,null,13,4,7,2,null,null,5,1], target_sum = 22
Output: [[5,4,11,2],[5,8,4,5]]
"""
from typing import List, Optional
from Tnode import Tnode


def path_sumii(root: Tnode, target_sum: int) -> List[List[int]]:
  result = []
  path = []
  path_of_sum = 0
  dfs(root, target_sum, path_of_sum, path, result)
  return result

def dfs(root: Tnode, sum: int, path_of_sum: int, path: List[int], result: List[List[int]]):
  if not root:
    return
  path_of_sum += root.data
  if root.left is None and root.right is None and path_of_sum == sum:
    result.append([*path, root.data])
    return None

  path.append(root.data)
  dfs(root.left, sum, path_of_sum, path, result)
  dfs(root.right, sum, path_of_sum, path, result)
  path_of_sum -= root.data
  path.pop()


# NOTE: approach two ( doesn't pass all test cases)
def path_sum(root: Optional[Tnode], target_sum: int) -> List[List[int]]:
  res = []

  if not root:
    return List[None]
  stack = []
  stack.append(root)

  curr_sum = 0
  values = []
  while stack:
    curr = stack.pop()
    values.append(curr.data)
    curr_sum += curr.data
    if curr.left:
      stack.append(curr.left)
    if curr.right:
      stack.append(curr.right)

    if curr.left is None and curr.right is None and curr_sum == target_sum:
      res.append(values)
      values = [root.data]
      curr_sum = root.data
      continue

    if curr.left is None and curr.right is None: # leaf node
      if curr_sum != target_sum:
        curr_sum -= curr.data
        values.pop()
  return res

if __name__ == '__main__':
  root = Tnode(5)
  root.left = Tnode(4)
  root.right = Tnode(8)

  root.left.left = Tnode(11)
  root.left.left.left = Tnode(7)
  root.left.left.right = Tnode(2)

  root.right.left = Tnode(13)
  root.right.right = Tnode(4)
  root.right.right.left = Tnode(5)
  root.right.right.right = Tnode(1)

  print(path_sumii(root, 22))
