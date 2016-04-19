import math

def has_factors_with_digits(n, d):
    fac1 = float(pow(10,d-1))
    while (fac1 < pow(10,d)):
        fac2 = n / fac1
        if (fac2 < pow(10,d-1)):
            return False
        elif (fac2 < pow(10,d) and math.floor(fac2) == fac2):
            return True
        fac1 += 1
    return False


def evenly_divisible(num, divisor):
    quotient = float(num) / divisior
    math.floor(quotient) == quotient

def is_root(n, r):
    root = n ** (1. / r)
    if (root == math.floor(root)):
        return True
    else:
        return False

def is_power(n):
    if (n < 4):
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2,sqrt+2):
        if (is_root(n, i)):
            return True
    return False

def is_prime(n):
    if (n <= 1):
        return False
    elif (n <= 3):
        return True
    elif (n % 2 == 0):
        return False
    elif (n % 3 == 0):
        return False
    i = 5
    while (i*i <= n):
        if (n % i == 0 or n % (i+2) == 0):
            return False
        i += 6
    return True

def next_prime(n):
    if n < 2:
        return 2
    elif n < 3:
        return 3
    if (n % 2 == 0):
        n += 1
    else:
        n += 2
    while (is_prime(n) == False):
        n += 2
    return n


def prime_factorization(n):
    prime_factors = {}
    i = 2
    while (n != 1):
        prime_factors[i] = 0
        while (n % i == 0):
            prime_factors[i] += 1
            n /= i
        i = next_prime(i)
    n_factors = {}
    for key in prime_factors:
        if (prime_factors[key] != 0):
            n_factors[key] = prime_factors[key]
    return n_factors

def prime_defactorization(factors):
    product = 1
    for prime, degree in factors.items():
        product *= pow(prime, degree)
    return product

def dict_merge(d1, d2):
    for key, val in d2.items():
        if key not in d1 or val > d1[key]:
            d1[key] = val
    return d1

def fib_seq(max, seq = [1,2]):
    if (seq[-1] > max):
        seq.pop()
        return seq
    else:
        seq.append(seq[-1] + seq[-2])
	return fib_seq(max, seq)

def evens_only(list):
    return [e for e in list if e % 2 == 0]


def is_palindrome(n):
    string = str(n)
    return string == string[::-1]

def square(n):
    return n*n
