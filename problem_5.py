"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# 1 is obv
# 4,8 -> 2
# 6 if 2 and 3
# 12 if 3 and 4
# 14 if 2 and 7
# 15 if 3 and 5
# 18 if 2 and 9

#naive solution

def is_divisible(n):
    return n%3==0 and n%4==0 and n%5==0 and n%6==0 and n%7==0 and n%8==0 and n%9==0 and n%10==0 and n%11==0 and n%13==0 and n%16==0 and n%17==0 and n%19==0 and n%20==0


def smallest_pos():
    for n in range(2522, 1000000000, 2):
        if is_divisible(n):
            return n


print(smallest_pos()) #232792560
