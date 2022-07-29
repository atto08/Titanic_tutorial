import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_csv():
    o=open("test.csv","r",encoding="utf-8")
    rd=csv.reader(o)
    ret=[]
    for i in rd:
        ret.append(i)

        return rd

def parsing(data):
    file1=[]
    file2=[[],[],[],[],[],[],[],[],[],[],[]]
    for line in data:
        file1.append(line)
    for i in range(0,11):
        for j in range(0,418):
            file2[i].append(file1[j][i])

    return file2

def save_csv(data2):
    name = {"0": "PassengerId", "1": "Pclass", "2": "Name", "3": "Sex", "4": "Age", "5": "SibSp", "6": "Parch"
            ,"7":"Ticket", "8": "Fare", "9": "Cabin", "10": "Embarked"}
    for n in range(0,11):
        with open(name[str(n)]+".csv", "w",newline="") as f:
            writer = csv.writer(f)

            writer.writerow(([name[str(n)]]))

            for i in range(0,418):
                     writer.writerows([[data2[n][i]]])

            f.close()

def Pclass_gr():
    o = open("Pclass.csv", "r", encoding="utf-8")
    rd = csv.reader(o)
    Pclass = []
    for i in rd:
        for j in i:
            Pclass.append(j)
    Pclass.pop(0)

    P1=Pclass.count("1")
    P2=Pclass.count("2")
    P3=Pclass.count("3")

            #막대그래프
    x = np.arange(3)
    Pc = ["1","2","3"]
    values = [P1,P2,P3]
    colors = ["r","g","b"]

    plt.bar(x, values, color=colors)
    plt.xticks(x,Pc)


    plt.title("Pclass_values")
    plt.xlabel("Pclass")
    plt.ylabel("values")

    plt.show()


def Sex_gr():
    o = open("Sex.csv", "r", encoding="utf-8")
    rd = csv.reader(o)
    Sex = []
    for i in rd:
        for j in i:
            Sex.append(j)
    Sex.pop(0)

    S1=Sex.count("male")
    S2=Sex.count("female")

    x = np.arange(2)
    Pc = ["male","female"]
    values = [S1,S2]
    colors = ["r","g"]

    plt.bar(x, values, color=colors)
    plt.xticks(x,Pc)


    plt.title("sex_values")
    plt.xlabel("sex")
    plt.ylabel("values")

    plt.show()


def Age_gr():
    o = open("Age.csv", "r", encoding="utf-8")
    rd = csv.reader(o)
    Age = []
    for i in rd:
        for j in i:
            Age.append(j)

    Age.pop(0)

    Age_int = []
    for i in Age:
        if i == "":
            Age.append(-1)
            Aa=Age.count(-1)
        elif i is not float:
            Age_int.append(float(i))


    Age_group = [[],[],[],[],[],[],[],[],[],[]]

    for j in Age_int:
        if j>=0 and j<10:
            Age_group[0].append(j)
        elif j>=10 and j<20:
            Age_group[1].append(j)
        elif j>=20 and j<30:
            Age_group[2].append(j)
        elif j>=30 and j<40:
            Age_group[3].append(j)
        elif j>=40 and j<50:
            Age_group[4].append(j)
        elif j>=50 and j<60:
            Age_group[5].append(j)
        elif j>=60 and j<70:
            Age_group[6].append(j)
        elif j>=70 and j<80:
            Age_group[7].append(j)
        elif j>=80 and j<90:
            Age_group[8].append(j)
        elif j>=90 and j<100:
            Age_group[9].append(j)

    A1=len(Age_group[0])
    A2=len(Age_group[1])
    A3=len(Age_group[2])
    A4=len(Age_group[3])
    A5=len(Age_group[4])
    A6=len(Age_group[5])
    A7=len(Age_group[6])
    A8=len(Age_group[7])
    A9=len(Age_group[8])
    A10=len(Age_group[9])

    x = np.arange(10)
    Pc = ["0~9","10~19","20~29","30~39","40~49","50~59","60~69","70~79","80~89","90~99"]
    values = [A1,A2,A3,A4,A5,A6,A7,A8,A9,A10]
    colors = ["tab:blue","tab:orange","tab:green","tab:red","tab:purple","tab:brown","tab:pink","tab:gray","tab:olive","tab:cyan"]

    plt.bar(x, values, width=0.4)
    plt.bar(x, values, color=colors)
    plt.xticks(x,Pc)


    plt.title("Age_values")
    plt.xlabel("Age")
    plt.ylabel("values")

    plt.show()

def Embarked_gr():
    o = open("Embarked.csv", "r", encoding="utf-8")
    rd = csv.reader(o)
    Embarked = []
    for i in rd:
        for j in i:
            Embarked.append(j)
    Embarked.pop(0)

    E1=Embarked.count("C")
    E2=Embarked.count("S")
    E3=Embarked.count("Q")

    x = np.arange(3)
    Pc = ["C","S","Q"]
    values = [E1,E2,E3]
    colors = ["r","g","b"]

    plt.bar(x, values, color=colors)
    plt.xticks(x,Pc)


    plt.title("Embarked_values")
    plt.xlabel("Embarked")
    plt.ylabel("values")

    plt.show()

if __name__ == "__main__":
    # rap = read_csv()
    # rap2 = parsing(rap)
    # save_csv(rap2)
    Pclass_gr()
    Sex_gr()
    Age_gr()
    Embarked_gr()
