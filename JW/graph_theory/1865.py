# https://www.acmicpc.net/problem/1865
# 웜홀

import sys
from collections import defaultdict

input = sys.stdin.readline
INF = sys.maxsize

T = int(input())
for _ in range(T):
    N, M, W = list(map(int, input().split()))
    edges = []

    l = defaultdict(int)

    for _ in range(M):
        line = list(map(int, input().split()))
        if l[line[0], line[1]] == 0:
            l[line[0], line[1]] = line[2]
        else:
            l[line[0], line[1]] = min(l[line[0], line[1]], line[2])

        if l[line[1], line[0]] == 0:
            l[line[1], line[0]] = line[2]
        else:
            l[line[1], line[0]] = min(l[line[1], line[0]], line[2])

    for _ in range(W):
        line = list(map(int, input().split()))
        l[line[0], line[1]] = -line[2]

    dist = [INF for _ in range(N + 1)]
    dist[1] = 0
    for _ in range(N - 1):
        for (point1, point2) in l.keys():
            if dist[point1] + l[point1, point2] < dist[point2]:
                dist[point2] = dist[point1] + l[point1, point2]

    cycle = False
    for (point1, point2) in l.keys():
        if dist[point1] + l[point1, point2] < dist[point2]:
            cycle = True
            break

    if cycle:
        print("YES")
    else:
        print("NO")
