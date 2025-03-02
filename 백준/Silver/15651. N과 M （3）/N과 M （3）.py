import sys

def dfs():
    if len(nums) == M:
        print(*nums)
        return
    for i in range(1, N+1):
        nums.append(i)
        dfs()
        nums.pop()

N, M = map(int, sys.stdin.readline().strip().split())
nums = []
dfs()