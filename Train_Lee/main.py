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

    o2 = open("Survived.csv", "r", encoding="utf-8")
    file2 = csv.reader(o2)

    csv_file=[]
    for i in file1:
        for j in i:
            csv_file.append(j)
    csv_file.pop(0)


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

    return csv_file,sv_file

def count_data(datafile):
    count=[]

    for i in datafile:
        count.append(i)

    return count

def Cabin_data(fn1,fn2,cd):
    cabin_list=[[],[],[],[],[],[],[],[]] #none~g
    c_dict={0:"A", 1:"B", 2:"C",3:"D",4:"E",5:"F",6:"G",7:"n"}
    cabin_list_count = len(cabin_list)

    for k in range(len(cd)):
        if fn1[k] == "":
            fn1[k] = "none"
        for j in range(cabin_list_count):
            if fn1[k][0] == c_dict[j]:
                if fn2[k] == 0:
                    cabin_list[j].append(0)
                else:
                    cabin_list[j].append(1)

    return cabin_list

def age_data(afn1,afn2,cd):
    age_list=[[],[],[],[],[],[],[],[],[],[]] #none~90
    a_dict = {0: 0, 1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80}
    a_dict_count = len(a_dict)

    Age_float = []

    for i in afn1:
        for j in range(len(cd)):
            if afn1[j]=="":
                afn1[j]="-1"
        if i is not float:
            Age_float.append(float(i))


    for i in range(len(cd)):
        for j in range(a_dict_count):
            p = a_dict[j] + 10

            if a_dict[j] <= Age_float[i] < p:
                if afn2[i] == 0:
                    age_list[j].append(0)
                else:
                    age_list[j].append(1)

            else:
                if afn2[i] == 0:
                    age_list[-1].append(0)
                else:
                    age_list[-1].append(1)

    return age_list



def embarked_data(efn1,efn2,cd):
    embarked_list = [[], [], [], []]  # C, Q, S, none
    e_dict = {0: "C", 1: "Q", 2: "S"}
    embarked_list_count = len(embarked_list) - 1

    for i in range(len(cd)):
        if efn1[i] == "":
            if efn2[i] ==0:
                embarked_list[-1].append(0)
            else:
                embarked_list[-1].append(0)
        for j in range(embarked_list_count):
            if efn1[i] == e_dict[j]:
                if efn2[i] == 0:
                    embarked_list[j].append(0)
                else:
                    embarked_list[j].append(1)

    return embarked_list

def parch_data(pfn1,pfn2,cd):
    #max(pfn1) #6
    parch_list = [[],[],[],[],[],[],[]] #0~6
    p_int=[]
    parch_list_count = len(parch_list)


    for i in range(len(cd)):
        if pfn1[i] is not int:
            p_int.append(int(pfn1[i]))
        for j in range(parch_list_count):
            if p_int[i] == j:
                if pfn2[i] == 0:
                    parch_list[j].append(0)
                else:
                    parch_list[j].append(1)

    return parch_list

def fare_data(ffn1,ffn2,cd):
    fare_list=[[],[],[],[],[],[]] #0~50,50이상
    f_dict={0:0,1:10,2:20,3:30,4:40}
    f_dict_count = len(f_dict)
    fare_f=[]

    for i in ffn1:
        if i is not float:
            fare_f.append(float(i))

    for i in range(len(cd)):
        if 50<= fare_f[i]:
            if ffn2[i] == 0:
                fare_list[-1].append(0)
            else:
                fare_list[-1].append(1)
        for j in range(f_dict_count):
            p = f_dict[j] + 10
            if f_dict[j] <= fare_f[i] < p:
                if ffn2[i] == 0:
                    fare_list[j].append(0)
                else:
                    fare_list[j].append(1)

    return fare_list

def pclass_data(ppfn1,ppfn2,cd):
    pclass_list=[[],[],[]] #1,2,3
    p_dict={0:1, 1:2, 2:3}
    pclass_int=[]

    for i in ppfn1:
        if i is not int:
            pclass_int.append(int(i))

    for i in range(len(cd)):
        for j in range(0,3):
            if pclass_int[i] == p_dict[j]:
                if ppfn2[i] == 0:
                    pclass_list[j].append(0)
                else:
                    pclass_list[j].append(1)

    return pclass_list

def sex_data(sfn1,sfn2,cd):
    sex_list=[[],[]] #male, female

    for i in range(len(cd)):
        if sfn1[i]=="male":
            if sfn2[i]==0:
                sex_list[0].append(0)
            else:
                sex_list[0].append(1)
        else:
            if sfn2[i]==0:
                sex_list[1].append(0)
            else:
                sex_list[1].append(1)

    return sex_list


def sibsp_data(ssfn1,ssfn2,cd):
    #max(ssfn1) #max8
    sibsp_list=[[],[],[],[],[],[],[],[],[]] #0~8
    sibsp_list_count = len(sibsp_list)
    sibsp_int=[]
    for i in ssfn1:
        if i is not int:
            sibsp_int.append(int(i))

    for i in range(len(cd)):
        for j in range(sibsp_list_count):
            if sibsp_int[i] == j:
                if ssfn2[i] == 0:
                    sibsp_list[j].append(0)
                else:
                    sibsp_list[j].append(1)

    return sibsp_list

def make_gr(dn,cn):
    x = np.arange(len(dn))  # x값 개수
    data_name = {"Cabin":["A", "B", "C", "D", "E", "F", "G","NONE"],"Age":["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","NONE"],"Embarked":["C", "Q", "S","none"],
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


    for i in range(len(dn)):
        print(len(dn[i]))

if  __name__ == "__main__":
    #rap=read_csv()
    #rap2=parsing(rap)
    #save_csv(rap2)
    d1,d2=csv_connect1("Fare.csv")
    d3=count_data(d1)
    #cabin=Cabin_data(d1,d2,d3) #cabin 데이터
    #age=age_data(d1,d2,d3) #age 데이터
    #embarked=embarked_data(d1,d2,d3) #embarked 데이터
    #parch=parch_data(d1,d2,d3) #parch 데이터
    fare=fare_data(d1,d2,d3) #fare 데이터
    #pclass=pclass_data(d1,d2,d3) #pclass 데이터
    #sex=sex_data(d1,d2,d3) #sex 데이터
    #sibsp=sibsp_data(d1,d2,d3) #sibsp 데이터
    make_gr(fare,"Fare")