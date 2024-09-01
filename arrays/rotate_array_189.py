"""
Leetcode: 189, Rotate Array
Given an integer array nums, rotate the array to the right by k

Example 1:
input : [1,2,3,4,5,6,7], k=3
output: [5,6,7,1,2,3,4]

Example 2:
input : [-1,-100,3,99], k=2
output: [3,99,-1,-100]
"""

def reverse(nums, left, right):
  while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left, right = left+1, right-1

def rotate(nums, k):
  k = k % len(nums)
  reverse(nums, 0, len(nums)-1)
  reverse(nums, 0, k-1)
  reverse(nums, k, len(nums)-1)

  return nums

if __name__ == '__main__':
  print(rotate([1,2,3,4,5,6,7], 3))
  print(rotate([-1,-100,3,99], 2))