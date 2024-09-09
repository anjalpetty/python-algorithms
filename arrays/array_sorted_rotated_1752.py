
"""
Leetcode: 172, Check if array is sorted and rotated
Given an array, return true if the array was sorted and then rotated. False otherwise
Example: 1
input : nums = [3,4,5,1,2]
output: true

Example: 2
input : nums[2,1,3,4]
output: false

Example: 3
input : nums[1,2,3]
output: true
"""

from typing import List

def check(nums: List[int]):

  count = 0
  for i in range(0, len(nums)):
    if nums[i] > nums[(i+1) % len(nums)]:
      count += 1
    if count > 1:
      return False
  return True

def main():
  for i in range(0, 5):
    print('hello')


if __name__ == '__main__':
  print(check([3,4,5,1,2])) # expects true
  print(check([2,1,3,4])) # expects false
  print(check([1,2,3])) # expects true
