t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sums = []
    for i in range(n):
        s = 0
        for j in range(n):
            s += arr[i][j]
        sums.append(s)
    for j in range(n):
        s = 0
        for i in range(n):
            s += arr[i][j]
        sums.append(s)
    d1 = 0
    d2 = 0
    for i in range(n):
        d1 += arr[i][i]     # 주대각선
        d2 += arr[i][n-1-i]     # 반대각선
    sums.append(d1)
    sums.append(d2)
    mx = sums[0]
    mn = sums[0]
    for x in sums:
        if x > mx:
            mx = x
        if x < mn:
            mn = x
    print(f'#{tc} {mx - mn}')