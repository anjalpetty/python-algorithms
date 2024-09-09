"""
Leetcode: 1913. Maximum Product Difference Between Two Pairs

Hint
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
"""


def max_prod_difference(nums):
  max1 = max2 = 0  # first and second largest
  min1 = min2 = float("inf")  # smallest and second smallest

  for n in nums:
    if n > max1:
      max2 = max1
      max1 = n
    elif n > max2:
      max2 = n

    if n < min2:
      min1 = min2
      min2 = n
    elif n < min1:
      min1 = n
  return (max1 * max2) - (min1 * min2)


if __name__ == '__main__':
  print(max_prod_difference([5, 6, 2, 7, 4]))  # expects 64 (6 * 7) - (2 * 4) => 42 - 8 => 34
