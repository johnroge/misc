


def fib(limit):
    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        yield current


print('with yield')
for n in fib(3000):
    print(n, end=', ')


