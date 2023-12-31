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
def ceil_div(x, y): return -(-x//y) # 切り上げ

# main code ------------------------------------------------------------------------------------
n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

dist = []
for i in range(m-1):
    dist.append(abs(x[i]-x[i+1]))
dist.sort(reverse=True)
dist = sum(dist[:n-1])

dist_x = x[-1] - x[0]

print(dist_x - dist)
