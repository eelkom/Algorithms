import sys

def dfs():
    if len(s) == M:
        print(*s)
        return
    for i in range(0, N):
        s.append(nums[i])
        dfs()
        s.pop()

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
nums.sort()
s = []
dfs()