"""
Leetcode: 88 Merge sorted array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n
input : [1,2,3,0,0,0], [2, 5, 6]
output: [1, 2, 2, 3, 5, 6]
"""
from typing import List


def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int):
  last = m + n -1

  while m > 0 and n > 0:
    if nums1[m-1] > nums2[n-1]:
      nums1[last] = nums1[m-1]
      m -= 1
    else:
      nums1[last] = nums2[n-1]
      n -= 1
    last -= 1

  while n > 0:
    nums1[last] = nums2[n-1]
    n, last = n-1, last-1

  return nums1


if __name__ == '__main__':
  print(f"merge two sorted arrays: {merge_sorted_arrays([1,2,3,0,0,0], 3, [2,5,6], 3)}")
