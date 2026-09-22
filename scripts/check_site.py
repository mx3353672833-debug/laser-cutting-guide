#!/usr/bin/env python3
"""Check generated local destinations, fragments and language counterparts."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]/'_site'
errors=[]; count=0
pages={p:BeautifulSoup(p.read_text(),'html.parser') for p in ROOT.rglob('*.html')}
for p,soup in pages.items():
    for el in soup.select('[href], [src]'):
        ref=el.get('href',el.get('src',''))
        if not ref:continue
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        target=(p.parent/unquote(u.path)).resolve() if u.path else p
        count+=1
        if not target.is_relative_to(ROOT):errors.append(f'{p.relative_to(ROOT)}: escapes site root: {ref}');continue
        if not target.exists():errors.append(f'{p.relative_to(ROOT)}: missing {ref}');continue
        if u.fragment and target.suffix=='.html':
            dst=pages.get(target)
            if dst is not None and not dst.find(id=unquote(u.fragment)):
                errors.append(f'{p.relative_to(ROOT)}: missing fragment {ref}')
    if p.name[:2].isdigit() and '/docs/' in str(p) and '/learn/' not in str(p):
        lang=soup.html.get('lang');switch=soup.select_one('a.language')
        if not switch or Path(urlsplit(switch['href']).path).name!=p.name:errors.append(f'{p.name}: not a same-chapter language switch')
        if switch and switch.get('lang')==lang:errors.append(f'{p.name}: language switch stays in same language')
for row in json.loads((ROOT/'search-index.json').read_text()):
    if not (ROOT/row['path']).is_file():errors.append(f'Search target missing: {row["path"]}')
print(f'{len(pages)} HTML pages; {count} local references; {len(errors)} errors')
for e in errors:print(e)
raise SystemExit(bool(errors))
