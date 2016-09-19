# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if n < 3:
    	return 1
    a = 1
    b = 1
    c = 0
    for i in range(2, n):
    	c = (a + b) % 10
    	a = b
    	b = c
    return c

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
