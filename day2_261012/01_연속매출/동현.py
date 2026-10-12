t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    sums=[]
    for i in range(n - m + 1):        # ← 구간 시작 위치
        s = 0
        for j in range(i,i+m):    # ← i부터 M개
            s += arr[j]
        sums.append(s)
    mx = sums[0]
    mn = sums[0]
    for x in sums:
        if x > mx:
            mx = x
        if x<mn:      # ← 최솟값 갱신 조건
            mn = x
    print(f'#{tc} {mx - mn}')