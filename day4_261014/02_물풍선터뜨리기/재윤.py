T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0

    for r in range(N):
        for c in range(M):
            power = grid[r][c]
            score = grid[r][c]

            for d in range(4):
                for k in range(1, power + 1):
                    nr = r + dr[d] * k
                    nc = c + dc[d] * k
                    if 0 <= nr < N and 0 <= nc < M:
                        score += grid[nr][nc]

            if score > max_score:
                max_score = score

    print(f'#{tc} {max_score}')