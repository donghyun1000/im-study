T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 4번 회전하면 원래대로 돌아옴
    K = K % 4

    # K번 회전
    for _ in range(K):
        new_arr = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                new_arr[j][N-1-i] = arr[i][j]

        arr = new_arr

    # 출력
    print(f"#{tc}")
    for row in arr:
        print(*row)
