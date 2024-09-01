"""

Leetcode: 167
find the indices of two numbers add up to a target
given array is sorted in ascending order
NOTE: the array is sorted in ascending order

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6, Therefore index1 = 1, index2 = 3. We return [1, 3].
"""


def two_sumii(nums, target):
  left, right = 0, len(nums) - 1
  while left < right:
    val = nums[left] + nums[right]
    if val > target:
      right -= 1
    elif val < target:
      left += 1
    else:
      return [left + 1, right + 1]
  return []


if __name__ == '__main__':
  print(two_sumii([1, 3, 4, 5, 7, 10, 11], 9))
