h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = 0
# 各マスについて、右と下をみる
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            continue
        if (j+1<=w-1) and (s[i][j+1])=='.':
            ans += 1
        if (i+1<=h-1) and (s[i+1][j])=='.':
            ans += 1
            
print(ans)