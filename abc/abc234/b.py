n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = -1

for i in range(n):
    for j in range(i+1, n):
        d = ((xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2) ** 0.5
        if d > ans:
            ans = d

print(ans)