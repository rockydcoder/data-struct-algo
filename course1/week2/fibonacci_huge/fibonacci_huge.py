# Uses python3
import sys

def get_fibonaccihuge(n, m):
    fibList = list()
    fibList.append(0)
    fibList.append(1)
    fibList.append(1)
    while True:
    	if fibList[len(fibList)-1] == 1 and fibList[len(fibList)-2] == 0:
    		break
    	fibList.append((fibList[len(fibList)-1] + fibList[len(fibList)-2]) % m)
    period =  len(fibList) - 2
    index = n % period
    return fibList[index]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
