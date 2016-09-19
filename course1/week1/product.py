# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
maxIndex1 = 0
maxIndex2 = 0
maxInt1 = 0
maxInt2 = 0
for i in range(0, n):
	if a[i] > maxInt1:
		maxInt1 = a[i]
		maxIndex1 = i

for i in range(0, n):
	if a[i] > maxInt2 and i != maxIndex1:
		maxInt2 = a[i]
		maxIndex2 = i

result = maxInt1 * maxInt2
print(result)
