T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    grid = [[0] * M for _ in range(N)]

    r = 0
    c = 0
    d = 0

    for num in range(1, N * M + 1):
        grid[r][c] = num

        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >= N or nc < 0 or nc >= M or grid[nr][nc] != 0:
            d = (d + 1) % 4
            nr = r + dr[d]
            nc = c + dc[d]

        r = nr
        c = nc

    print(f'#{tc}')
    for i in range(N):
        print(*grid[i])