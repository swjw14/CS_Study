# https://www.acmicpc.net/problem/14938
# 서강그라운드

import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, r = list(map(int, input().split()))
weights = list(map(int, input().split()))
weights.insert(0, 0)

dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(r):
    start, end, weight = list(map(int, input().split()))
    dist[start][end] = weight
    dist[end][start] = weight

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if dist[i][j] <= m:
            tmp += weights[j]
    ans = max(ans, tmp)

print(ans)