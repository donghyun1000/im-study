T = int(input())

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    pond = [list(map(int, input().split())) for _ in range(N)]

    r, c = map(int, input().split())
    r -= 1
    c -= 1

    Q = int(input())
    for _ in range(Q):
        d, k = map(int, input().split())

        nr = r + dr[d] * k
        nc = c + dc[d] * k

        if 0 <= nr < N and 0 <= nc < N and pond[nr][nc] == 1:
            pond[r][c] = 0
            r = nr
            c = nc

    leaves = 0
    for i in range(N):
        for j in range(N):
            if pond[i][j] == 1:
                leaves += 1

    print(f'#{tc} {r + 1} {c + 1} {leaves}')