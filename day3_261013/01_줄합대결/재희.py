T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    arr_3 = 0   # 우하향대각선합
    arr_4 = 0   # 우상향대각선합
    ans_max = 0
    ans_min = float('inf')
    ans = 0

    # 가로합
    for i in range(N):
        arr_1 = 0  # 가로합
        arr_2 = 0  # 세로합
        for j in range(N):
            arr_1 += arr[i][j]
            arr_2 += arr[j][i]

        ans_max = max(ans_max, arr_1, arr_2)
        ans_min = min(ans_min, arr_1, arr_2)

        # 대각선의 합
        arr_3 += arr[i][i]
        arr_4 += arr[i][N-1-i]

    ans_max = max(ans_max, arr_3, arr_4)
    ans_min = min(ans_min, arr_3, arr_4)

    ans = ans_max - ans_min
    print(f"#{tc} {ans}")

