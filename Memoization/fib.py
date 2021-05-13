import gc
def fib(n):
    if n <= 1:
        return 1
    memoi = [0 for i in range(n+1)]
    memoi[1] = 1
    for i in range(2, n+1):
        memoi[i] = memoi[i-1] + memoi[i-2]
    return memoi[n]

print(fib(8))
print(fib(9))
print(fib(150))

gc.collect()