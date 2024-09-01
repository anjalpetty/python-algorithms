"""
Write a function which takes a String and shifts every character by k positions.
Note: The letters should wrap around the alphabets.
For example: if the letter is z and k = 2. after the shift the target character is b (z--> a--> b)

INPUT : xyz.    x-> y--> z, y--> z--> a, z--> a --> b
Expected OUTPUT: zab
"""
def caesar_cypher_encrypt(s: str, key: int) -> str:
  key %= 26
  result = []
  for c in s:
    pos = ord(c) + key
    if pos > ord('z'):
      pos = ord('a') + (pos - ord('z'))-1
    result.append(chr(pos))
  return ''.join(result) # convert list to string

if __name__ == '__main__':
  print(f"output: {caesar_cypher_encrypt("xyz", 2)}") # expect zab
  print(f"output: {caesar_cypher_encrypt("car", 5)}") # expect hfw