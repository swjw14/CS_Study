# https://www.acmicpc.net/problem/16236
# 아기 상어

import sys
from collections import deque

input = sys.stdin.readline
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N = int(input())
mp = []
cur_shark_weight = 2
cur_shark_row = -1
cur_shark_col = -1

for i in range(N):
    line = list(map(int, input().split()))
    if 9 in line:
        cur_shark_row = i
        cur_shark_col = line.index(9)
    mp.append(line)

ans = 0
shark_size_tmp = 0
mp[cur_shark_row][cur_shark_col] = 0
while True:
    queue = deque([(cur_shark_row, cur_shark_col, 0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[cur_shark_row][cur_shark_col] = True

    threshold = sys.maxsize
    min_row = sys.maxsize
    min_col = sys.maxsize

    while queue:
        cur_row, cur_col, dist = queue.popleft()
        for dx, dy in dxdy:
            new_row = cur_row + dx
            new_col = cur_col + dy
            new_dist = dist + 1
            if 0 <= new_row < N and 0 <= new_col < N and not visited[new_row][new_col] and new_dist <= threshold:
                if mp[new_row][new_col] == 0:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, new_dist))

                elif mp[new_row][new_col] < cur_shark_weight:
                    threshold = new_dist
                    visited[new_row][new_col] = True

                    if new_row < min_row:
                        min_row = new_row
                        min_col = new_col
                    elif new_row == min_row and new_col < min_col:
                        min_row = new_row
                        min_col = new_col

                elif mp[new_row][new_col] == cur_shark_weight:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, new_dist))

    if threshold == sys.maxsize:
        print(ans)
        break
    else:
        shark_size_tmp += 1
        if shark_size_tmp == cur_shark_weight:
            cur_shark_weight += 1
            shark_size_tmp = 0

        ans += threshold
        cur_shark_row = min_row
        cur_shark_col = min_col

        mp[min_row][min_col] = 0
