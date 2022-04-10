# https://www.acmicpc.net/problem/2224
# 명제 증명

import sys
INF = sys.maxsize


def alp_to_num(alp):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".index(alp)


N = int(input())
dist = [[INF for _ in range(52)] for _ in range(52)]

for i in range(52):
    dist[i][i] = 0

for _ in range(N):
    line = input().split(" => ")
    dist[alp_to_num(line[0])][alp_to_num(line[1])] = 1

for k in range(52):
    for i in range(52):
        for j in range(52):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = []
for i in range(52):
    for j in range(52):
        if i != j and dist[i][j] != sys.maxsize:
            start_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[i]
            end_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"[j]
            ans.append("{} => {}".format(start_str, end_str))

print(len(ans))
for i in ans:
    print(i)