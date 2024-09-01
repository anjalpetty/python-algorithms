"""
Leetcode: 283: Move Zeros

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


def move_zeros(nums):
  cnt = 0
  for i in range(0, len(nums)):
    if nums[i] != 0:
      nums[cnt] = nums[i]
      cnt += 1

  for i in range(cnt, len(nums)):
    nums[i] = 0

  return nums


if __name__ == '__main__':
  print(move_zeros([0, 1, 0, 3, 12]))
