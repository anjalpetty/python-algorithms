"""
Leetcode: 152. Maximum product subarray
Given an integer array, find the continuous subarray that has the largest product

Example: 1
input : nums=[2,3,-2,4]
output: 6
Example: 2
input : nums=[-2,0,-1]
output: 0
"""


def max_product_subarray(nums):
  max_product = nums[0]
  left_product = 1
  right_product = 1
  for i in range(0, len(nums)):
    if left_product == 0:
      left_product = 1
    if right_product == 0:
      right_product = 1

    left_product *= nums[i]
    right_product *= nums[len(nums) - 1 - i]
    max_product = max(max_product, left_product, right_product)

  return max_product


if __name__ == '__main__':
  print(max_product_subarray([2, 3, -2, 4]))  # expects 6
  print(max_product_subarray([-2, 0, -1]))  # expects 0
