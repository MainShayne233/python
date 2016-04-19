import utils

# Version 1.0

# def prob4():
#     largest = 0
#
#     for i in range(100,1000):
#         for j in range(100,1000):
#             prod = i*j
#             if (utils.is_palindrome(prod) and prod > largest):
#                 largest = prod
#     return largest

def prob4():
    start = 999*999
    while (True):
        start -= 1
        if (utils.is_palindrome(start) and utils.has_factors_with_digits(start, 3)):
            return start

print(prob4())
