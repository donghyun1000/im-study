di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(M):
            num = arr[i][j]  # 현재 풍선의 세기
            balloon = num   # 자기 자신부터 더하기

            # 상하좌우 4방향 탐색
            for d in range(4):

                # 풍선의 세기만큼 거리 탐색
                for k in range(1, num+1):
                    ni = i + di[d] * k
                    nj = j + dj[d] * k

                    # 격자 범위 안이면 더하기
                    if 0 <= ni < N and 0 <= nj < M:
                        balloon += arr[ni][nj]

            # 최대 점수 갱신
            ans = max(ans, balloon)

    print(f"#{tc} {ans}")