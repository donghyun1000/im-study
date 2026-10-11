t = int(input())
for tc in range(1,t+1):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    answer = 0
    for i in range(n):
        mx = 0
        for j in range(i-k,i+k+1):   # ← i-k 부터 i+k 까지
            if 0<=j<n and j!=i:      # ← 범위 안이고, 자기 자신(i)이 아닐 때만
                if arr[j] > mx:
                    mx = arr[j]
        if arr[i] > mx:
            answer += arr[i] - mx

    print(f'#{tc} {answer}')