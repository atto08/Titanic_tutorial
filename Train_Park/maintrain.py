import csv
import matplotlib.pyplot as plt
import numpy as np

def read_csv():
    o = open('train.csv','r',encoding="utf-8")
    rd = csv.reader(o)
    ret = []
    for i in rd:
        ret.append(i)
        return ret

def parsing(data):




if __name__ == "__main__":
    read_csv()