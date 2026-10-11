"""
풀이 채점기

사용법 (레포 최상위 폴더에서):
    python check.py day1_261012/01_카페주문통계/동현.py
    python check.py day1_261012/01_카페주문통계/동현.java

- 같은 폴더의 input.txt를 표준입력으로 넣고, output.txt와 비교한다.
- 풀이 안에서 sys.stdin = open('input.txt') 를 써도 그대로 동작한다.
- Java는 `public class Solution` 으로 작성해야 한다. (SWEA와 동일)
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

TIME_LIMIT = 10  # 초 (전체 테스트 케이스 기준)


def split_cases(text):
    """'#1 ...' 으로 시작하는 줄 기준으로 케이스별 블록을 나눈다."""
    cases, cur = {}, None
    for line in text.replace('\r', '').split('\n'):
        line = line.rstrip()
        m = re.match(r'^#(\d+)(?:\s+(.*))?$', line)
        if m:
            cur = int(m.group(1))
            cases[cur] = [m.group(2).strip()] if m.group(2) else []
        elif cur is not None and line.strip():
            cases[cur].append(' '.join(line.split()))
    return cases


def run(sol, folder, inp):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    if sol.endswith('.py'):
        cmd, tmp = [sys.executable, os.path.abspath(sol)], None
    elif sol.endswith('.java'):
        tmp = tempfile.mkdtemp()
        shutil.copy(sol, os.path.join(tmp, 'Solution.java'))
        c = subprocess.run(['javac', '-encoding', 'UTF-8', 'Solution.java'],
                           cwd=tmp, capture_output=True, text=True)
        if c.returncode != 0:
            print('❌ 컴파일 에러\n' + c.stderr)
            sys.exit(1)
        cmd = ['java', '-cp', tmp, 'Solution']
    else:
        print('.py 또는 .java 파일만 채점할 수 있어요.')
        sys.exit(1)
    start = time.time()
    try:
        p = subprocess.run(cmd, input=inp.encode('utf-8'), cwd=folder,
                           capture_output=True, timeout=TIME_LIMIT, env=env)
    except subprocess.TimeoutExpired:
        print(f'⏰ 시간 초과 ({TIME_LIMIT}초)')
        sys.exit(1)
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
    elapsed = time.time() - start
    if p.returncode != 0:
        print('❌ 런타임 에러\n' + p.stderr.decode('utf-8', 'replace'))
        sys.exit(1)
    return p.stdout.decode('utf-8', 'replace'), elapsed


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    sol = sys.argv[1]
    folder = os.path.dirname(os.path.abspath(sol))
    with open(os.path.join(folder, 'input.txt'), encoding='utf-8') as f:
        inp = f.read()
    with open(os.path.join(folder, 'output.txt'), encoding='utf-8') as f:
        expected = split_cases(f.read())

    out, elapsed = run(sol, folder, inp)
    got = split_cases(out)

    ok = 0
    for t in sorted(expected):
        if got.get(t) == expected[t]:
            ok += 1
            print(f'  #{t} ✅')
        else:
            print(f'  #{t} ❌  기대: {" / ".join(expected[t])}')
            print(f'       출력: {" / ".join(got.get(t, ["(없음)"]))}')
    total = len(expected)
    print(f'\n결과: {ok}/{total} 통과  ({elapsed:.2f}초)')
    print('🎉 Pass!' if ok == total else '💪 다시 도전!')


if __name__ == '__main__':
    main()
