# https://www.acmicpc.net/problem/10159
# 저울

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    dist[i][i] = 0

for _ in range(M):
    start, end = list(map(int, input().split()))
    dist[start][end] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dist[i][j] = min(dist[i][j], dist[j][i])
        dist[j][i] = min(dist[i][j], dist[j][i])

for i in range(1, N + 1):
    print(dist[i].count(sys.maxsize) - 1)