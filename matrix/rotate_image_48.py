"""
Leetcode: 48, rotate image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]

Output:
[[7,4,1],
 [8,5,2],
 [9,6,3]]
"""

def transpose(matrix):
  for i in range(len(matrix)):
    for j in range(i+1, len(matrix[i])):
      t = matrix[i][j]
      matrix[i][j] = matrix[j][i]
      matrix[j][i] = t
  return matrix


def rotate(matrix):
  matrix = transpose(matrix)
  col_len = len(matrix[0])
  for i in range(len(matrix)):
    for j in range(col_len//2):
      t = matrix[i][j]
      matrix[i][j] = matrix[i][col_len-j-1]
      matrix[i][col_len-j-1] = t
  return matrix

if __name__ == '__main__':

  matrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]
  matrix = rotate(matrix)
  print(matrix)