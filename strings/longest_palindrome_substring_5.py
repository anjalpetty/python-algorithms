"""
Leetcode: 5 Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input : s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input : s = "cbbd"
Output: "bb"

"""

def longest_palindrome(s: str) -> str:
  res = ""
  res_len = 0
  for i in range(len(s)):
    # odd length
    l, r = i, i
    while l>=0 and r < len(s) and s[l] == s[r]:
      if (r-l+1) > res_len:
        res = s[l:r+1]
        res_len = r-l+1
      l, r = l-1, r+1
    # even length
    l, r = i, i+1
    while l>=0 and r < len(s) and s[l] == s[r]:
      if (r-l+1) > res_len:
        res = s[l:r+1]
        res_len = r-l+1
      l, r = l-1, r+1
  return res

if __name__ == '__main__':
  print(longest_palindrome("babad")) # expect aba
  print(longest_palindrome("cbbd")) # expect bb
