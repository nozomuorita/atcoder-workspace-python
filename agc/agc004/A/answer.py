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
a, b, c = map(int, input().split())

s = a * b * c
ans = []

# pattern a
a2 = a//2
s_a = a2 * b * c
s_o = s - s_a
ans.append(abs(s_o - s_a))

# pattern b
b2 = b//2
s_b = a * b2 * c
s_o = s - s_b
ans.append(abs(s_o - s_b))

# pattern c
c2 = c//2
s_c = a * b * c2
s_o = s - s_c
ans.append(abs(s_o - s_c))

print(min(ans))