from math import gcd
a, b, c = map(int, input().split())
g = gcd(gcd(a, b), c)

ans = ((a//g)-1) + ((b//g)-1) + ((c//g)-1)
print(ans)