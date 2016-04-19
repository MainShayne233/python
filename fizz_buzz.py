def fizz_buzz(n):
    key = sum([int(not bool(n%3))*2, int(not bool(n%5))*3])
    dict = {0: str(n), 2: 'fizz', 3: 'buzz', 5: 'fizzbuzz'}
    return dict[key]

print "\n".join(map(fizz_buzz, range(1,100)))
