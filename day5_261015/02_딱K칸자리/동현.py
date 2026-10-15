t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    # 가로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1

    # 세로: 위 블록을 복사하고 arr[i][j] → arr[?][?] 만 바꾸기
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1
            
    print(f'#{tc} {ans}')