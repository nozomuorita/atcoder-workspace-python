k, s = map(int, input().split())
ans = 0

for i in range(k+1):
    for j in range(k+1):
        z = s - i - j
        if 0<=z<=k: ans+=1

print(ans)