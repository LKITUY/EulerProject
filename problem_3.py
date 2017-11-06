'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?'''


def largest_prime_factor(n):
    factors = []
    num = n
    for p in range(2, n):
        while num % p == 0:
            factors.append(p)
            num /= p
        if num <= 1:
            break
    return factors[-1]


number = 600851475143
print(largest_prime_factor(number)) #6857
