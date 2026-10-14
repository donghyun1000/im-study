T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # N행 M열 빈 배열 만들기
    arr = [[0] * M for _ in range(N)]

    # 오른쪽 → 아래 → 왼쪽 → 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 시작 위치와 방향
    i, j = 0, 0
    d = 0

    # 1부터 N*M까지 숫자 채우기
    for num in range(1, N*M+1):

        # 현재 위치에 숫자 저장
        arr[i][j] = num

        # 다음 위치 계산
        ni = i + di[d]
        nj = j + dj[d]

        # 범위를 벗어나거나 이미 채워진 칸이면 방향 전환
        if not (0 <= ni < N and 0 <= nj < M) or arr[ni][nj] != 0:
            d = (d + 1) % 4

            # 바뀐 방향으로 다음 위치 계산
            ni = i + di[d]
            nj = j + dj[d]

        # 다음 위치로 이동
        i, j = ni, nj

    # 출력
    print(f"#{tc}")
    for row in arr:
        print(*row)