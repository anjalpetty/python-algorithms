
"""
leetcode: 13, roman to int
input: MCMXCIV
output: 1994
"""

def romanToInt(str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(str)):
        if i + 1 < len(str) and roman[str[i]] < roman[str[i+1]]:
            result -= roman[str[i]]
        else:
            result += roman[str[i]]
    return result

"""
leetcode: 12, int to roman
input: 1994
output: MCMXCIV
"""
def intToRoman(num: int) -> str:
    d = {1000: 'M',
         900: 'CM',
         500: 'D',
         400: 'CD',
         100: 'C',
         90: 'XC',
         50: 'L',
         40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    res = ""
    for i in d:
        res += (num//i) * d[i]
        num %= i
    return res


if __name__ == '__main__':
    result = romanToInt("MCMXCIV")
    print(f"roman to int: {result}")

    result = intToRoman(1994)
    print(f"int to roman: {result}")