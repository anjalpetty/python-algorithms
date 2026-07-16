"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""

def missing_number(nums):
  result = len(nums)
  for i in range(len(nums)):
    result += (i-nums[i])
  return result

## TIP: xor with all numbers in the range along with the position of the number will get the missing number
def missing_number_xor(nums):
  result = len(nums)
  for i in range(len(nums)):
    result ^= i ^ nums[i]
  return result

if __name__ == '__main__':
  print(missing_number_xor([3,0,1]))
  print(missing_number_xor([0,1]))
  print(missing_number_xor([9,6,4,2,3,5,7,0,1]))