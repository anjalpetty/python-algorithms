"""
Leetcode: 7 reverse integer
Given a signed 32-bit integer x, return x with its digits reversed.
If it goes outside of signed 32-bit range, return 0

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

def reverse(x: int) -> int:

  if x < 0:
    symbol = -1
  else:
    symbol = 1

  x = abs(x)
  res = 0
  while x > 0:
    res = (res * 10) + (x % 10)
    x //= 10

  # return res
  return 0 if res > 2**31 else res*symbol


if __name__ == '__main__':
  print(reverse(123))   # expects 321
  print(reverse(-123))  # expects -321
  print(reverse(120))   # expects 21