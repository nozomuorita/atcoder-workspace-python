n = int(input())
a = list(map(int, input().split()))

dp = [1<<60] * n
dp[0] = 0
for i in range(1, n):
    if i-1>=0:
        dp[i] = min(dp[i], dp[i-1]+abs(a[i]-a[i-1]))
    if i-2>=0:
        dp[i] = min(dp[i], dp[i-2]+abs(a[i]-a[i-2]))

print(dp[-1])