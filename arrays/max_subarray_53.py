"""
Leetcode: 53. Maximum subarray

Given an integer array nums, find the subarray with the largest sum

Example 1:
input : nums[-2,1,-3,4,-1,2,1,-5,4]
output: 6

Example 2:
input : nums[1]
output: 1
"""


def max_subarray(nums):
  max_value = nums[0]
  curr_sum = 0
  for i in range(0, len(nums)):
    if curr_sum < 0:
      curr_sum = 0
    curr_sum += nums[i]
    max_value = max(max_value, curr_sum)
  return max_value


if __name__ == '__main__':
  print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expects 6
  print(max_subarray([1]))  # expects 1
  print(max_subarray([5, 4, -1, 7, 8]))  # expects 23
