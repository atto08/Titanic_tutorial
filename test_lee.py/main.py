import csv
import matplotlib.pyplot as plt
import numpy as np

def read_csv():
    o=open("../test.csv","r",encoding="utf-8")
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



if __name__ == "__main__":
    #rap = read_csv()
    #rap2 = parsing(rap)
    #save_csv(rap2)
    Pclass_gr()
    Sex_gr()
    Age_gr()
    Embarked_gr()
