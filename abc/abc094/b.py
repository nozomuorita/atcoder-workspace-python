n, m, x = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, 0
for i in range(m):
    if a[i]<x: left+=1
    else: right+=1

print(min(left, right))