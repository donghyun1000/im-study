T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    K = K % 4

    for _ in range(K):
        new_board = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_board[i][j] = board[N - 1 - j][i]
        board = new_board

    print(f'#{tc}')
    for i in range(N):
        print(*board[i])