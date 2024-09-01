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

  # signed = False
  # if x < 0:
  #   signed = True
  # x = abs(x)

  if x < 0:
    symbol = -1
  else:
    symbol = 1

  MIN = -2 ^ 31
  MAX = 2 ^ 31 - 1
  res = 0
  while x > 0:
    res = (res * 10) + (x % 10)
    x //= 10
    # if res > MAX or res <MIN:
    #   return 0


  # if signed:
  #   res = -1 * res

  # return res
  return 0 if res > 2**31 else res*symbol


if __name__ == '__main__':
  print(reverse(123))   # expects 321
  print(reverse(-123))  # expects -321
  print(reverse(120))   # expects 21