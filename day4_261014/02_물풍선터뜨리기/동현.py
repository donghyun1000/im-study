t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dr = [-1, 1, 0, 0]       # 상 하 좌 우
    dc = [0, 0, -1, 1]

    best = 0
    for i in range(n):
        for j in range(m):
            power = arr[i][j]
            s = power               # ← 자기 자신부터 더해 두기
            for d in range(4):
                for k in range(1,power+1):        # ← 1칸 ~ power칸
                    nr = i + dr[d] * k
                    nc = j + dc[d] * k
                    if 0 <= nr < n and 0 <= nc < m:  # ← 범위 안이면
                        s += arr[nr][nc]
            if s > best:
                best = s
    print(f'#{tc} {best}')