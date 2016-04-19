import utils

def prob3():
    prime_factors = utils.prime_factorization(600851475143)
    return list(prime_factors)[0]

print(prob3())
