T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):

            total = 0
            for ni in range(M):
                for nj in range(M):
                    if ni == 0 or nj == 0 or ni == M-1 or nj == M-1:
                        total += arr[i+ni][j+nj]
            ans = max(ans, total)
    print((f"#{tc} {ans}"))

