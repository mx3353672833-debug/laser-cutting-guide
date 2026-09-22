#!/usr/bin/env python3
"""Regenerate teaching DXFs with ezdxf (valid R2010). Offline practice only."""
from pathlib import Path
import ezdxf

def new_doc(insunits=4):
    doc = ezdxf.new("R2010", setup=False)
    doc.header["$INSUNITS"] = insunits
    for ly, c in [("CUT",1),("MARK",2),("TEXT0",8),("TINY",6),("NOTE",3),("SHEET",5)]:
        doc.layers.add(ly, color=c)
    return doc

def main():
    out = Path(__file__).resolve().parents[1]
    doc = new_doc(); m = doc.modelspace()
    m.add_lwpolyline([(0,0),(80,0),(80,40),(0,40)], close=True, dxfattribs={"layer":"CUT"})
    m.add_circle((20,20),4,dxfattribs={"layer":"CUT"}); m.add_circle((60,20),4,dxfattribs={"layer":"CUT"})
    m.add_text("80x40 2-hole plate mm", dxfattribs={"height":4,"layer":"MARK"}).set_placement((2,36))
    doc.saveas(out/"ex01-双孔连接片.dxf")
    doc = new_doc(insunits=1); m = doc.modelspace()
    m.add_lwpolyline([(0,0),(80,0),(80,40),(0,40)], close=True, dxfattribs={"layer":"CUT"})
    m.add_circle((20,20),4,dxfattribs={"layer":"CUT"}); m.add_circle((60,20),4,dxfattribs={"layer":"CUT"})
    m.add_text("INSUNITS=inch but coords drawn as mm", dxfattribs={"height":3,"layer":"NOTE"}).set_placement((2,45))
    doc.saveas(out/"ex02-单位错误.dxf")
    doc = new_doc(); m = doc.modelspace()
    m.add_lwpolyline([(0,0),(60,0),(60,30),(0,30)], close=True, dxfattribs={"layer":"CUT"})
    m.add_line((0,0),(60,0),dxfattribs={"layer":"CUT"}); m.add_line((0,0),(60,0),dxfattribs={"layer":"CUT"})
    m.add_circle((30,15),5,dxfattribs={"layer":"CUT"})
    doc.saveas(out/"ex03-重复线.dxf")
    doc = new_doc(); m = doc.modelspace()
    m.add_line((0,2),(0,40),dxfattribs={"layer":"CUT"})
    m.add_line((0,40),(80,40),dxfattribs={"layer":"CUT"})
    m.add_line((80,40),(80,0),dxfattribs={"layer":"CUT"})
    m.add_line((80,0),(0,0),dxfattribs={"layer":"CUT"})
    m.add_circle((40,20),6,dxfattribs={"layer":"CUT"})
    doc.saveas(out/"ex04-开口轮廓.dxf")
    doc = new_doc(); m = doc.modelspace()
    m.add_lwpolyline([(0,0),(50,0),(50,50),(0,50)], close=True, dxfattribs={"layer":"CUT"})
    m.add_line((10,10),(10.05,10),dxfattribs={"layer":"TINY"})
    m.add_circle((25,25),0.03,dxfattribs={"layer":"TINY"})
    m.add_line((20,20),(20.02,20.02),dxfattribs={"layer":"TINY"})
    doc.saveas(out/"ex05-微小图元.dxf")
    doc = new_doc(); m = doc.modelspace()
    m.add_lwpolyline([(0,0),(100,0),(100,60),(0,60)], close=True, dxfattribs={"layer":"CUT"})
    m.add_lwpolyline([(15,15),(45,15),(45,45),(15,45)], close=True, dxfattribs={"layer":"CUT"})
    m.add_circle((75,30),12,dxfattribs={"layer":"CUT"}); m.add_circle((75,30),5,dxfattribs={"layer":"CUT"})
    doc.saveas(out/"ex06-内外轮廓嵌套.dxf")
    doc = new_doc(); m = doc.modelspace()
    m.add_lwpolyline([(0,0),(70,0),(70,35),(0,35)], close=True, dxfattribs={"layer":"CUT"})
    m.add_circle((18,17.5),5,dxfattribs={"layer":"CUT"})
    m.add_line((35,10),(55,10),dxfattribs={"layer":"MARK"}); m.add_line((35,18),(55,18),dxfattribs={"layer":"MARK"})
    m.add_text("P-01", dxfattribs={"height":4,"layer":"MARK"}).set_placement((35,25))
    m.add_text("center text do not cut", dxfattribs={"height":3,"layer":"TEXT0"}).set_placement((2,31))
    doc.saveas(out/"ex07-工艺分层.dxf")
    doc = new_doc(); m = doc.modelspace()
    for ox in (10,75,140):
        m.add_lwpolyline([(ox,15),(ox+50,15),(ox+50,55),(ox,55)], close=True, dxfattribs={"layer":"CUT"})
        m.add_circle((ox+25,35),6,dxfattribs={"layer":"CUT"})
    m.add_lwpolyline([(5,5),(195,5),(195,80),(5,80)], close=True, dxfattribs={"layer":"SHEET"})
    m.add_text("sheet 190x75 mm ref closed", dxfattribs={"height":4,"layer":"NOTE"}).set_placement((8,70))
    doc.saveas(out/"ex08-多件布局.dxf")
    print("generated 8 dxf via ezdxf")

if __name__ == "__main__":
    main()
