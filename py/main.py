import markdown2output as m2o

if __name__ == "__main__":
    m2o.create_tmp()
    m2o.mdtopptx()
else:
    print("Start program in /main.py")