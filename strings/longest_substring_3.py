"""
Leetcode: 3. Longest Substring Without Repeating Characters
  Given a string s, find the length of the longest substring without repeating characters.
  Input: s = "abcabcbb"
  Output: 3

  Input: s = "bbbbb"
  Output: 1

  Input: s = "pwwkew"
  Output: 3
"""
from collections import deque

# better solution using deque
def longest_substring(s: str) -> int:
  res = 0
  d = deque()
  for i in range(len(s)):
    while s[i] in d:
      d.popleft()
    d.append(s[i])
    res = max(res, len(d))
  return res


def longest_sub_string(s: str) -> int:
  hash = set()
  l = 0
  res = 0
  for r in range(len(s)):
    while s[r] in hash:
      hash.remove(s[l])
      l += 1

    hash.add(s[r])
    res = max(res, r - l + 1)
  return res


if __name__ == '__main__':
  print(f"longest_sub_string(abcabcbb): {longest_substring("abcabcbb")}")  # expect 3
  print(f"longest_sub_string(bbbbb): {longest_sub_string("bbbbb")}") # expect 1
  print(f"longest_sub_string(pwwkew): {longest_sub_string("pwwkew")}") # expect 3
