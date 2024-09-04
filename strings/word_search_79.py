
"""
Leetcode: 79. Word Search

Input: board =
[
 ["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]
]
word = "ABCCED", return true

word = "SEE, return true
word "ABCB", return false

Constraints:
1. You can move in 4 directions (left, right, top, bottom)
2. A node once traversed cannot re-traversed
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == word[0] and dfs_around(board, word, 0, i, j):
        return True
  return False

def dfs_around(board: List[List[str]], word: str, ind:  int, row: int, col: int):
  if ind == len(word):
    return True

  if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[ind]:
    return False

  tmp = board[row][col]
  board[row][col] = ' '
  found: bool = (dfs_around(board, word, ind+1, row+1, col)
                 or dfs_around(board, word, ind+1, row-1, col)
                 or dfs_around(board, word, ind+1, row, col+1)
                 or dfs_around(board, word, ind+1, row, col-1))
  board[row][col] = tmp
  return found

if __name__ == '__main__':
  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
  print("exist(ABCCED):", exist(board, "ABCCED"))
  print("exist(SEE)   :", exist(board, "SEE"))
  print("exist(ABCB)  :", exist(board, "ABCB"))
