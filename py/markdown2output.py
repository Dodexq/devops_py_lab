import os
import markdown2input as m2i
import subprocess

def create_tmp():
    incsv = m2i.inputmd()
    for i in incsv:
        slide_md="""
## {model}
:::::::::::::: {{.columns}}
::: {{.column }}
* вендор: {vendor}
* модель: {model}
* артикул: {product_id}
* цена: {price}
:::
::: {{.column }}
![фото товара](../pic/{product_id}.png)
:::
::::::::::::::
""".format_map(i)
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