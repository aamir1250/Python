def fib(n, mem=None):

    if mem is None:
        mem = [-1] * (n + 1)

    if n <= 1:
        return n

    if mem[n] != -1:
        return mem[n]

    mem[n] = fib(n - 1, mem) + fib(n - 2, mem)

    return mem[n]


for i in range(10):
    print(fib(i))
