# https://www.acmicpc.net/problem/11265
# 끝나지 않은 파티

import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

for _ in range(M):
    start, end, weight = list(map(int, input().split()))
    if lst[start - 1][end - 1] <= weight:
        print("Enjoy other party")
    else:
        print("Stay here")
