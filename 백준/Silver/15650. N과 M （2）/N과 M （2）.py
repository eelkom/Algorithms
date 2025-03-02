import sys

def dfs(i):
    if len(nums) == M:
        print(*nums)
        return
    for i in range(i, N+1):
        if visited[i] == True:
            continue
        visited[i] = True
        nums.append(i)
        dfs(i+1)
        nums.pop()
        visited[i] = False

N, M = map(int, sys.stdin.readline().strip().split())
nums = []
visited = [False] * (N+1)
dfs(1)