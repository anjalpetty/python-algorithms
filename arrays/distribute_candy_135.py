"""
leetcode:135 Candy
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

e.g: input [1, 2]
output 3 (1+2)

input [1, 5, 2, 1]
output 7 (1 + 3 + 2 + 1)

input [7, 3, 1, 5, 3]
output 9 (3 + 2 + 1 + 2 + 1)
"""


def candy(ratings):
  left = [1] * len(ratings)
  right = [1] * len(ratings)
  for i in range(1, len(ratings)):
    if ratings[i] > ratings[i - 1]:
      left[i] = left[i - 1] + 1
  for i in range(len(ratings) - 2, -1, -1):
    if ratings[i] > ratings[i + 1]:
      right[i] = right[i + 1] + 1
  candies = 0
  for n in range(0, len(ratings)):
    candies += max(left[n], right[n])
  return candies


if __name__ == '__main__':
  print("Candies required: " + str(candy([1, 3, 2])))  # expects 4
  print("Candies required: " + str(candy([1, 5, 2, 1])))  # expects 7
  print("Candies required: " + str(candy([7, 3, 1, 5, 3])))  # expects 9
  print("Candies required: " + str(candy([1, 2, 6, 5, 4, 3, 1])))  # expects 18
