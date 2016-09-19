# Uses python3
import sys

def get_change(n):
    denoms = [10, 5, 1]
    counter = 0
    for denom in denoms:
    	counter += n // denom
    	n = n % denom
    return counter

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
