T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    orders = list(map(int, input().split()))

    count = [0] * 101

    for menu in orders:
        count[menu] += 1

    best_menu = 1
    best_count = count[1]

    for menu in range(2, 101):
        if count[menu] > best_count:
            best_menu = menu
            best_count = count[menu]

    print(f'#{tc} {best_menu} {best_count}')