# https://www.acmicpc.net/problem/1719
# 택배

import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = list(map(int, input().split()))
dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
ans = [[i for i in range(n + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    start, end, weight = list(map(int, input().split()))
    dist[start][end] = weight
    dist[end][start] = weight


def traceback(start, num):
    if ans[start][num] == num:
        return num
    else:
        return traceback(start, ans[start][num])


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            new_dist = dist[i][k] + dist[k][j]
            if new_dist < dist[i][j]:
                dist[i][j] = new_dist
                ans[i][j] = traceback(i, k)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("-", end=" ")
        else:
            print(ans[i][j], end=' ')
    print()
