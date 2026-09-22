#!/usr/bin/env python3
"""Build the bilingual reader from the repository's Markdown. No network required."""
from pathlib import Path
import html,json,os,re,shutil
from urllib.parse import urlsplit,urlunsplit
import markdown
from markdown.extensions.toc import slugify_unicode
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_site'
COURSE=json.loads((ROOT/'site/course.json').read_text())
if OUT.exists():shutil.rmtree(OUT)
OUT.mkdir()
for name in ('assets','exercises','templates','site'):
    shutil.copytree(ROOT/name,OUT/name,ignore=shutil.ignore_patterns('__pycache__','.DS_Store'))
(OUT/'.nojekyll').touch()
index=[]
pages=[p for p in ROOT.rglob('*.md') if not any(x in p.relative_to(ROOT).parts for x in ('_site','.git','.github'))]
for p in pages:
    rel=p.relative_to(ROOT); target=OUT/rel.with_suffix('.html');target.parent.mkdir(parents=True,exist_ok=True)
    lang='en' if 'en' in rel.parts or p.name.endswith('.en.md') else 'zh-CN'
    en=lang=='en';t=COURSE['titles'][lang]
    def url(path):return os.path.relpath(OUT/path,target.parent).replace(os.sep,'/')
    md=markdown.Markdown(extensions=['tables','fenced_code','toc','md_in_html'], extension_configs={'toc':{'slugify':slugify_unicode}})
    soup=BeautifulSoup(md.convert(p.read_text()),'html.parser')
    title=soup.h1.get_text() if soup.h1 else p.stem
    # Reader chrome carries language and chapter navigation; Markdown keeps its own.
    if rel.parts[:1]==('docs',):
        for para in list(soup.find_all('p')):
            if '简体中文' in para.get_text() and 'English' in para.get_text() and len(para.get_text())<55:para.decompose()
        hrs=soup.find_all('hr')
        if hrs:
            last=hrs[-1]
            sib=last.find_next_sibling()
            if sib and sib.name=='p' and ('目录' in sib.get_text() or 'Contents' in sib.get_text()):sib.decompose();last.decompose()
    for a in soup.find_all('a',href=True):
        u=urlsplit(a['href'])
        if not u.scheme and u.path.endswith('.md'):a['href']=urlunsplit(('', '',u.path[:-3]+'.html',u.query,u.fragment))
    for im in soup.find_all('img'):
        im['loading']='lazy';im['decoding']='async';im['tabindex']='0';im['role']='button';im['aria-label']=('Enlarge: ' if en else '放大图片：')+im.get('alt','')
    for table in list(soup.find_all('table')):
        wrap=soup.new_tag('div',attrs={'class':'table-scroll','tabindex':'0'});table.wrap(wrap)
    slug=p.stem; chapter=COURSE['slugs'].index(slug) if slug in COURSE['slugs'] else None
    other='zh-CN' if en else 'en';alt=Path(str(rel).replace(f'/{lang}/',f'/{other}/'))
    if rel==Path('exercises/README.en.md'):alt=Path('exercises/README.md')
    elif rel==Path('exercises/README.md'):alt=Path('exercises/README.en.md')
    elif alt==rel or not (ROOT/alt).exists():alt=Path('docs')/other/'README.md'
    switch=url(alt.with_suffix('.html'))
    nav=''
    groups=[(0,5,'文件准备','File preparation'),(5,10,'机器与首件','Machine & first part'),(10,16,'作业与进阶','Jobs & next steps')]
    for start,end,zh,eng in groups:
        nav+=f'<div class="nav-group">{html.escape(eng if en else zh)}</div>'
        for i in range(start,end):
            active=' aria-current="page"' if chapter==i else ''
            nav+=f'<a{active} href="{url(Path("docs")/lang/(COURSE["slugs"][i]+".html"))}"><span>{i:02d}</span>{html.escape(t[i])}</a>'
    toc=''.join(f'<a href="#{h.get("id","")}">{html.escape(h.get_text())}</a>' for h in soup.find_all('h2'))
    seq=''
    if chapter is not None:
        for i,label in [(chapter-1,'Previous' if en else '上一章'),(chapter+1,'Next' if en else '下一章')]:
            if 0<=i<16:seq+=f'<a href="{url(Path("docs")/lang/(COURSE["slugs"][i]+".html"))}"><small>{label}</small><strong>{i:02d} · {html.escape(t[i])}</strong></a>'
    safe_title=html.escape(title)
    html_page=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="A bilingual practical laser-cutting guide: drawing, toolpath, machine setup and inspection."><title>{safe_title} · Laser cutting guide</title><link rel="stylesheet" href="{url(Path('site/reader.css'))}"></head>
<body data-lang="{lang}" data-root="{url(Path('.'))}/"><a class="skip" href="#reading">{'Skip to content' if en else '跳到正文'}</a>
<header class="top"><button class="menu-button" aria-label="{'Open contents' if en else '打开目录'}" aria-controls="sidebar" aria-expanded="false">☰</button><a class="brand" href="{url(Path('docs')/lang/'README.html')}"><span class="brand-mark" aria-hidden="true">⌗</span><span>{'LASER CUTTING' if en else '激光切割操作入门'}<small>{'A practical field guide' if en else '从图纸到第一件零件'}</small></span></a><div class="top-actions"><button class="search-open">{'Search' if en else '搜索教程'} <kbd>/</kbd></button><a class="language" href="{switch}" lang="{other}">{'简体中文' if en else 'English'}</a><a class="github" href="https://github.com/mx3353672833-debug/laser-cutting-guide">GitHub ↗</a></div></header>
<div class="layout"><aside id="sidebar" class="sidebar"><p class="sidebar-label">{'COURSE / 16 CHAPTERS' if en else '学习路线 / 16 章'}</p><nav aria-label="{'Chapters' if en else '章节'}">{nav}</nav><div class="nav-group">{'Reference' if en else '随手查'}</div><a href="{url(Path('docs')/lang/'glossary.html')}">{'Glossary' if en else '术语表'}</a><a href="{url(Path('exercises/README.en.html' if en else 'exercises/README.html'))}">{'DXF exercises' if en else 'DXF 与答案'}</a><a href="{url(Path('docs')/lang/'sources.html')}">{'Sources' if en else '资料来源'}</a><a href="{url(Path('docs')/lang/'version-scope.html')}">{'Versions & scope' if en else '版本与适用范围'}</a></aside>
<main id="reading"><div class="eyebrow">{'FIELD NOTES' if en else '操作笔记'} <span>v0.2 · {'Bilingual edition' if en else '中英文版'}</span></div><article>{soup}</article><nav class="chapter-next" aria-label="{'Chapter navigation' if en else '章节导航'}">{seq}</nav><footer><a href="https://github.com/mx3353672833-debug/laser-cutting-guide/issues/new/choose">{'Report a problem with this lesson' if en else '这一页有问题？提交勘误'}</a><span>{'Documented concepts. Machine settings remain equipment-specific.' if en else '按对应软件学习，按实际机器验证。'}</span></footer></main>
<aside class="toc"><span>{'On this page' if en else '本章内容'}</span>{toc}</aside></div>
<dialog class="search-dialog"><form method="dialog"><button class="close" aria-label="{'Close' if en else '关闭'}">×</button></form><label for="search-input">{'Search this guide' if en else '搜索章节与正文'}</label><input id="search-input" type="search" autocomplete="off" placeholder="{'Try kerf, units, pressure…' if en else '试试：补偿、单位、寻边…'}"><div class="search-results" aria-live="polite"></div></dialog>
<dialog class="image-dialog"><form method="dialog"><button class="close" aria-label="{'Close image' if en else '关闭图片'}">×</button></form><img alt=""><p></p></dialog><script src="{url(Path('site/reader.js'))}" defer></script></body></html>'''
    target.write_text(html_page)
    if 'learn' not in rel.parts:
        index.append({'title':title,'path':str(rel.with_suffix('.html')),'lang':lang,'chapter':chapter is not None and rel.parts[0]=='docs','text':soup.get_text(' ',strip=True)})
(OUT/'search-index.json').write_text(json.dumps(index,ensure_ascii=False))
(OUT/'index.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=docs/zh-CN/00-start-here.html"><title>Laser cutting guide</title><a href="docs/zh-CN/00-start-here.html">简体中文</a> · <a href="docs/en/00-start-here.html">English</a></html>')
print(f'Built {len(pages)} pages in {OUT}')
