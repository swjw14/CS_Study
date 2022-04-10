# https://www.acmicpc.net/problem/2252
# 줄 세우기

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = list(map(int, input().split()))
line = defaultdict(set)
is_degree = defaultdict(int)

for _ in range(M):
    start, end = list(map(int, input().split()))
    line[start].add(end)
    is_degree[end] += 1

queue = []
for i in range(1, N + 1):
    if is_degree[i] == 0:
        queue.append(i)
queue = deque(queue)

ans = []

while queue:
    student = queue.popleft()
    ans.append(student)

    for related_point in line[student]:
        is_degree[related_point] -= 1
        if is_degree[related_point] == 0:
            queue.append(related_point)

for i in ans:
    print(i, end=' ')
