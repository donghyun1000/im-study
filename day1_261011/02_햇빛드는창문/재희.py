T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    B = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        max_height = 0

        for j in range(1, K+1):
            # 왼쪽 건물
            if i-j >= 0:
                if B[i-j] > max_height:
                    max_height = B[i-j]

            # 오른쪽 건물
            if i+j < N:
                if B[i+j] > max_height:
                    max_height = B[i+j]

    
        if B[i] > max_height:
            ans += B[i] - max_height

    print(f"#{tc} {ans}")