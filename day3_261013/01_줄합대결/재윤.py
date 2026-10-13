T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    sums = []

    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum += board[i][j]
        sums.append(row_sum)

    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum += board[i][j]
        sums.append(col_sum)

    diag1 = 0
    diag2 = 0
    for i in range(N):
        diag1 += board[i][i]
        diag2 += board[i][N - 1 - i]
    sums.append(diag1)
    sums.append(diag2)

    max_s = sums[0]
    min_s = sums[0]
    for s in sums:
        if s > max_s:
            max_s = s
        if s < min_s:
            min_s = s

    print(f'#{tc} {max_s - min_s}')