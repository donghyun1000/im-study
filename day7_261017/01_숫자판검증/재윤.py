T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    # 행 검사
    for i in range(N):
        count = [0] * (N + 1)
        for j in range(N):
            count[board[i][j]] += 1

        ok = True
        for num in range(1, N + 1):
            if count[num] != 1:
                ok = False
        if not ok:
            answer += 1

    # 열 검사
    for j in range(N):
        count = [0] * (N + 1)
        for i in range(N):
            count[board[i][j]] += 1

        ok = True
        for num in range(1, N + 1):
            if count[num] != 1:
                ok = False
        if not ok:
            answer += 1

    print(f'#{tc} {answer}')