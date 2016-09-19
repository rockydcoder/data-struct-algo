# Uses python3
import sys

def optimal_summands(n):
    summands = []
    l = 1
    while n > l * 2:
    	summands.append(l)
    	n -= l
    	l += 1
    summands.append(n)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
