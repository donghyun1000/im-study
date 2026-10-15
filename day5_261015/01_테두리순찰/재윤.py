T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            total = 0

            for i in range(M):
                for j in range(M):
                    if i == 0 or i == M - 1 or j == 0 or j == M - 1:
                        total += grid[r + i][c + j]

            if total > max_sum:
                max_sum = total

    print(f'#{tc} {max_sum}')