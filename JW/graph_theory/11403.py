# https://www.acmicpc.net/problem/11403
# 경로 찾기

import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
dist = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 0:
            line[j] = INF
    dist.append(line)

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(N):
    for j in range(N):
        if dist[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
