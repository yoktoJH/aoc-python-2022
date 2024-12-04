def fib_rec(n):
    if n == 1:
        return (1, 0)
    pred, pred2 = fib_rec(n - 1)
    return pred + pred2, pred


def fib(n):
    return fib_rec(n)[0]


assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(5) == 5
assert fib(9) == 34
assert fib(11) == 89
assert fib(20) == 6765
assert fib(40) == 102334155
print(fib(2 ** 2 ** 20))
