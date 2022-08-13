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
            fn1[i] = "none"

    for i in range(0,891):
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
        elif fn1[i] == "none":
            if fn2[i] == "0":
                none.append(0)
            else:
                none.append(1)

    x = np.arange(8) #x값 개수
    Pc = ["A", "B", "C", "D", "E", "F", "G", "NONE"] #x값
    values = [a.count(1)/len(a)*100,b.count(1)/len(b)*100,c.count(1)/len(c)*100,d.count(1)/len(d)*100,
              e.count(1)/len(e)*100,f.count(1)/len(f)*100,g.count(1)/len(g)*100,none.count(1)/len(none)*100] #y값
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

    ''' #파이 그래프
    labels = ["A", "B", "C", "D", "E", "F", "G", "NONE"]
    ratio = [a.count(1) / len(a) * 100, b.count(1) / len(b) * 100, c.count(1) / len(c) * 100, d.count(1) / len(d) * 100,
             e.count(1) / len(e) * 100, f.count(1) / len(f) * 100, g.count(1) / len(g) * 100,
             none.count(1) / len(none) * 100]

    plt.pie(ratio, labels=labels, autopct="%.1f%%")
    '''

    print(len(a),len(b),len(c),len(d),len(e),len(f),len(g),len(none))


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

    #max(afn1) #max 80

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
        else:
            if afn2[i] == "0":
                none.append(0)
            else:
                none.append(1)

    print(len(a0_10), len(a11_20), len(a21_30), len(a31_40), len(a41_50), len(a51_60), len(a61_70), len(a71_80),len(none))

    x = np.arange(8)  # x값 개수
    Pc = ["0-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80"]  # x값
    values = [a0_10.count(1) / len(a0_10) * 100, a11_20.count(1) / len(a11_20) * 100, a21_30.count(1) / len(a21_30) * 100,
              a31_40.count(1) / len(a31_40) * 100,a41_50.count(1) / len(a41_50) * 100, a51_60.count(1) / len(a51_60) * 100,
              a61_70.count(1) / len(a61_70) * 100,a71_80.count(1) / len(a71_80)]  # y값
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown",
              "tab:pink", "tab:gray"]  # 막대 컬러
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
    c=[]
    q=[]
    s=[]

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

    print(len(c), len(q), len(s))

    x = np.arange(3)  # x값 개수
    Pc = ["C", "Q", "S"]  # x값
    values = [c.count(1) / len(c) * 100, q.count(1) / len(q) * 100,
              s.count(1) / len(s) * 100]

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

    print(len(par0), len(par1), len(par2),len(par3),len(par4), len(par5), len(par6))

    x = np.arange(7)  # x값 개수
    Pc = ["0","1","2","3","4","5","6"]  # x값
    values = [par0.count(1) / len(par0) * 100, par1.count(1) / len(par1) * 100,
              par2.count(1) / len(par2) * 100, par3.count(1) / len(par3) * 100, par4.count(1) / len(par4) * 100,
              par5.count(1) / len(par5) * 100, par6.count(1) / len(par6) * 100]

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
    #(max(ffn1)) #최댓값 93.5

    f0_10=[]
    f11_20=[]
    f21_30=[]
    f31_40=[]
    f41_50=[]
    f51_60=[]
    f61_70=[]
    f71_80=[]
    f81_90=[]
    f91_100=[]

    fare_f=[]

    for i in ffn1:
        if i is not float:
            fare_f.append(float(i))

    for i in range(0,891):
        if 0 <= fare_f[i] <= 10:
            if ffn2[i] == "0":
                f0_10.append(0)
            else:
                f0_10.append(1)
        elif 11 <= fare_f[i] <= 20:
            if ffn2[i] == "0":
                f11_20.append(0)
            else:
                f11_20.append(1)
        elif 21 <= fare_f[i] <= 30:
            if ffn2[i] == "0":
                f21_30.append(0)
            else:
                f21_30.append(1)
        elif 31 <= fare_f[i] <= 40:
            if ffn2[i] == "0":
                f31_40.append(0)
            else:
                f31_40.append(1)
        elif 41 <= fare_f[i] <= 50:
            if ffn2[i] == "0":
                f41_50.append(0)
            else:
                f41_50.append(1)
        elif 51 <= fare_f[i] <= 60:
            if ffn2[i] == "0":
                f51_60.append(0)
            else:
                f51_60.append(1)
        elif 61 <=fare_f[i] <= 70:
            if ffn2[i] == "0":
                f61_70.append(0)
            else:
                f71_80.append(1)
        elif 71 <= fare_f[i] <= 80:
            if ffn2[i] == "0":
                f71_80.append(0)
            else:
                f71_80.append(1)
        elif 81 <= fare_f[i] <= 90:
            if ffn2[i] == "0":
                f81_90.append(0)
            else:
                f81_90.append(1)
        elif 91 <= fare_f[i] <= 100:
            if ffn2[i] == "0":
                f91_100.append(0)
            else:
                f91_100.append(1)

    print(len(f0_10), len(f11_20), len(f21_30), len(f31_40), len(f41_50), len(f51_60), len(f61_70),
          len(f71_80), len(f81_90), len(f91_100))

    x = np.arange(10)  # x값 개수
    Pc = ["0-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80","81-90","91-100"]  # x값
    values = [f0_10.count(1) / len(f0_10) * 100, f11_20.count(1) / len(f11_20) * 100,
              f21_30.count(1) / len(f21_30) * 100, f31_40.count(1) / len(f31_40) * 100, f41_50.count(1) / len(f41_50) * 100,
              f51_60.count(1) / len(f51_60) * 100, f61_70.count(1) / len(f61_70) * 100, f71_80.count(1) / len(f71_80) * 100,
              f81_90.count(1) / len(f81_90) * 100, f91_100.count(1) / len(f91_100) * 100]

    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown",
              "tab:pink", "tab:gray", "tab:olive", "tab:cyan"]  # 막대 컬러

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

def pclass_data(ppfn1,ppfn2):
    pclass_i=[]
    pc0=[]
    pc1=[]
    pc2=[]
    pc3=[]

    for i in ppfn1:
        if i is not int:
            pclass_i.append(int(i))

    for i in range(0,891):
        if pclass_i[i]==1:
            if ppfn2[i] == "0":
                pc1.append(0)
            else:
                pc1.append(1)
        elif pclass_i[i]==2:
            if ppfn2[i] == "0":
                pc2.append(0)
            else:
                pc2.append(1)
        elif pclass_i[i]==3:
            if ppfn2[i] == "0":
                pc3.append(0)
            else:
                pc3.append(1)
    print(len(pc1),len(pc2),len(pc3))

    x = np.arange(3)  # x값 개수
    Pc = ["1","2","3"]  # x값
    values = [pc1.count(1) / len(pc1) * 100,
              pc2.count(1) / len(pc2) * 100, pc3.count(1) / len(pc3) * 100]

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
    sib0=[]
    sib1=[]
    sib2=[]
    sib3=[]
    sib4=[]
    sib5=[]
    sib6=[]
    sib7=[]
    sib8=[]

    sibsp_i=[]
    for i in ssfn1:
        if i is not int:
            sibsp_i.append(int(i))

    for i in range(0,891):
        if sibsp_i[i] == 0:
            if ssfn2[i] == "0":
                sib0.append(0)
            else:
                sib0.append(1)
        elif sibsp_i[i] == 1:
            if ssfn2[i] == "0":
                sib1.append(0)
            else:
                sib1.append(1)
        elif sibsp_i[i] == 2:
            if ssfn2[i] == "0":
                sib2.append(0)
            else:
                sib2.append(1)
        elif sibsp_i[i] == 3:
            if ssfn2[i] == "0":
                sib3.append(0)
            else:
                sib3.append(1)
        elif sibsp_i[i] == 4:
            if ssfn2[i] == "0":
                sib4.append(0)
            else:
                sib4.append(1)
        elif sibsp_i[i] == 5:
            if ssfn2[i] == "0":
                sib5.append(0)
            else:
                sib5.append(1)
        elif sibsp_i[i] == 6:
            if ssfn2[i] == "0":
                sib6.append(0)
            else:
                sib6.append(1)
        elif sibsp_i[i] == 7:
            if ssfn2[i] == "0":
                sib7.append(0)
            else:
                sib7.append(1)
        elif sibsp_i[i] == 8:
            if ssfn2[i] == "0":
                sib8.append(0)
            else:
                sib8.append(1)
    x = np.arange(9)  # x값 개수
    Pc = ["0","1","2","3","4","5","6","7","8"]  # x값
    values = [sib0.count(1) / len(sib0) * 100, sib1.count(1) / len(sib1) * 100, sib2.count(1) / len(sib2) * 100,
              sib3.count(1) / len(sib3) * 100, sib4.count(1) / len(sib4) * 100, sib5.count(1) / len(sib5) * 100,
              0.0, 0.0, sib8.count(1) / len(sib8) * 100]
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown",
              "tab:pink", "tab:gray", "tab:olive"]  # 막대 컬러
    for i in range(len(Pc)):
        plt.bar(x, values, color=colors[i], label=Pc[i])  # 데이터 값, 막대 컬러 적용
    plt.xticks(x, Pc)  # x를 순서대로 나열
    plt.title("Survival rate by Sibsp")  # 차트 제목
    plt.xlabel("sibsp")  # x축 레이블
    plt.ylabel("values")  # y축 레이블

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
    d1=csv_connect1("Cabin.csv")
    d2=csv_connect2()
    Cabin_data(d1,d2) #cabin 데이터
    #age_data(d1,d2) #age 데이터
    #embarked_data(d1,d2) #embarked 데이터
    #parch_data(d1,d2) #parch 데이터
    #fare_data(d1,d2) #fare 데이터
    #pclass_data(d1,d2) #pclass 데이터
    #sex_data(d1,d2) #sex 데이터
    #sibsp_data(d1,d2) #sibsp 데이터
