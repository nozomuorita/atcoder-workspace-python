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
s=list(input())
t=list(input())
s_ord=[]
t_ord=[]

# 文字コードの差分が等しいならYes
for i in range(len(s)):
    s_ord.append(ord(s[i]))
    t_ord.append(ord(t[i]))

dist=[]
for i in range(len(s)):
    tmp=(s_ord[i]-t_ord[i])%26
    dist.append(tmp)

if len(set(dist))==1:
    print('Yes')
else:
    print('No')