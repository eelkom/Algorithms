import sys

def dfs():
    if len(s) == M:
        print(*s)
        return
    for i in range(N):
        if visited[i] == True:
            continue
        visited[i] = True
        s.append(nums[i])
        dfs()
        s.pop()
        visited[i] = False

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
nums.sort()
s = []
visited = [False] * N
dfs()