T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    sales = list(map(int, input().split()))

    max_sum = 0
    min_sum = 10000 * 1000

    for i in range(N - M + 1):
        total = 0
        for j in range(i, i + M):
            total += sales[j]

        if total > max_sum:
            max_sum = total
        if total < min_sum:
            min_sum = total

    print(f'#{tc} {max_sum - min_sum}')