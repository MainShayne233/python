import utils

def prob6():
    sum_of_squares = sum(map(utils.square, range(1,101)))
    square_of_sums = utils.square(sum(range(1,101)))
    return abs(sum_of_squares - square_of_sums)


print(prob6())
