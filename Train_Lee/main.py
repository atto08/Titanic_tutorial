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

    s_file = []

    for i in survive_file:
        for j in i:
            if j is not int:
                s_file.append(int(j))

    return s_file

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

    for a in range(0,7):
        print(len(c_file[a]))

    x = np.arange(8) #x값 개수
    Pc = ["A", "B", "C", "D", "E", "F", "G", "NONE"] #x값
    values = [c_file[1].count(1)/len(c_file[1])*100,c_file[2].count(1)/len(c_file[2])*100,c_file[3].count(1)/len(c_file[3])*100,c_file[4].count(1)/len(c_file[4])*100,
              c_file[5].count(1)/len(c_file[5])*100,c_file[6].count(1)/len(c_file[6])*100,c_file[7].count(1)/len(c_file[7])*100,c_file[0].count(1)/len(c_file[0])*100] #y값
    colors = ["tab:blue","tab:orange","tab:green","tab:red","tab:purple","tab:brown","tab:pink"
              ,"tab:gray"] #막대 컬러
    for i in range(len(Pc)):
        plt.bar(x, values, color=colors[i], label=Pc[i]) #데이터 값, 막대 컬러 적용
    plt.xticks(x, Pc) #x를 순서대로 나열

    plt.title("Survival rate by cabin") #차트 제목
    plt.xlabel("cabin") #x축 레이블
    plt.ylabel("values") #y축 레이블

    plt.ylim(0,100) #y축 범위

    bar = plt.bar(x, values, color=colors) #텍스트 삽입
    for rect in bar:
        height=rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.0,height,"%.1f"%height,ha="center",va="bottom",size=12)

    plt.legend()

    plt.show()

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

    for i in range(0,10):
        print(len(a_file[i]))

    x = np.arange(10)  # x값 개수
    Pc = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","none"]  # x값
    values = [a_file[0].count(1)/len(a_file[0])*100, a_file[1].count(1) / len(a_file[1]) * 100, a_file[2].count(1) / len(a_file[2]) * 100, a_file[3].count(1) / len(a_file[3]) * 100,
              a_file[4].count(1) / len(a_file[4]) * 100,a_file[5].count(1) / len(a_file[5]) * 100, a_file[6].count(1) / len(a_file[6]) * 100,
              a_file[7].count(1) / len(a_file[7]) * 100,a_file[8].count(1) / len(a_file[8])*100, a_file[9].count(1) / len(a_file[9])*100]  # y값
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown",
              "tab:pink", "tab:gray", "tab:olive","tab:cyan"]  # 막대 컬러
    for i in range(len(Pc)):
        plt.bar(x, values, color=colors[i], label=Pc[i])  # 데이터 값, 막대 컬러 적용
    plt.xticks(x, Pc)  # x를 순서대로 나열

    plt.title("Survival rate by Age")  # 차트 제목
    plt.xlabel("age")  # x축 레이블
    plt.ylabel("values")  # y축 레이블

    plt.ylim(0, 100)  # y축 범위

    bar = plt.bar(x, values, color=colors)  # 텍스트 삽입
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, "%.1f" % height, ha="center", va="bottom", size=12)

    plt.legend()

    plt.show()

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



    x = np.arange(3)  # x값 개수
    Pc = ["C", "Q", "S"]  # x값
    values = [e_file[0].count(1) / len(e_file[0]) * 100, e_file[1].count(1) / len(e_file[1]) * 100,
              e_file[2].count(1) / len(e_file[2]) * 100]

    colors = ["tab:blue", "tab:orange", "tab:green"]  # 막대 컬러
    for i in range(len(Pc)):
        plt.bar(x, values, color=colors[i], label=Pc[i])  # 데이터 값, 막대 컬러 적용
    plt.xticks(x, Pc)  # x를 순서대로 나열

    plt.title("Survival rate by embarked")  # 차트 제목
    plt.xlabel("embarked")  # x축 레이블
    plt.ylabel("values")  # y축 레이블

    plt.ylim(0, 100)  # y축 범위

    bar = plt.bar(x, values, color=colors)  # 텍스트 삽입
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, "%.1f" % height, ha="center", va="bottom", size=12)

    plt.legend()

    plt.show()

    print(len(e_file[0]),len(e_file[1]),len(e_file[2]),len(e_file[3]))

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

    for i in range(0,7):
        print(len(p_file[i]))


    x = np.arange(7)  # x값 개수
    Pc = ["0","1","2","3","4","5","6"]  # x값
    values = [p_file[0].count(1) / len(p_file[0]) * 100, p_file[1].count(1) / len(p_file[1]) * 100,
              p_file[2].count(1) / len(p_file[2]) * 100, p_file[3].count(1) / len(p_file[3]) * 100, p_file[4].count(1) / len(p_file[4]) * 100,
              p_file[5].count(1) / len(p_file[5]) * 100, p_file[6].count(1) / len(p_file[6]) * 100]

    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown",
              "tab:pink"]  # 막대 컬러

    for i in range(len(Pc)):
        plt.bar(x, values, color=colors[i], label=Pc[i])  # 데이터 값, 막대 컬러 적용
    plt.xticks(x, Pc)  # x를 순서대로 나열

    plt.title("Survival rate by Parch")  # 차트 제목
    plt.xlabel("parch")  # x축 레이블
    plt.ylabel("values")  # y축 레이블

    plt.ylim(0, 100)  # y축 범위

    bar = plt.bar(x, values, color=colors)  # 텍스트 삽입
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, "%.1f" % height, ha="center", va="bottom", size=12)

    plt.legend()

    plt.show()

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


    x = np.arange(6)  # x값 개수
    Pc = ["0-10","11-20","21-30","31-40","41-50","over_50"]  # x값
    values = [f_file[0].count(1) / len(f_file[0]) * 100, f_file[1].count(1) / len(f_file[1]) * 100,
              f_file[2].count(1) / len(f_file[2]) * 100, f_file[3].count(1) / len(f_file[3]) * 100, f_file[4].count(1) / len(f_file[4]) * 100,
              f_file[5].count(1) / len(f_file[5]) * 100]
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown"]  # 막대 컬러

    for i in range(len(Pc)):
        plt.bar(x, values, color=colors[i], label=Pc[i])  # 데이터 값, 막대 컬러 적용
    plt.xticks(x, Pc)  # x를 순서대로 나열

    plt.title("Survival rate by Fare")  # 차트 제목
    plt.xlabel("fare")  # x축 레이블
    plt.ylabel("values")  # y축 레이블

    plt.ylim(0, 100)  # y축 범위

    bar = plt.bar(x, values, color=colors)  # 텍스트 삽입
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, "%.1f" % height, ha="center", va="bottom", size=12)

    plt.legend()

    plt.show()
    for i in range(0,6):
        print(len(f_file[i]))

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


    x = np.arange(3)  # x값 개수
    Pc = ["1","2","3"]  # x값
    values = [p_file[0].count(1) / len(p_file[0]) * 100,
              p_file[1].count(1) / len(p_file[1]) * 100, p_file[2].count(1) / len(p_file[2])*100]

    colors = ["tab:blue", "tab:orange", "tab:green"]  # 막대 컬러

    for i in range(len(Pc)):
        plt.bar(x, values, color=colors[i], label=Pc[i])  # 데이터 값, 막대 컬러 적용
    plt.xticks(x, Pc)  # x를 순서대로 나열

    plt.title("Survival rate by Pclass")  # 차트 제목
    plt.xlabel("Pclass")  # x축 레이블
    plt.ylabel("values")  # y축 레이블

    plt.ylim(0, 100)  # y축 범위

    bar = plt.bar(x, values, color=colors)  # 텍스트 삽입
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, "%.1f" % height, ha="center", va="bottom", size=12)

    plt.legend()

    plt.show()

    for i in range(0,2):
        print(p_file[i])

def sex_data(sfn1,sfn2):
    male=[]
    female=[]

    for i in range(0,891):
        if sfn1[i]=="male":
            if sfn2[i]=="0":
                male.append(0)
            else:
                male.append(1)
        else:
            if sfn2[i]=="0":
                female.append(0)
            else:
                female.append(1)
    print(len(male),len(female))

    x = np.arange(2)  # x값 개수
    Pc = ["male","female"]  # x값
    values = [male.count(1) / len(male) * 100, female.count(1) / len(female) * 100]

    colors = ["tab:blue", "tab:orange"]  # 막대 컬러

    for i in range(len(Pc)):
        plt.bar(x, values, color=colors[i], label=Pc[i])  # 데이터 값, 막대 컬러 적용
    plt.xticks(x, Pc)  # x를 순서대로 나열

    plt.title("Survival rate by Sex")  # 차트 제목
    plt.xlabel("sex")  # x축 레이블
    plt.ylabel("values")  # y축 레이블

    plt.ylim(0, 100)  # y축 범위

    bar = plt.bar(x, values, color=colors)  # 텍스트 삽입
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, "%.1f" % height, ha="center", va="bottom", size=12)

    plt.legend()

    plt.show()
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


    x = np.arange(9)  # x값 개수
    Pc = ["0","1","2","3","4","5","6","7","8"]  # x값
    values = [s_file[0].count(1) / len(s_file[0]) * 100, s_file[1].count(1) / len(s_file[1]) * 100, s_file[2].count(1) / len(s_file[2]) * 100,
              s_file[3].count(1) / len(s_file[3]) * 100, s_file[4].count(1) / len(s_file[4]) * 100, s_file[5].count(1) / len(s_file[5]) * 100,
              0,0, s_file[8].count(1) / len(s_file[8]) * 100]

    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown",
              "tab:pink", "tab:gray", "tab:olive"]  # 막대 컬러

    for i in range(len(Pc)):
        plt.bar(x, values, color=colors[i], label=Pc[i])  # 데이터 값, 막대 컬러 적용
    plt.xticks(x, Pc)  # x를 순서대로 나열

    plt.title("Survival rate by Sibsp")  # 차트 제목
    plt.xlabel("sibsp")  # x축 레이블
    plt.ylabel("values")  # y축 레이블

    plt.ylim(0, 100)  # y축 범위

    bar = plt.bar(x, values, color=colors)  # 텍스트 삽입
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, "%.1f" % height, ha="center", va="bottom", size=12)

    plt.legend()

    plt.show()

    for i in range(0,9):
        print(len(s_file[i]))

if  __name__ == "__main__":
    #rap=read_csv()
    #rap2=parsing(rap)
    #save_csv(rap2)
    d1=csv_connect1("Age.csv")
    d2=csv_connect2()
    #Cabin_data(d1,d2) #cabin 데이터
    age_data(d1,d2) #age 데이터
    #embarked_data(d1,d2) #embarked 데이터
    #parch_data(d1,d2) #parch 데이터
    #fare_data(d1,d2) #fare 데이터
    #pclass_data(d1,d2) #pclass 데이터
    #sex_data(d1,d2) #sex 데이터
    #sibsp_data(d1,d2) #sibsp 데이터
