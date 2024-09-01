"""
Leetcode 33: Search in a rotated sorted sorry
There is an integer array nums sorted in ascending order (with distinct values).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


def search(nums, target, left, right):
  if left > right:
    return -1

  mid = left + (right - left) // 2
  if target == nums[mid]:
    return mid

  # if left half is sorted
  if nums[mid] >= nums[left]:
    # if target is in the left half
    if nums[left] <= target <= nums[mid]:
      return search(nums, target, left, mid - 1)
    else:
      return search(nums, target, mid + 1, right)
  else:
    # if right half is sorted
    if nums[mid] <= target <= nums[right]:
      return search(nums, target, mid + 1, right)
    else:
      return search(nums, target, left, mid - 1)


if __name__ == '__main__':
  input1 = [4, 5, 6, 7, 0, 1, 2]
  print(search(input1, 0, 0, len(input1) - 1))  # expects 4

  input2 = [4, 5, 6, 7, 0, 1, 2]
  print(search(input2, 3, 0, len(input2) - 1))  # expects -1
