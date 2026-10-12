"""Update the README progress table from merged solution files."""
import re
from pathlib import Path


README = Path('README.md')
MEMBERS = ('동현', '재윤', '재희')
SOLUTION_EXTENSIONS = ('.py', '.java')
PROBLEM_TITLE = re.compile(r'^#\s*\[Day(\d+)-\d+\]\s*(.+?)\s*$')


def problems():
    found = []
    for directory in sorted(Path('.').glob('day[0-9]*_*/[0-9][0-9]_*')):
        readme = directory / 'README.md'
        if not readme.is_file():
            raise FileNotFoundError(f'문제 README를 찾을 수 없어요: {readme}')

        first_line = readme.read_text(encoding='utf-8').splitlines()[0]
        match = PROBLEM_TITLE.match(first_line)
        if not match:
            raise ValueError(f'문제 제목 형식이 올바르지 않아요: {readme}')

        submitted = {
            member: any((directory / f'{member}{extension}').is_file()
                        for extension in SOLUTION_EXTENSIONS)
            for member in MEMBERS
        }
        found.append((int(match.group(1)), match.group(2), submitted))
    return found


def progress_table():
    items = problems()
    rows = [
        '| Day | 문제 | 동현 | 재윤 | 재희 |',
        '|---|---|---|---|---|',
    ]
    totals = {member: 0 for member in MEMBERS}
    for day, title, submitted in items:
        cells = []
        for member in MEMBERS:
            marked = submitted[member]
            totals[member] += marked
            cells.append('✅' if marked else '')
        rows.append(f'| {day} | {title} | ' + ' | '.join(cells) + ' |')

    rows.append(
        '| | **합계** | ' +
        ' | '.join(f'{totals[member]}/{len(items)}' for member in MEMBERS) +
        ' |'
    )
    return '\n'.join(rows)


def update_readme():
    text = README.read_text(encoding='utf-8')
    section = '## 📊 진행 현황 (✅ 풀이 제출 후 master에 머지)'
    if section not in text:
        raise ValueError('README에서 진행 현황 섹션을 찾을 수 없어요.')

    lines = text.splitlines()
    section_index = lines.index(section)
    table_start = next(
        (index for index in range(section_index + 1, len(lines))
         if lines[index].startswith('| Day |')),
        None,
    )
    if table_start is None:
        raise ValueError('진행 현황 표의 헤더를 찾을 수 없어요.')

    table_end = table_start
    while table_end < len(lines) and lines[table_end].startswith('|'):
        table_end += 1
    lines[table_start:table_end] = progress_table().splitlines()
    updated = '\n'.join(lines) + '\n'
    if updated != text:
        README.write_text(updated, encoding='utf-8')
        print('README 진행 현황을 갱신했어요.')
    else:
        print('README 진행 현황에 변경 사항이 없어요.')


if __name__ == '__main__':
    update_readme()
