import utils

def prob5():
    factors = {}
    for i in range(1,21):
        prime_factors = utils.prime_factorization(i)
        utils.dict_merge(factors, prime_factors)
    product = utils.prime_defactorization(factors)
    return product

print(prob5())
