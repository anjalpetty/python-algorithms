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

ratings = [1, 5, 2, 1]
# ratings = [7, 3, 1, 5, 3]
candy = [1] * len(ratings)
for index in range(1, len(ratings)):
    if ratings[index] > ratings[index-1]:
        candy[index] = 1 + candy[index-1]

for index in range(len(ratings)-2, -1, -1):
    if ratings[index] > ratings[index+1]:
        candy[index] = max(candy[index], candy[index+1] + 1)

print(sum(candy))

