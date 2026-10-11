T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    total = 0

    for i in range(N):
        max_h = 0

        for j in range(i - K, i + K + 1):
            if j == i:
                continue
            if j < 0 or j >= N:
                continue
            if h[j] > max_h:
                max_h = h[j]

        if h[i] - max_h > 0:
            total += h[i] - max_h

    print(f'#{tc} {total}')