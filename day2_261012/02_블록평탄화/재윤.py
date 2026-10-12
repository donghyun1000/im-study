T = int(input())

for tc in range(1, T + 1):
    N, D = map(int, input().split())
    h = list(map(int, input().split()))

    for _ in range(D):
        max_idx = 0
        min_idx = 0
        for i in range(N):
            if h[i] > h[max_idx]:
                max_idx = i
            if h[i] < h[min_idx]:
                min_idx = i

        if h[max_idx] - h[min_idx] <= 1:
            break

        h[max_idx] -= 1
        h[min_idx] += 1

    max_h = h[0]
    min_h = h[0]
    for i in range(N):
        if h[i] > max_h:
            max_h = h[i]
        if h[i] < min_h:
            min_h = h[i]

    print(f'#{tc} {max_h - min_h}')