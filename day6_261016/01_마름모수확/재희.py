T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    m = N // 2
    harvest = 0
    outside = 0

    for i in range(N):
        # 중앙에서 얼마나 떨어져 있는지 계산
        d = abs(m - i)

        # 수확할 열의 시작과 끝
        start = d
        end = N - d

        for j in range(N):
            if start <= j < end:
                harvest += arr[i][j]
            else:
                outside += arr[i][j]

    ans = harvest - outside
    print(f"#{tc} {ans}")