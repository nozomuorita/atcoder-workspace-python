"""
・aとして考えられるのは10**4までそれ以上だと、制約を超える
・よって、aを1から10**4まで回す
・もしkをaで割った余りが0でないなら式が成立しないので飛ばす
・aで割った余りが0の場合、bc=k//aとなる
・ここで、bとして成立する値は√(k//a)までである。bがこれを超えるとb<=cなので式が成立しなくなる
・よって、bを√(k//a)まで繰り返す
・このとき、cはk//(a*b)となる(割り切れないなら飛ばす)
・最後にa<=b<=cを満たすならansをインクリメント
"""
k = int(input())

ans = 0
for a in range(1, 10**4+1):
    if k%a!=0: continue
    for b in range(1, int((k//a)**0.5)+1):
        if k%(a*b)!=0: continue
        c = k//(a*b)
        if a<=b<=c: ans+=1
        
print(ans)