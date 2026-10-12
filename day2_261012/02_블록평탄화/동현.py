t = int(input())
for tc in range(1, t+1):
    n, dump = map(int, input().split())
    box = list(map(int, input().split()))
    for i in range(dump):
        box.sort()
        if box[-1] - box[0] <= 1:
            break
        box[-1] -= 1
        box[0] += 1
    box.sort()
    print(f'#{tc} {box[-1] - box[0]}')