import sys

def cnt_max(c):
    max_cnt = 1
    for i in range(N):
        row_cnt = 1
        col_cnt = 1
        for j in range(1, N):
            if c[i][j] == c[i][j-1]:
                row_cnt += 1
            else:
                row_cnt = 1

            if c[j][i] == c[j-1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            max_cnt = max(max_cnt, row_cnt, col_cnt)

    return max_cnt

N = int(sys.stdin.readline().strip())
c = [list(sys.stdin.readline().strip()) for _ in range(N)]
max_res = cnt_max(c)

for i in range(N):
    for j in range(N-1):
        if c[i][j] != c[i][j+1]:
            c[i][j], c[i][j+1] = c[i][j+1], c[i][j]
            max_res = max(max_res, cnt_max(c))
            c[i][j+1], c[i][j] = c[i][j], c[i][j+1]

        if c[j][i] != c[j+1][i]:
            c[j][i], c[j+1][i] = c[j+1][i], c[j][i]
            max_res = max(max_res, cnt_max(c))
            c[j+1][i], c[j][i] = c[j][i], c[j+1][i]

print(max_res)