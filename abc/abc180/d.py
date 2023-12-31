"""
・先にカコモンジムに通ってから、AtCoderジムに通うのが良いといえる
・強さがb増える=x+bをしてから、a倍するより先にa倍するほうが強さの増分が少なくて済むため
・なので、カコモンジムに通う回数を0回、1回、2回としたときを考えていき、Atcoderジムはその残り分だけ行うとする
・このときyの上限は10**18なので、最初の強さが1で全部カコモンジムにいったとしたときの通う回数を見積もってみる
・n回カコモンジムに通ったとすると、強さは(a**n)倍で、最大で10**18であるので(a**n)<=10**18である。
・これは、logを使ってn=とすると、n=log_a(10**18)となり、aの範囲からnは最大でも60くらいであるため、カコモンジムに通う回数を全探索できる
・以上より、カコモンジムに通う回数を決定し、進化しないように増やせる残りの強さを計算(このとき、経験値はカコモンジムに通う回数だけ増える)
・残りの強さをbで割った商がAtCoderジムに通える回数なのでその分だけ経験値を増やす。
・経験値が最大値を更新するなら更新
"""
x, y, a, b = map(int, input().split())

ans = -1
# カコモンジムに通う回数で全探索
for i in range(0, 100):
    if x*(a**i)>=y: break  #  カコモンジムにi回通ったあとの強さがy以上なら、break
    exp = i                #  経験値はカコモンジムに通った回数iだけ増加
    st = x*(a**i)          #  カコモンジムにi回通ったあとの強さの計算

    t = y-st-1             #  y以上にならないように増やせる残りの強さを計算
    exp += t//b            #  残りの強さをbで割った商だけAtCoderジムに通えるので、その分経験値を増やす
    ans = max(ans, exp)    #  ansが更新されるなら更新
    
print(ans)