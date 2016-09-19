# Uses python3
def calc_fib(n):
    if n < 2:
        return n
    a = 0
    b = 1 
    c = 0
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return c
n = int(input())
print(calc_fib(n))
