H, W = map(int, input().split())
S = []
for i in range(H):
    s = input()
    S.append(s)
    
koma = []
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            koma.append([i, j])
            
print(abs(koma[0][0] - koma[1][0]) + abs(koma[0][1] - koma[1][1]))