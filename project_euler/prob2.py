import utils

def prob2():
    seq = utils.fib_seq(4*pow(10,6))
    seq = utils.evens_only(seq)
    return sum(seq)

print(prob2())
