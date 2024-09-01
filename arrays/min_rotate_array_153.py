"""
Leetcode: 153, Find minimum in a rotated sorted array
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
"""


def find_min(nums):
  res = nums[0]
  left, right = 0, len(nums) - 1

  while left <= right:
    if nums[left] < nums[right]:
      res = min(res, nums[left])
      break
    mid = left + (right - left) // 2
    res = min(res, nums[mid])
    if nums[mid] >= nums[left]:
      left = mid + 1
    else:
      right = mid - 1
  return res


if __name__ == '__main__':
  print(find_min([3, 4, 5, 1, 2]))  # expect 1
  print(find_min([4, 5, 6, 7, 0, 1, 2]))  # expect 0
