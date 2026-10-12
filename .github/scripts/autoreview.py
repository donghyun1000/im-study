"""
IM 스터디 자동 코드리뷰 스크립트 (GitHub Actions에서 실행)

python .github/scripts/autoreview.py pr <변경된 파일들...>   → PR 채점 결과 마크다운 출력
python .github/scripts/autoreview.py master                → 3명 모두 제출한 문제에 코드리뷰 이슈 생성
"""
import glob
import json
import os
import re
import subprocess
import sys

# 파일 이름(풀이 파일명) → GitHub 아이디
MEMBERS = {
    '동현': 'donghyun1000',
    '재윤': 'JaeYunAn',
    '재희': 'jaehee454-cloud',
}
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdOs4rhY8XAL8pQEo4J43eS3PHbIaqK7DlnXLDhU_8J85q7mQ/viewform'
REPO = os.environ.get('GITHUB_REPOSITORY', 'donghyun1000/im-study')
BRANCH = os.environ.get('DEFAULT_BRANCH', 'master')
DRY_RUN = os.environ.get('DRY_RUN') == '1'
EXTS = ('.py', '.java')


# ---------------------------------------------------------------- helpers
def problem_dirs():
    return sorted(d for d in glob.glob('day*_*/[0-9][0-9]_*') if os.path.isdir(d))


def problem_title(pdir):
    """'[Day1-1] 카페 주문 통계' 형태로 README 첫 줄에서 가져온다."""
    with open(os.path.join(pdir, 'README.md'), encoding='utf-8') as f:
        return f.readline().lstrip('# ').strip()


def solutions(pdir):
    """{멤버이름: 파일경로} — 멤버당 첫 번째 풀이 파일만."""
    found = {}
    for name in MEMBERS:
        for ext in EXTS:
            p = os.path.join(pdir, name + ext)
            if os.path.exists(p):
                found[name] = p
                break
    return found


def grade(path):
    """check.py 실행 → (통과수, 전체, 초, 상태문자열)"""
    try:
        p = subprocess.run([sys.executable, 'check.py', path], capture_output=True,
                           text=True, timeout=60, encoding='utf-8', errors='replace')
        out = p.stdout + p.stderr
    except subprocess.TimeoutExpired:
        return 0, 10, None, '⏰ 시간 초과'
    m = re.search(r'결과: (\d+)/(\d+) 통과\s+\(([\d.]+)초\)', out)
    if m:
        ok, total, sec = int(m.group(1)), int(m.group(2)), float(m.group(3))
        return ok, total, sec, '✅ Pass' if ok == total else '❌ Fail'
    if '컴파일 에러' in out:
        return 0, 10, None, '🛠️ 컴파일 에러'
    if '시간 초과' in out:
        return 0, 10, None, '⏰ 시간 초과'
    return 0, 10, None, '💥 런타임 에러'


def solve_time(path):
    """파일 상단 주석의 '풀이 시간: 45분' 을 읽는다."""
    try:
        with open(path, encoding='utf-8', errors='replace') as f:
            head = f.read(2000)
    except OSError:
        return '-'
    m = re.search(r'풀이\s*시간\s*[:：]\s*([^\n/]+)', head)
    return m.group(1).strip() if m and m.group(1).strip() else '-'


def loc(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return sum(1 for line in f if line.strip() and not line.strip().startswith(('#', '//', '*', '/*', '"""')))


def blob_url(path):
    return f'https://github.com/{REPO}/blob/{BRANCH}/' + path.replace(os.sep, '/')


def gh(*args, input_text=None):
    if DRY_RUN:
        print('[DRY_RUN] gh', ' '.join(args))
        return ''
    return subprocess.run(['gh', *args], input=input_text, capture_output=True,
                          text=True, check=True).stdout


# ---------------------------------------------------------------- PR mode
def pr_mode(files):
    targets = []
    for f in files:
        f = f.strip().strip('"')
        if not f.endswith(EXTS) or not os.path.exists(f):
            continue
        if not re.match(r'^day\d+_\d+/\d\d_[^/]+/[^/]+$', f):
            continue
        targets.append(f)

    lines = ['## 🤖 자동 채점 결과', '']
    if not targets:
        lines.append('채점할 풀이 파일이 없어요. 문제 폴더 안에 `이름.py` / `이름.java` 로 저장했는지 확인해 주세요.')
    else:
        lines += ['| 문제 | 파일 | 결과 | 통과 | 실행 시간 | 풀이 시간 |', '|---|---|---|---|---|---|']
        for f in targets:
            pdir = os.path.dirname(f)
            ok, total, sec, status = grade(f)
            sec_s = f'{sec:.2f}s' if sec is not None else '-'
            lines.append(f'| {problem_title(pdir)} | `{os.path.basename(f)}` | {status} | {ok}/{total} | {sec_s} | {solve_time(f)} |')
            name = os.path.splitext(os.path.basename(f))[0]
            if name not in MEMBERS:
                lines.append(f'| | ⚠️ `{name}` 은(는) 멤버 이름이 아니에요. `동현/재윤/재희` 로 저장해 주세요. | | | | |')

        lines += ['', '> 3명이 모두 제출하고 master에 merge되면 문제별 **코드리뷰 이슈**가 자동으로 열려요.']
    print('\n'.join(lines))


# ---------------------------------------------------------------- master mode
def existing_issue_titles():
    if DRY_RUN:
        return set()
    out = gh('issue', 'list', '--state', 'all', '--limit', '200', '--json', 'title')
    return {i['title'] for i in json.loads(out or '[]')}


def ensure_labels():
    for name, color in (('코드리뷰', '1f6feb'), ('완주', 'f2cc60')):
        try:
            gh('label', 'create', name, '--color', color, '--force')
        except subprocess.CalledProcessError:
            pass


def review_body(pdir, sols):
    title = problem_title(pdir)
    mentions = ' '.join('@' + MEMBERS[n] for n in MEMBERS)
    rows = []
    for name, path in sols.items():
        ok, total, sec, status = grade(path)
        sec_s = f'{sec:.2f}s' if sec is not None else '-'
        rows.append(f'| {name} | [{os.path.basename(path)}]({blob_url(path)}) | {status} | {ok}/{total} '
                    f'| {sec_s} | {solve_time(path)} | {loc(path)} |')

    pairs = list(MEMBERS)
    assign = '\n'.join(f'- [ ] **{pairs[i]}** → {pairs[(i + 1) % 3]} 코드 리뷰' for i in range(3))

    return f'''{mentions}

**{title}** 3명 모두 제출 완료! 🎉 서로의 풀이를 리뷰해 주세요.

📄 [문제 보기]({blob_url(os.path.join(pdir, 'README.md'))})

## 📊 채점 결과
| 이름 | 풀이 | 결과 | 통과 | 실행 시간 | 풀이 시간 | 코드 줄 수 |
|---|---|---|---|---|---|---|
{chr(10).join(rows)}

## 👀 리뷰 순서 (각자 1명 이상 코멘트)
{assign}

## ✍️ 리뷰 포인트
- 접근 방법이 어떻게 다른가? 더 간단한 방법은?
- 인덱스 범위 / 경계 체크 실수 가능성은 없는가?
- 변수 이름과 구조가 읽기 쉬운가?
- 시간이 가장 오래 걸린 사람은 어디서 막혔는가?

리뷰를 다 달았으면 위 체크박스를 체크하고, 3개 모두 체크되면 이 이슈를 Close 해 주세요.
'''


# 예전에 잘못 적었던 GitHub 아이디 → 올바른 아이디 (이미 열린 이슈 본문도 고쳐준다)
OLD_HANDLES = {'jaehee454': 'jaehee454-cloud'}


def fix_old_mentions():
    if DRY_RUN:
        return
    out = gh('issue', 'list', '--label', '코드리뷰', '--state', 'all', '--limit', '200',
             '--json', 'number,body')
    for it in json.loads(out or '[]'):
        body = it['body'] or ''
        new = body
        for old, cur in OLD_HANDLES.items():
            new = re.sub(r'@' + re.escape(old) + r'(?![\w-])', '@' + cur, new)
        if new != body:
            print(f'→ 이슈 #{it["number"]} 멘션 수정')
            gh('issue', 'edit', str(it['number']), '--body-file', '-', input_text=new)


def master_mode():
    titles = existing_issue_titles()
    ensure_labels()
    fix_old_mentions()
    dirs = problem_dirs()
    complete = 0
    for pdir in dirs:
        sols = solutions(pdir)
        if len(sols) < len(MEMBERS):
            continue
        complete += 1
        issue_title = '[코드리뷰] ' + problem_title(pdir).replace('[', '').replace(']', '')
        if issue_title in titles:
            continue
        body = review_body(pdir, sols)
        print(f'→ 이슈 생성: {issue_title}')
        if DRY_RUN:
            print(body)
        gh('issue', 'create', '--title', issue_title, '--label', '코드리뷰', '--body-file', '-', input_text=body)

    print(f'3명 모두 제출한 문제: {complete}/{len(dirs)}')
    done_title = '🎉 [완주] IM 스터디 14문제 3명 모두 완료'
    if dirs and complete == len(dirs) and done_title not in titles:
        mentions = ' '.join('@' + v for v in MEMBERS.values())
        body = f'''{mentions}

14문제 × 3명 = 42개 풀이 제출 완료! 수고했어요 👏

## ✅ 각자 할 일
- [ ] 동현 — [완주 인증 구글폼]({FORM_URL}) 제출
- [ ] 재윤 — [완주 인증 구글폼]({FORM_URL}) 제출
- [ ] 재희 — [완주 인증 구글폼]({FORM_URL}) 제출

인증 자료로 이 레포 링크(`https://github.com/{REPO}`)와 README 진행 현황표 캡처를 쓰면 돼요.
'''
        print('→ 완주 이슈 생성')
        gh('issue', 'create', '--title', done_title, '--label', '완주', '--body-file', '-', input_text=body)


AI_MARKER = '<!-- ai-review -->'


def ai_targets():
    """AI 리뷰가 아직 안 달린 열린 코드리뷰 이슈 → [{"issue": n, "dir": 문제폴더, "title": 제목}]"""
    by_title = {'[코드리뷰] ' + problem_title(d).replace('[', '').replace(']', ''): d for d in problem_dirs()}
    out = gh('issue', 'list', '--label', '코드리뷰', '--state', 'open', '--limit', '100',
             '--json', 'number,title')
    targets = []
    for it in json.loads(out or '[]'):
        pdir = by_title.get(it['title'])
        if not pdir or len(solutions(pdir)) < len(MEMBERS):
            continue
        comments = gh('issue', 'view', str(it['number']), '--json', 'comments', '--jq', '.comments[].body')
        if AI_MARKER in (comments or ''):
            continue
        targets.append({'issue': it['number'], 'dir': pdir, 'title': it['title']})
    print(json.dumps(targets, ensure_ascii=False))
    gh_out = os.environ.get('GITHUB_OUTPUT')
    if gh_out:
        with open(gh_out, 'a', encoding='utf-8') as f:
            f.write('targets=' + json.dumps(targets, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == 'pr':
        pr_mode(sys.argv[2:])
    elif len(sys.argv) >= 2 and sys.argv[1] == 'master':
        master_mode()
    elif len(sys.argv) >= 2 and sys.argv[1] == 'ai-targets':
        ai_targets()
    else:
        print(__doc__)
