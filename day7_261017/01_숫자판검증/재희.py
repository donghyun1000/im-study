T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        cnt_row = [0] * (N+1)
        cnt_col = [0] * (N+1)
        for j in range(N):
            cnt_row[arr[i][j]] += 1
            cnt_col[arr[j][i]] += 1

        for l in range(1, N+1):
            if cnt_row[l] != 1:
                ans += 1
                break
        for l in range(1, N+1):
            if cnt_col[l] != 1:
                ans += 1
                break

    print(f"#{tc} {ans}")


