
"""
Leetcode 14 - Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input : strs = ["flower","flow","flight"]
Output: fl

Example 2:
Input : strs = ["dog","racecar","car"]
Output: ""
"""

def longest_common_prefix(strs) -> str:
  res = ""
  for i in range(len(strs[0])):
    for s in strs:
      if i == len(s) or s[i] != strs[0][i]:
        return res
    res += strs[0][i]
  return res


if __name__ == '__main__':
  print(f"output: {longest_common_prefix(["flower", "flow", "flight"])}")
  print(f"output: {longest_common_prefix(["dog", "racecar", "car"])}")