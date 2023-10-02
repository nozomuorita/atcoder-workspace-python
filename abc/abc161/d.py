# ルンルン数を列挙していく
import sys
sys.setrecursionlimit(1000000)

K = int(input())
ans = []   #ルンルン数を格納していく(小さい方からでなくて大丈夫)

# 再帰関数
# 文字列として扱う
def dfs(n):
    global ans
    # Kの制約と入力例から答えの最大値は10桁なので，11桁以上になったら終了
    if len(n) >= 11:
        return
    
    ans.append(int(n))   # nをint型に変換してansに格納
    
    # もし，末尾が0と9でないならば，末尾aに対して a-1, a, a+1を付け足したものを再帰で呼び出す
    # n=13ならば，'13'に2, 3, 4をそれぞれ付け足した132, 133, 134を呼び出す
    if (n[-1]!=str(0)) and (n[-1]!=str(9)):
        dfs(n+str(int(n[-1])-1))
        dfs(n+str(n[-1]))
        dfs(n+str(int(n[-1])+1))
        
    # 末尾が0の場合は，末尾aに対して，a-1したものを付け足してしまうと，9をつけることになってしまうので，この処理は行わない
    elif n[-1]==str(0):
        dfs(n+str(n[-1]))
        dfs(n+str(int(n[-1])+1))
        
    # 末尾が9の場合は，+1したものを付け足してしまうと，'10'を付け加えることになってしまうので，行わない
    # 例: n=349の場合，+1も行ってしまうと34910となってしまい，条件を満たさない
    elif n[-1]==str(9):
        dfs(n+str(int(n[-1])-1))
        dfs(n+str(n[-1]))

# 初期値は，1~9の値で行う
for i in range(1, 10):
    dfs(str(i))
    
# 最後に，列挙したルンルン数をソートし，K番目（K-1)のものを出力    
ans2 = sorted(ans)
print(ans2[K-1])