from typing import List


def check(nums: List[int]):
  l, r = 0, len(nums)-1

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
  # main()
  print(check([3,2,6,9,8,8]))
