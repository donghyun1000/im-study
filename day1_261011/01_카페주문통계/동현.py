"""
   [Day1-1] 카페 주문 통계
   - 채점 결과: 10/10 ✅
   - 접근: 카운팅 배열로 빈도 세고, > 비교로 동률 시 작은 번호 유지
   """


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    m = list(map(int, input().split()))
    cnt = [0]*101
    for i in m:
        cnt[i] += 1
    best_num = 0
    best_cnt = 0
    for num in range(1, 101):
        if cnt[num] > best_cnt:
            best_num = num
            best_cnt = cnt[num]
    print(f'#{tc} {best_num} {best_cnt}')