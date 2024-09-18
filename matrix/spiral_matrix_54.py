"""
Leetcode:54 Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
output: [1,2,3,6,9,8,7,4,5]
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
  res = []
  row_len = len(matrix)
  col_len = len(matrix[0])
  for row in range(row_len):
    # top right
    for col in range(row, col_len-row):
      res.append(matrix[row][col])

    # right bottom
    for col in range(row+1, col_len-row):
      res.append(matrix[col][col_len-1-row])

    # bottom left
    for col in range(row+1, col_len-row):
      res.append(matrix[col_len-1-row][col_len-1-col])

    # bottom top
    for col in range(row+1, col_len-row-1):
      res.append(matrix[row_len-1-col][row])

  return res

if __name__ == '__main__':
  matrix = [[1,2,3],[4,5,6],[7,8,9]]
  print(spiral_order(matrix))
