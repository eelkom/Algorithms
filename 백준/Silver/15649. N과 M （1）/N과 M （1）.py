import sys

def dfs():
    if len(sequence) == M:
        print(*sequence)
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        sequence.append(i)
        dfs()
        sequence.pop()
        visited[i] = False

N, M = map(int, sys.stdin.readline().strip().split())
visited = [False] * (N+1)
sequence = []
dfs()