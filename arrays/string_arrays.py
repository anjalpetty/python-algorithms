

"""
leetcode 1189: Maximum number of Balloons
   Given a string text, you want to use the characters of text to form as many instances
   of the word "balloon" as possible.
   You can use each character in text at most once. Return the maximum number of instances
   that can be formed.
"""
from collections import defaultdict
def maxNumberOfBalloons(str) -> int:
    counts = defaultdict(int)
    for c in str:
        if c in ['b', 'a', 'l', 'o', 'n']:
            counts[c] += 1
    counts['l'] //= 2
    counts['o'] //= 2
    return min(counts['b'], counts['a'], counts['l'], counts['o'], counts['n'])


"""
Leetcode: 14. Longest Common Prefix
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    
    Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
"""
def longestCommonPrefix(strs) -> str:
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res


"""
Write a function which takes a String and shifts every character by k positions.
Note: The letters should wrap around the alphabets.
For example: if the letter is z and k = 2. after the shift the target character is b (z--> a--> b)

INPUT : xyz.    x-> y--> z, y--> z--> a, z--> a --> b
Expected OUTPUT: zab
"""
def caesarCypherEncrypt(s: str, key: int) -> str:
    key %= 26
    result = []
    for c in s:
        pos = ord(c) + key
        if pos > ord('z'):
            pos = ord('a') + (pos - ord('z'))-1
        result.append(chr(pos))
    return ''.join(result) # convert list to string


"""
leetcode: 3. Longest Substring Without Repeating Characters
  Given a string s, find the length of the longest substring without repeating characters.
  Input: s = "abcabcbb"
  Output: 3

  Input: s = "bbbbb"
  Output: 1

  Input: s = "pwwkew"
  Output: 3
"""


def longestSubString(s: str) -> int:
    hash = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in hash:
            hash.remove(s[l])
            l += 1

        hash.add(s[r])
        res = max(res, r-l+1)
    return res


if __name__ == '__main__':
    result = maxNumberOfBalloons("nlaebolko")
    print(f"max balloon of nlaebolko: {result}")
    result = maxNumberOfBalloons("loonbalxballpoon")
    print(f"max balloon of loonbalxballpoon: {result}")
    result = maxNumberOfBalloons("leetcode")
    print(f"max balloon of leetcode: {result}")

    result = longestCommonPrefix(["flower", "flow", "flight"])
    print(f"longest common prefix: {result}")

    result = caesarCypherEncrypt("xyz", 2)
    print(f"caesarCypher encrypt(xyz, 2): {result}")

    result = longestSubString("abcabcbb")
    print(f"longestSubString(abcabcbb): {result}")
    result = longestSubString("bbbbb")
    print(f"longestSubString(bbbbb): {result}")
    result = longestSubString("pwwkew")
    print(f"longestSubString(pwwkew): {result}")