# 📮 풀이 제출 가이드

> 처음 한 번만 **0단계**, 그다음부터는 매일 **1~5단계**만 반복하면 돼요.

| 이름 | 파일 이름 | 브랜치 이름 |
|---|---|---|
| 동현 | `동현.py` / `동현.java` | `donghyun` |
| 재윤 | `재윤.py` / `재윤.java` | `jaeyun` |
| 재희 | `재희.py` / `재희.java` | `jaehee` |

> ⚠️ **파일 이름이 위와 다르면 제출로 인정되지 않아요.** (자동 채점·코드리뷰 이슈가 이름으로 사람을 구분해요)

---

## 0️⃣ 처음 한 번만

1. 메일이나 GitHub 알림으로 온 **초대(Invitation)를 Accept** 하기
2. 레포를 내려받고 내 브랜치 만들기

```bash
git clone https://github.com/donghyun1000/im-study.git
cd im-study
git checkout -b jaeyun          # ← 본인 브랜치 이름
git push -u origin jaeyun
```

처음 commit할 때 `Please tell me who you are`가 나오면:
```bash
git config --global user.name "GitHub아이디"
git config --global user.email "GitHub가입이메일"
```

---

## 1️⃣ 매일 시작할 때: 최신 상태 받기

```bash
git checkout master
git pull origin master
git checkout jaeyun
git merge master
```

> 이걸 안 하면 다른 사람이 올린 내용과 꼬일 수 있어요. **매일 꼭!**

## 2️⃣ 문제 풀기

1. 오늘 문제 폴더의 `README.md`를 읽는다 → 목록은 [`ROADMAP.md`](./ROADMAP.md)
2. **타이머 2시간** 켜고 시작
3. 같은 폴더에 내 이름으로 저장하고, 맨 위에 [`TEMPLATE.md`](./TEMPLATE.md) 주석을 붙인다

```
day1_261011/
└── 01_카페주문통계/
    ├── README.md   ← 문제
    ├── input.txt
    ├── output.txt
    └── 재윤.py      ← 여기에 저장!
```

> 🙈 **다른 사람 풀이 파일은 내가 다 풀기 전까지 열어보지 않기!**

## 3️⃣ 채점하기

레포 최상위 폴더(`im-study`)에서:
```bash
python check.py day1_261011/01_카페주문통계/재윤.py
```
`10/10 통과 🎉 Pass!` 가 나오면 성공. 2시간 안에 못 풀었으면 그 상태 그대로 제출해요.

## 4️⃣ 올리기 (push)

```bash
git add .
git commit -m "[Day1] 재윤 - 카페 주문 통계, 햇빛 드는 창문"
git push
```

> ⚠️ `README.md`, `input.txt`, `output.txt` 같은 **공용 파일은 수정하지 않기.** 내 풀이 파일만 올려요.

## 5️⃣ PR 만들기 → 리뷰 → merge

1. GitHub 레포에 들어가면 뜨는 **`Compare & pull request`** 버튼 클릭
   (안 보이면 **Pull requests → New pull request → base: `master` ← compare: `jaeyun`**)
2. PR 템플릿 채우고 **Create pull request**
3. 🤖 1~2분 뒤 **자동 채점 결과**가 PR 코멘트로 달려요
4. 다른 팀원 1명이 **Files changed → Review changes → Approve**
5. Approve 받으면 본인이 **Merge pull request** 클릭
6. merge 후 **Delete branch 버튼은 누르지 않기** (다음 날도 같은 브랜치 써요)

> ⏰ 마감: 매일 23:59까지 PR 올리기

---

## 🤖 자동으로 일어나는 일

- **PR을 올리면** → 내 풀이 자동 채점 결과가 코멘트로 달림
- **풀이 PR이 master에 merge되면** → README 진행 현황에 ✅가 자동 표시되고, 합계도 자동 갱신
- **3명 풀이가 모두 master에 merge되면** → `[코드리뷰] Day1-1 ...` 이슈가 자동 생성
  - 이슈에 적힌 순서대로 리뷰 (동현 → 재윤 → 재희 → 동현)
  - 이슈 표의 풀이 링크를 열어 읽고, 이슈 댓글에 `재희.py 12번째 줄: 경계 체크를 이렇게 하면 더 짧아요` 식으로 남기면 돼요
  - 리뷰 끝나면 이슈의 체크박스 체크, 3개 다 체크되면 Close
- **14문제 × 3명 모두 끝나면** → 🎉 완주 이슈 + 구글폼 링크가 열림 → 각자 폼 제출

---

## 🆘 자주 막히는 상황

| 상황 | 해결 |
|---|---|
| `push` 할 때 `rejected` | `git pull origin jaeyun` 후 다시 `git push` |
| `merge master` 하다가 `CONFLICT` | 대부분 공용 파일을 건드린 경우. 단톡방에 캡처 공유하기 |
| PR에 다른 사람 파일까지 들어감 | 1단계(`merge master`)를 안 한 경우. 단톡방에 공유 |
| 자동 채점이 `런타임 에러` | `check.py`로 로컬에서 먼저 돌려보기. 입력 받는 방식 확인 |
| Java 채점이 안 됨 | 클래스 이름을 `public class Solution` 으로 |
