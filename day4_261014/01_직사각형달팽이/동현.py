t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c, d = 0, 0, 0                  # 시작: (0,0), 오른쪽

    for v in range(1, n*m + 1):
        grid[r][c] = v
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] != 0:     # ← 밖이거나 이미 채운 칸이면
            d = (d + 1) % 4
            nr = r + dr[d]
            nc = c + dc[d]
        r, c = nr, nc

    print(f'#{tc}')
    for row in grid:
        print(*row)