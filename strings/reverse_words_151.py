"""
Leetcode: 151 reverse words in a string
Given an input string s, reverse the order of the words.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""
from collections import deque


def reverse_words(s: str) -> str:
  d = deque()
  start = -1
  i = 0
  while i < len(s):
    if s[i] != ' ':
      start = i
      while i < len(s) and s[i] != ' ':
        i += 1
      d.appendleft(s[start: i])
    i += 1
  return " ".join(d)


if __name__ == '__main__':
  print('['+reverse_words("the sky is blue")+']')
  print('['+reverse_words("  hello world  ") +']')
  print('['+reverse_words("a good   example")+']')