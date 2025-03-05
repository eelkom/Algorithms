import sys

def is_valid(x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
            return False
    return True

def dfs(tot, cnt, start_x, start_y):
    global max_sum

    if cnt == K:
        max_sum = max(max_sum, tot)
        return

    for i in range(start_x, N):
        for j in range(start_y if i == start_x else 0, M):
            if not visited[i][j] and is_valid(i, j):
                visited[i][j] = True
                dfs(tot + a[i][j], cnt + 1, i, j)  # i, j 이후만 탐색
                visited[i][j] = False

N, M, K = map(int, sys.stdin.readline().strip().split())
a = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_sum = -float('inf')

dfs(0, 0, 0, 0)
print(max_sum)
