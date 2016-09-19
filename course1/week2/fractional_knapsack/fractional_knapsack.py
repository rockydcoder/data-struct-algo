# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
    opt_value = 0
    vAndW = list()
    for weight, value in zip(weights, values):
        vAndW.append((value, weight))
    vAndW.sort(key = lambda tup: tup[0]/tup[1], reverse = True)
    for elem in vAndW:
        if capacity == 0:
            return opt_value
        w = min(elem[1], capacity)
        opt_value += elem[0]*w/elem[1]
        capacity -= w
    return opt_value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
