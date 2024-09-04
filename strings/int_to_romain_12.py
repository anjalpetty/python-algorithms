
"""
Leetcode: 12 Integer to Roman

Example 1
Input : num = 3749
Output: "MMMDCCXLIX"

Example 2:
Input : num = 58
Output: "LVIII"

Example 3:
Input : num = 1994
Output: "MCMXCIV"
"""

def int_to_romain(num: int):
  hash = {1: 'I', 4: 'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900: 'CM', 1000:'M'}

  res=""
  for k,v in reversed(hash.items()):
    count = num // k
    while count > 0:
      res = res + v
      count -= 1
    num %= k
  return res

if __name__ == '__main__':
  print("intToRomain(3749):", int_to_romain(3749)) # expect MMMDCCXLIX
  print("intToRomain(58)  :", int_to_romain(58))   # expect LVIII
  print("intToRomain(1994):", int_to_romain(1994)) # expect MCMXCIV
