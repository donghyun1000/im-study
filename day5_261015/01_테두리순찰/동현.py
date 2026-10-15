t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    best = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            s = 0
            for a in range(i, i + m):
                for b in range(j, j + m):
                    if a == i or a == i + m - 1 or b == j or b == j + m - 1:
                        s += arr[a][b]
            if s > best:
                best = s
    print(f'#{tc} {best}')