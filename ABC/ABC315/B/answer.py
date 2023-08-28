# @nzm_ort
# https://github.com/nozomuorita/atcoder-workspace-python

# import module ------------------------------------------------------------------------------
from collections import defaultdict, deque, Counter
import math
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
import bisect
import sys
# sys.setrecursionlimit(100000000)
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y)

# main code ------------------------------------------------------------------------------------
m = int(input())
d = list(map(int, input().split()))

mid = (sum(d)+1)//2
tmp = 0
for i in range(len(d)):
    if tmp + d[i] >= mid:
        b = mid - tmp
        a = i+1
        break
    else:
        tmp += d[i]
        
print(a, b)