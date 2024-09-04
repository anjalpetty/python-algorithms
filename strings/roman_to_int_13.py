
"""
Leetcode: 13 Romain to Integer

"""

def roman_to_int(s: str) -> int:

  hash = {'I': 1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}

  res = 0
  i = 0
  while i < len(s):
    if i+1 < len(s) and s[i:i+2] in hash:
      res += hash[s[i:i+2]]
      i += 2
    else:
      res += hash[s[i]]
      i += 1
  return res

if __name__ == '__main__':
  print('romain to int(III)    :', roman_to_int('III'))    # expect 3
  print('romain to int(LVIII)  :', roman_to_int('LVIII'))  # expect 58
  print('romain to int(MCMXCIV):', roman_to_int('MCMXCIV'))# expect 1994