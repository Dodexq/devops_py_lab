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
    with open(f"{outdir}{ids}.md", "w") as writef:
        writef.write(mdout)
def mdtopptx():
    outdir = f"../out/"
    subprocess.call(["pandoc","-o",f"{outdir}homework.pptx", \
        f"{outdir}8483040.md", f"{outdir}13883932.md", \
            f"{outdir}70598275.md", f"{outdir}65374769.md"])