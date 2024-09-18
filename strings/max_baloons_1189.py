
"""
Leetcode 1189: Maximum number of Balloons
   Given a string text, you want to use the characters of text to form as many instances
   of the word "balloon" as possible.
   You can use each character in text at most once. Return the maximum number of instances
   that can be formed.
"""
from collections import defaultdict
def max_number_of_balloons(str) -> int:
  counts = defaultdict(int)
  for c in str:
    if c in ['b', 'a', 'l', 'o', 'n']:
      counts[c] += 1
  counts['l'] //= 2
  counts['o'] //= 2
  return min(counts['b'], counts['a'], counts['l'], counts['o'], counts['n'])

# solution without using any dictionary
def max_number_of_balloons(s):
  arr = [0] * 26 # initialize array with zero
  for i in range(len(s)):
    p = ord(s[i]) - ord('a')
    arr[p] += 1

  return min(arr[1], arr[0], arr[11]//2, arr[14]//2, arr[13])

if __name__ == '__main__':
  print("max baloons[nlaebolko]: " + str(max_number_of_balloons("nlaebolko"))) # expect 1
  print("max baloons[loonbalxballpoon]: " + str(max_number_of_balloons("loonbalxballpoon"))) # expect 2
  print("max baloons[leetcode]: " + str(max_number_of_balloons("leetcode"))) # expect 0