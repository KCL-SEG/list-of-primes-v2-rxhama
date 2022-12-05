"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f'Argument: {number_of_primes} cannot be 0 or negative!')
    list = []
    num = 2
    while(len(list) < number_of_primes):
        if is_prime(num):
            list.append(num)
        num += 1

    return list

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
