t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    k = k % 4
    for _ in range(k):
        new = [[0] * n for _ in range(n)]   # 새 판 (빈 판)
        for i in range(n):
            for j in range(n):
                new[j][n-1-i] = arr[i][j]     # ← 찾은 규칙
        arr = new                           # 돌린 판으로 교체
    print(f'#{tc}')
    for row in arr:
        print(*row)   