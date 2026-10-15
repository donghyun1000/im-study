T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 가로방향
    for i in range(N):
        cnt = 0

        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        # 한 행의 탐색이 끝나고 cnt == K 한번 더 확인
        if cnt == K:
            ans += 1
    # 세로방향
    for i in range(N):
        cnt = 0

        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        # 한 열의 탐색이 끝나고 cnt == K 한번 더 확인
        if cnt == K:
            ans += 1
            
    print(f"#{tc} {ans}")
