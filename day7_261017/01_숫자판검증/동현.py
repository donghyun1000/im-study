t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    bad = 0

    # 행 검사
    for i in range(n):
        cnt = [0] * (n + 1)          # 줄마다 새 카운팅 배열
        for j in range(n):
            cnt[arr[i][j]] += 1      # 이 줄의 숫자 세기
        for v in range(1, n + 1):
            if cnt[v] != 1:          # 1~n 중 하나라도 1번이 아니면
                bad += 1             # 어긴 줄 +1
                break                # 이 줄은 한 번만 세고 끝

    # 열 검사: 행 검사에서 arr[i][j]의 i, j 역할만 바꿈
    for j in range(n):
        cnt = [0] * (n + 1)
        for i in range(n):
            cnt[arr[i][j]] += 1
        for v in range(1, n + 1):
            if cnt[v] != 1:
                bad += 1
                break

    print(f'#{tc} {bad}')