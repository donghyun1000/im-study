T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    mid = N // 2
    inside = 0
    outside = 0

    for i in range(N):
        for j in range(N):
            if abs(i - mid) + abs(j - mid) <= mid:
                inside += farm[i][j]
            else:
                outside += farm[i][j]

    print(f'#{tc} {inside - outside}')