import csv
import matplotlib.pyplot as plt
import numpy as np

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

    sv_file = []

    for i in survive_file:
        for j in i:
            if j is not int:
                sv_file.append(int(j))

    return sv_file

def Cabin_data(fn1,fn2):
    c_file=[[],[],[],[],[],[],[],[]] #none~g
    c_dict={0:"n", 1:"A", 2:"B",3:"C",4:"D",5:"E",6:"F",7:"G"}

    for i in range(0,891):
        if fn1[i] == "":
            fn1[i] = "none"

    for k in range(0,891):
        for j in range(0,8):
            if fn1[k][0] == c_dict[j]:
                if fn2[k] == 0:
                    c_file[j].append(0)
                else:
                    c_file[j].append(1)

    return c_file

def age_data(afn1,afn2):
    a_file=[[],[],[],[],[],[],[],[],[],[]] #none~90

    for i in range(0,891):
        if afn1[i]=="":
            afn1[i]=-1

    Age_int = []
    for i in afn1:
        if i is not float:
            Age_int.append(float(i))

    for i in range(0,891):
        for j in range(0,81,10):
            k = j + 10
            n = j / 10
            m = int(n)

            if j <= Age_int[i] < k:
                if afn2[i] == 0:
                    a_file[m].append(0)
                else:
                    a_file[m].append(1)

        if Age_int[i] == -1:
            if afn2[i] == 0:
                a_file[9].append(0)
            else:
                a_file[9].append(1)

    return a_file

def embarked_data(efn1,efn2):
    e_file = [[], [], [], []]  # C, Q, S, none
    e_dict = {0: "C", 1: "Q", 2: "S"}

    for i in range(0, 891):
        for j in range(0, 3):
            if efn1[i] == e_dict[j]:
                if efn2[i] == 0:
                    e_file[j].append(0)
                else:
                    e_file[j].append(1)

    for i in range(0, 891):
        if efn1[i] == "":
            if efn2[i] ==0:
                e_file[3].append(0)
            else:
                e_file[3].append(0)

    return e_file

def parch_data(pfn1,pfn2):
    #max(pfn1) #6
    p_file=[[],[],[],[],[],[],[]] #0~6
    p_int=[]

    for n in range(0,891):
        if pfn1[n] is not int:
            p_int.append(int(pfn1[n]))

    for i in range(0,891):
        for j in range(0,7):
            if p_int[i] == j:
                if pfn2[i] == 0:
                    p_file[j].append(0)
                else:
                    p_file[j].append(1)

    return p_file

def fare_data(ffn1,ffn2):
    f_file=[[],[],[],[],[],[]] #0~50,50이상
    fare_f=[]

    for i in ffn1:
        if i is not float:
            fare_f.append(float(i))

    for i in range(0, 891):
        for j in range(0, 41, 10):
            k = j + 10
            n = j / 10
            m = int(n)

            if j <= fare_f[i] < k:
                if ffn2[i] == 0:
                    f_file[m].append(0)
                else:
                    f_file[m].append(1)
    for i in range(0,891):
        if 50 <= fare_f[i]:
            if ffn2[i] == 0:
                f_file[5].append(0)
            else:
                f_file[5].append(1)

    return f_file


def pclass_data(ppfn1,ppfn2):
    p_file=[[],[],[]] #1,2,3
    p_dict={0:1,1:2,2:3}
    pclass_int=[]

    for i in ppfn1:
        if i is not int:
            pclass_int.append(int(i))

    for i in range(0,891):
        for j in range(0,3):
            if pclass_int[i] == p_dict[j]:
                if ppfn2[i] == 0:
                    p_file[j].append(0)
                else:
                    p_file[j].append(1)

    return p_file

def sex_data(sfn1,sfn2):
    sex_file=[[],[]] #male, female

    for i in range(0,891):
        if sfn1[i]=="male":
            if sfn2[i]==0:
                sex_file[0].append(0)
            else:
                sex_file[0].append(1)
        else:
            if sfn2[i]==0:
                sex_file[1].append(0)
            else:
                sex_file[1].append(1)

    return sex_file


def sibsp_data(ssfn1,ssfn2):
    #max(ssfn1) #max8
    s_file=[[],[],[],[],[],[],[],[],[]] #0~8

    sibsp_int=[]
    for i in ssfn1:
        if i is not int:
            sibsp_int.append(int(i))

    for i in range(0,891):
        for j in range(0,9):
            if sibsp_int[i] == j:
                if ssfn2[i] == 0:
                    s_file[j].append(0)
                else:
                    s_file[j].append(1)

    return s_file


def make_gr(dn,cn):
    x = np.arange(len(dn))  # x값 개수
    data_name = {"Cabin":["A", "B", "C", "D", "E", "F", "G", "NONE"],"Age":["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","NONE"],"Embarked":["C", "Q", "S"],
                 "Parch":["0","1","2","3","4","5","6"],"Fare":["0-10","11-20","21-30","31-40","41-50","over_50"],"Pclass":["1","2","3"],"Sex":["male","female"],"SibSp":["0","1","2","3","4","5","6","7","8"]}

    xdata = data_name[cn]

    values = []
    colors = []
    color_dict = {0:"tab:blue", 1:"tab:orange", 2:"tab:green", 3:"tab:red", 4:"tab:purple", 5:"tab:brown",
             6:"tab:pink", 7:"tab:gray", 8:"tab:olive", 9:"tab:cyan"}


    for i in range(len(dn)):
        colors.append(color_dict[i])
        if dn[i].count(1) == 0:
            values.append(0)
        else:
            values.append(dn[i].count(1) / len(dn[i]) * 100)


    for i in range(len(xdata)):
        plt.bar(x, values, color=colors[i], label=xdata[i])  # 데이터 값, 막대 컬러 적용
    plt.xticks(x, xdata)

    plt.title("Survival rate by"+ cn)  # 차트 제목
    plt.xlabel(cn)  # x축 레이블
    plt.ylabel("percent")  # y축 레이블

    plt.ylim(0, 100)  # y축 범위

    bar = plt.bar(x, values, color=colors)  # 텍스트 삽입

    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, "%.1f" % height, ha="center", va="bottom", size=12)

    plt.legend()

    plt.show()

if  __name__ == "__main__":
    #rap=read_csv()
    #rap2=parsing(rap)
    #save_csv(rap2)
    d1=csv_connect1("Parch.csv")
    d2=csv_connect2()
    #cabib=Cabin_data(d1,d2) #cabin 데이터
    #age=age_data(d1,d2) #age 데이터
    #embarked=embarked_data(d1,d2) #embarked 데이터
    parch=parch_data(d1,d2) #parch 데이터
    #fare=fare_data(d1,d2) #fare 데이터
    #pclass=pclass_data(d1,d2) #pclass 데이터
    #sex=sex_data(d1,d2) #sex 데이터
    #sibsp=sibsp_data(d1,d2) #sibsp 데이터
    make_gr(parch,"Parch")