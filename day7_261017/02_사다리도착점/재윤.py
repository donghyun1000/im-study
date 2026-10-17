T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]

    answer = -1

    for start in range(N):
        if ladder[0][start] != 1:
            continue

        c = start

        for r in range(1, N - 1):
            if c - 1 >= 0 and ladder[r][c - 1] == 1:
                while c - 1 >= 0 and ladder[r][c - 1] == 1:
                    c -= 1
            elif c + 1 < N and ladder[r][c + 1] == 1:
                while c + 1 < N and ladder[r][c + 1] == 1:
                    c += 1

        if ladder[N - 1][c] == 2:
            answer = start

    print(f'#{tc} {answer}')