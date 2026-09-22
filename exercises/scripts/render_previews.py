#!/usr/bin/env python3
"""Read teaching DXFs directly; retain DXF +Y up. No machine validation implied."""
from pathlib import Path
from collections import Counter
import ezdxf
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt, font_manager
from matplotlib.patches import Circle

ROOT = Path(__file__).resolve().parents[1]
names = {f.name for f in font_manager.fontManager.ttflist}
font = next((n for n in ['PingFang SC', 'Heiti TC', 'Arial Unicode MS', 'Noto Sans CJK SC'] if n in names), None)
if not font:
    raise RuntimeError('Install a Chinese font before generating Chinese previews')
plt.rcParams['font.family'] = [font]
plt.rcParams['axes.unicode_minus'] = False
colors = {'CUT': '#1967d2', 'SHEET': '#78848e', 'MARK': '#218c58', 'TEXT0': '#8b5fa8', 'TINY': '#c74689', 'NOTE': '#78848e'}

for path in sorted(ROOT.glob('*.dxf')):
    doc = ezdxf.readfile(path)
    fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
    ends = Counter()
    for e in doc.modelspace():
        color = colors.get(e.dxf.layer, '#555555')
        if e.dxftype() == 'LWPOLYLINE':
            pts = [(float(x), float(y)) for x, y in e.get_points('xy')]
            if e.closed:
                pts.append(pts[0])
            ax.plot(*zip(*pts), color=color, lw=1.8)
        elif e.dxftype() == 'LINE':
            start, end = tuple(e.dxf.start)[:2], tuple(e.dxf.end)[:2]
            ax.plot(*zip(start, end), color=color, lw=1.8)
            ends.update([start, end])
        elif e.dxftype() == 'CIRCLE':
            ax.add_patch(Circle(tuple(e.dxf.center)[:2], e.dxf.radius, fill=False, color=color, lw=1.8))
        elif e.dxftype() == 'TEXT':
            ax.text(e.dxf.insert.x, e.dxf.insert.y, e.dxf.text, color=color, fontsize=7)
    if path.name.startswith('ex04'):
        for point, count in ends.items():
            if count == 1:
                ax.scatter(*point, c='#d93025', zorder=5, s=32)
        ax.annotate('左下缺口 2 mm\n端点 (0, 0) 与 (0, 2)', xy=(0, 1), xytext=(12, -12),
                    arrowprops={'arrowstyle':'->', 'color':'#d93025'}, fontsize=10, color='#d93025')
    ax.autoscale_view()
    ax.margins(.14)
    ax.set_aspect('equal', adjustable='box')
    assert not ax.yaxis_inverted()
    unit = '英寸声明，坐标按毫米意图绘制' if doc.units == 1 else '毫米'
    ax.set_title(f'{path.stem}\nDXF 几何预览 · {unit} · Y 轴向上', fontsize=12)
    ax.set_xlabel('X（原始坐标）')
    ax.set_ylabel('Y（原始坐标）')
    ax.grid(alpha=.18)
    fig.savefig(ROOT/'previews'/f'{path.stem}.png', dpi=140)
    plt.close(fig)
    print(path.name, 'preview generated, +Y up, font:', font)
