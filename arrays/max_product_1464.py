"""
Leetcode: 1464. Maximum product of two elements in an array
Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0),
you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
"""


def max_product(nums):
  first_max = second_max = 0
  for i in range(0, len(nums)):
    if nums[i] > first_max:
      second_max = first_max
      first_max = nums[i]
    elif nums[i] > second_max:
      second_max = nums[i]
  return (first_max - 1) * (second_max - 1)


if __name__ == '__main__':
  print(max_product([3, 4, 5, 2]))
