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
    none=[]
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
                none.append(0)
            else:
                none.append(1)

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

def age_data(afn1,afn2):
    none=[]
    a0_10=[]
    a11_20=[]
    a21_30=[]
    a31_40=[]
    a41_50=[]
    a51_60=[]
    a61_70=[]
    a71_80=[]
    a81_90=[]
    a91_100=[]

    for i in range(0,891):
        if afn1[i]=="":
            afn1[i]=-1

    Age_int = []
    for i in afn1:
        if i is not float:
            Age_int.append(float(i))

    for i in range(0,891):
        if 0 <= Age_int[i] <= 10:
            if afn2[i] == "0":
                a0_10.append(0)
            else:
                a0_10.append(1)
        elif 11 <= Age_int[i] <= 20:
            if afn2[i] == "0":
                a11_20.append(0)
            else:
                a11_20.append(1)
        elif 21 <= Age_int[i] <= 30:
            if afn2[i] == "0":
                a21_30.append(0)
            else:
                a21_30.append(1)
        elif 31 <= Age_int[i] <= 40:
            if afn2[i] == "0":
                a31_40.append(0)
            else:
                a31_40.append(1)
        elif 41 <= Age_int[i] <= 50:
            if afn2[i] == "0":
                a41_50.append(0)
            else:
                a41_50.append(1)
        elif 51 <= Age_int[i] <= 60:
            if afn2[i] == "0":
                a51_60.append(0)
            else:
                a51_60.append(1)
        elif 61 <= Age_int[i] <= 70:
            if afn2[i] == "0":
                a61_70.append(0)
            else:
                a71_80.append(1)
        elif 71 <= Age_int[i] <= 80:
            if afn2[i] == "0":
                a71_80.append(0)
            else:
                a71_80.append(1)
        elif 81 <= Age_int[i] <= 90:
            if afn2[i] == "0":
                a81_90.append(0)
            else:
                a81_90.append(1)
        elif 91 <= Age_int[i] <= 100:
            if afn2[i] == "0":
                a91_100.append(0)
            else:
                a91_100.append(1)
        else:
            if afn2[i] == "0":
                none.append(0)
            else:
                none.append(1)

def embarked_data(efn1,efn2):
    s=[]
    c=[]
    q=[]

    for i in range(0,891):
        if efn1[i] == "S":
            if efn2[i] =="0":
                s.append(0)
            else:
                s.append(1)
        elif efn1[i] == "C":
            if efn2[i] =="0":
                c.append(0)
            else:
                c.append(1)
        else:
            if efn2[i] == "0":
                q.append(0)
            else:
                q.append(1)

def parch_data(pfn1,pfn2):
    #max(pfn1) #6
    par0=[]
    par1=[]
    par2=[]
    par3=[]
    par4=[]
    par5=[]
    par6=[]

    for i in range(0,891):
        if pfn1[i] == "0":
            if pfn2[i] == "0":
                par0.append(0)
            else:
                par0.append(1)

        elif pfn1[i] == "1":
            if pfn2[i] == "0":
                par1.append(0)
            else:
                par1.append(1)

        elif pfn1[i] == "2":
            if pfn2[i] == "0":
                par2.append(0)
            else:
                par2.append(1)

        elif pfn1[i] == "3":
            if pfn2[i] == "0":
                par3.append(0)
            else:
                par3.append(1)
        elif pfn1[i] == "4":
            if pfn2[4] == "0":
                par4.append(0)
            else:
                par4.append(1)
        elif pfn1[i] == "5":
            if pfn2[i] == "0":
                par5.append(0)
            else:
                par5.append(1)
        elif pfn1[i] == "6":
            if pfn2[i] == "0":
                par6.append(0)
            else:
                par6.append(1)

    print(par0)
    print(par1)
    print(par2)
    print(par3)
    print(par4)
    print(par5)
    print(par6)


if  __name__ == "__main__":
    #rap=read_csv()
    #rap2=parsing(rap)
    #save_csv(rap2)
    d1=csv_connect1("Parch.csv")
    d2=csv_connect2()
    #Cabin_data(d1,d2) #cabin 데이터
    #age_data(d1,d2) #age 데이터
    #embarked_data(d1,d2) #embarked 데이터
    parch_data(d1,d2)