"""
Leetcode:54 Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
output: [1,2,3,6,9,8,7,4,5]
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:

  res = []
  left, right = 0, len(matrix[0])
  top, bottom = 0, len(matrix)

  while left < right and top < bottom:
    # left to right
    for i in range(left, right):
      res.append(matrix[top][i])
    top += 1

    # top to bottom
    for i in range(top, bottom):
      res.append(matrix[i][right-1])
    right -= 1

    if not (left < right and top < bottom):
      break

    # right to left
    for i in range(right-1, left-1, -1):
      res.append(matrix[bottom-1][i])
    bottom -= 1

    # bottom to top
    for i in range(bottom-1, top-1, -1):
      res.append(matrix[i][left])
    left += 1

  return res

if __name__ == '__main__':
  matrix = [[1,2,3],[4,5,6],[7,8,9]]
  print(spiral_order(matrix))
  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  print(spiral_order(matrix))
