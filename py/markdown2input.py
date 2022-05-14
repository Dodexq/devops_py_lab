import os
import csv

def inputmd(fieldname=None):
    os.chdir(os.path.dirname(__file__))
    with open("../csv/wb_dquotes.csv", newline="", encoding="utf-8") as fi:
        mydict = csv.DictReader(fi, delimiter=";")
        for row in mydict:
            if fieldname == None:
                yield row
            else:
                yield row[fieldname]