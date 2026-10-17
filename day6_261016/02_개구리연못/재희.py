di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 개구리 시작 위치 (인덱스를 0부터 시작하도록 변경)
    r, c = map(int, input().split())
    r -= 1
    c -= 1

    Q = int(input())

    # 현재 연잎 개수
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1

    # Q개의 명령 수행
    for _ in range(Q):
        d, k = map(int, input().split())

        # 점프할 위치 계산
        ni = r + di[d] * k
        nj = c + dj[d] * k

        # 연못 안에 있고, 도착 칸이 연잎이라면
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:

            # 기존 연잎은 물로 변경
            arr[r][c] = 0
            cnt -= 1

            # 개구리 위치 변경
            r, c = ni, nj

    # 출력할 때 다시 1부터 시작하는 좌표로 변경
    print(f"#{tc} {r+1} {c+1} {cnt}")