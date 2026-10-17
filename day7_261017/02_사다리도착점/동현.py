t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = -1

    for start in range(n):
        if arr[0][start] != 1:          # 출발점이 아니면 건너뛰기
            continue
        r, c = 0, start
        while r < n - 1:                 # 맨 아래 줄 전까지
            if c - 1 >= 0 and arr[r][c-1] == 1:        # 왼쪽 가로선
                while c - 1 >= 0 and arr[r][c-1] == 1:
                    c -= 1
            elif c + 1 < n and arr[r][c+1] == 1:       # 오른쪽 가로선
                while c + 1 < n and arr[r][c+1] == 1:
                    c += 1
            r += 1                       # 한 칸 아래로
        if arr[n-1][c] == 2:             # 도착점이면 정답
            ans = start
            break

    print(f'#{tc} {ans}')