import csv

def read_csv():
    o=open("train.csv", "r", encoding="utf-8")
    rd=csv.reader(o)
    ret=[]
    for i in rd:
        ret.append(i)

    return ret

def parsing(data):
    file1=[]
    file2=[[],[],[],[],[],[],[],[],[],[],[],[]]
    for line in data:
        file1.append(line)
    for i in range(0,12):
        for j in range(0,892):
            file2[i].append(file1[j][i])

    return file2


def save_csv(data2):
    name = {"0": "PassengerId", "1": "Survived", "2": "Pclass", "3": "Name", "4": "Sex", "5": "Age", "6": "SibSp",
            "7": "Parch", "8": "Ticket", "9": "Fare", "10": "Cabin", "11": "Embarked"}

    for n in range(0,12):
        with open(name[str(n)]+".csv", "w", newline="") as f:
            writer = csv.writer(f)

            for i in range(0,892):
                writer.writerows([[data2[n][i]]])

            f.close()

def csv_connect1(file_name1):
    o1 = open(file_name1, "r", encoding="utf-8")
    file1 = csv.reader(o1)

    csv_file=[]
    for i in file1:
        for j in i:
            csv_file.append(j)
    csv_file.pop(0)

    return csv_file

def csv_connect2():
    o2 = open("Survived.csv", "r", encoding="utf-8")
    file2 = csv.reader(o2)

    survive_file = []
    for i in file2:
        for j in i:
            survive_file.append(j)
    survive_file.pop(0)

    return survive_file


def Cabin_data(fn1,fn2):
    space=[]
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    for i in range(0,891):
        if fn1[i] == "":
            if fn2[i] == "0":
                space.append(0)
            else:
                space.append(1)

    while "" in fn1:
        fn1.remove("")#"" 제외한 fn1 데이터 개수:204

    for i in range(0,204):
        if fn1[i][0] == "A":
            if fn2[i] == "0":
                a.append(0)
            else:
                a.append(1)
        elif fn1[i][0] == "B":
            if fn2[i] == "0":
                b.append(0)
            else:
                b.append(1)
        elif fn1[i][0] == "C":
            if fn2[i] == "0":
                c.append(0)
            else:
                c.append(1)
        elif fn1[i][0] == "D":
            if fn2[i] == "0":
                d.append(0)
            else:
                d.append(1)
        elif fn1[i][0] == "E":
            if fn2[i] == "0":
                e.append(0)
            else:
                e.append(1)
        elif fn1[i][0] == "F":
            if fn2[i] == "0":
                f.append(0)
            else:
                f.append(1)
        elif fn1[i][0] == "G":
            if fn2[i] == "0":
                g.append(0)
            else:
                g.append(1)


if  __name__ == "__main__":
    #rap=read_csv()
    #rap2=parsing(rap)
    #save_csv(rap2)
    d1=csv_connect1("Cabin.csv")
    d2=csv_connect2()
    Cabin_data(d1 , d2)