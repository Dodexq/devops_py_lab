from encodings import utf_8
import os
import markdown2input as m2i
import slide2md
import subprocess

def create_tmp():
    incsv = m2i.inputmd()
    for i in incsv:
        slide_md = slide2md.slide.format_map(i)
        marktooutput(slide_md, i["product_id"])

def marktooutput(mdout, ids):
    os.chdir(os.path.dirname(__file__))
    outdir = f"../out/"
    with open(f"{outdir}{ids}.md", encoding="utf-8", mode="w") as writef:
        writef.write(mdout)
        
def mdtopptx():
    os.chdir("../out/")
    allmdout = os.listdir()
    subprocess.call(["pandoc","-o", "hw.pptx", *allmdout])