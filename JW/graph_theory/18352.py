# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기

import sys
from collections import deque, defaultdict
input = sys.stdin.readline
INF = sys.maxsize

N, M, K, X = list(map(int, input().split()))
connection = defaultdict(set)
for _ in range(M):
    start, end = list(map(int, input().split()))
    connection[start].add(end)

dist = [INF for _ in range(N + 1)]
queue = deque([(X, 0)])
dist[X] = 0

while queue:
    cur_point, cur_dist = queue.popleft()
    for connected_point in connection[cur_point]:
        new_dist = cur_dist + 1
        if dist[connected_point] > new_dist:
            queue.append((connected_point, new_dist))
            dist[connected_point] = new_dist

ans = []
for i in range(1, N + 1):
    if dist[i] == K:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)