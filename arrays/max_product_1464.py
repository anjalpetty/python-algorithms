"""
Leetcode: 1464. Maximum product of two elements in an array
Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0),
you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
"""


def max_product(nums):
  max1 = max2 = 0
  for n in nums:
    if n > max1:
      max2 = max1
      max1 = n
    elif n > max2:
      max2 = n
  return (max1 - 1) * (max2 - 1)


if __name__ == '__main__':
  print(max_product([3, 4, 5, 2]))
