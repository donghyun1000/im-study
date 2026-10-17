t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    mid = n // 2
    inside = 0
    outside = 0
    for i in range(n):
        d = abs(i - mid)
        for j in range(n):
            if d <= j <= n - 1 - d:    # ← 수확 범위
                inside += arr[i][j]
            else:
                outside += arr[i][j]
    print(f'#{tc} {inside - outside}')