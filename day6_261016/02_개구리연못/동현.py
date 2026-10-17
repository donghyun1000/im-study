t = int(input())
for tc in range(1, t+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    q = int(input())
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    for _ in range(q):
        d, k = map(int, input().split())
        nr = r + dr[d] * k
        nc = c + dc[d] * k
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
            grid[r][c] = 0                  # ← 떠난 칸 가라앉음
            r, c = nr, nc

    leaf = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                leaf += 1
    print(f'#{tc} {r+1} {c+1} {leaf}')