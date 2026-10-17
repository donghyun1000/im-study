T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 도착점 2의 위치 찾기
    r = N - 1

    for j in range(N):
        if arr[r][j] == 2:
            c = j
            break

    # 도착점에서 위로 이동
    while r > 0:

        # 왼쪽에 길이 있다면 왼쪽으로 이동
        if c > 0 and arr[r][c-1] == 1:
            while c > 0 and arr[r][c-1] == 1:
                c -= 1

        # 오른쪽에 길이 있다면 오른쪽으로 이동
        elif c < N-1 and arr[r][c+1] == 1:
            while c < N-1 and arr[r][c+1] == 1:
                c += 1

        # 위로 한 칸 이동
        r -= 1

    print(f"#{tc} {c}")