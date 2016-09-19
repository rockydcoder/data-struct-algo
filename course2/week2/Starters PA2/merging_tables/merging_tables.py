# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    if rank[realDestination] >= rank[realSource]:
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        parent[realSource] = realDestination
        global ans
        if ans < lines[realDestination]:
            ans = lines[realDestination]

    else:
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
        parent[realDestination] = realSource
        global ans
        if ans < lines[realSource]:
            ans = lines[realSource]

    if rank[realSource] == rank[realDestination]:
        rank[realDestination] += 1

    return True

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
    
