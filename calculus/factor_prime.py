"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

from math import log, ceil

def factorPrime(number):    
    i = 2  
    count = 0  
    while i < number:
        if number % i == 0:
           number = number / i
        else:
            i += 1
    return int(number)

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False

def upper_bound_for_p_n(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))

def find_n_prime(n):
    primes = list(find_primes(upper_bound_for_p_n(n)))
    return primes[n - 1]

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
def sum_primes(n):
    prime = [True] * (n + 1)
    s = 2
    while s * s <= n:
        if prime[s] == True:
            i = s * 2
            while i <= n:
                prime[i] = False
                i += s
        s = s + 1
    sum = 0
    for i in range (2, n + 1):
        if(prime[i]):
            sum = sum + i
    return sum


