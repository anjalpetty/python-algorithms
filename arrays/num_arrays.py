# sum of two array elements matching to target
def two_sum(nums, target) -> []:
    num_dict = {}
    for i, n in enumerate(nums):
        value = target - n
        if value in num_dict:
            return [i, num_dict[value]]
        num_dict[n] = i
    return []


"""
leetcode: 167 Two Sum II - Input Array is sorted find the 
indices of two numbers add up to a target given array is sorted in ascending order
NOTE: the array is sorted in ascending order this differs from above approach
"""
def two_sum_2(nums, target) -> []:
    left, right = 0, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            return [left+1, right+1]
    return []


"""
leetcode 121. best time to buy and sell stock, return maximum profit, 0 otherwise
"""
def max_profit(price):
    buy = price[0]
    profit = 0
    for i in range(1, len(price)):
        if price[i] < buy:
            buy = price[i]
            continue
        cur_profit = price[i] - buy
        profit = max(cur_profit, profit)
    return profit

"""
leetcode: 1464: maximum product of two elements in an array
"""
def max_product(nums):
    return 0

"""
The solution should maintain the relative order of items in the array 
and should not use constant space.
"""
def move_zeros_right(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    while count < len(nums):
        nums[count] = 0
        count += 1
    return nums


"""
leetcode: 53 Maximum subarray
Given an int array nums, find the continuous subarray which has the largest sum, return sum
input : [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output: 6
"""

def max_sub_array(nums) -> int:
    max_sub = nums[0]
    cur_sum = 0
    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sub = max(max_sub, cur_sum)
    return max_sub


"""
leetcode: 152. Max product sub array
find continous subarray within an array which has largest product
input: [2, 3, -1, 4]
output: 6
"""
def max_prod_sub_array(nums) -> int:
    max_sub = nums[0]
    # TODO
    return max_sub

"""
leetcode: 153. Find Minimum in Rotated Sorted Array
   find minimum in O(log n) times in a rotated sorted array
   Input: nums = [3,4,5,1,2]
   Output: 1
   Explanation: The original array was [1,2,3,4,5] rotated 3 times.

   Input: nums = [4,5,6,7,0,1,2]
   Output: 0
   Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
"""
def find_min(nums) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l)//2
        if nums[mid] < nums[r]:
            r = mid
        elif nums[mid] > nums[r]:
            l = mid+1
    return nums[l]

"""
leetcode: 33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
input: [4, 5, 6, 7, 0, 1, 2], 0
output: True
"""
def search_rotated_sorted_array(nums, key) -> int:
    l, r = 0, len(nums) -1

    while l < r:
        m = l + int((r-l)/2)
        if key == nums[m]:
            return m
        if nums[m] > key:
            l = m
        elif nums[m] < key:
            r = m-1
        else:
            return m

"""
rotate count [9, 2, 3, 5, 7]
[ 7, 6, 5, 1, 2, 3, 4]
[1, 2, 3, 4, 5, 6, 7]
"""
def rotateCount(nums):
    count = 0
    # left, right = 0, len(nums)-1
    # while left < right:
    #     if nums[left] > nums[right]:
    #         count += 1
    #     left += 1
    # return count
    min = nums[0]
    min_index = 0
    for i in range(0, len(nums)-1):
        if min > nums[i]:
            min = nums[i]
            min_index = i
    return min_index



"""
leetcode: 189. Rotate array
Given an integer array nums, rotate the arraty to right by k steps
approach: reverse entire array, split array k position, reverse each two sub array
input: nums=[1, 2, 3, 4, 5, 6, 7, 8], k=3
output: [6, 7, 8, 1, 2, 3, 4, 5]
"""

def rotate(nums, k):
    k = k % len(nums)
    nums = reverse(nums, 0, len(nums)-1)
    nums = reverse(nums, 0, k-1)
    nums = reverse(nums, k, len(nums)-1)
    return nums


def reverse(nums, start, end):
    left, right = start, end
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left+1, right-1
    return nums


"""
merge two sorted arrays
input : [0, 1, 3, 4, 8, 9], [2, 5, 6, 7]
output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
def mergeSortedArrays(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
    # left over
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result


"""
leetcode: 217: Contains duplicate
input: [1, 2, 3, 1]
output: True
"""

def containsDuplicate(nums):
    hash = set()
    for n in nums:
        if n in hash:
            return True
        hash.add(n)
    return False


if __name__ == '__main__':
    result = two_sum([8, 9, 5, 1, 0, 4, 7], 12)
    print(f"two sum - {result}")

    result = two_sum_2([1, 3, 4, 5, 7, 10, 11], 9)
    print(f"two sum II - {result}")

    result = max_profit([7, 1, 5, 3, 6, 4])
    print(f"max profit: {result}")

    result = max_product([-10, -3, 5, 6, -2])
    print(f"max product of two array: {result}")

    result = move_zeros_right([6, 0, 8, 2, 3, 0, 4, 0, 1])
    print(f"move zeros right {result}")

    result = max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(f"max sub array: {result}")

    # result = max_prod_sub_array([2, 3, -1, 4])
    # print(f"max prod sub array: {result}")

    result = find_min([3, 4, 5, 1, 2])
    print(f"min in rotated sorted array: {result}")

    result = search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0)
    print(f"search in rotated sorted array: {result}")

    result = rotateCount([9, 2, 3, 5, 7])
    print(f"rotate count: {result}")

    result = rotate([1, 2, 3, 4, 5, 6, 7, 8], 3)
    print(f"rotate an array k positions: {result}")

    result = mergeSortedArrays([0, 1, 3, 4, 8, 9], [2, 5, 6, 7])
    print(f"merge two sorted arrays: {result}")

    result = containsDuplicate([1, 2, 3, 1])
    print(f"contains duplicate: {result}")
