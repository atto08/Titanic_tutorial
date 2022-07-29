import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_csv(csv_name):
    o=open(csv_name,"r",encoding="utf-8")
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

#매개변수 (test.csv를 파싱한 p_data, 저장할csv파일 이름 csv_name, 경우의 수 ? 숫자 n)
def save_csv(p_data,csv_name,n):
    labels = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    with open(csv_name, "w", newline="") as f:
        writer = csv.writer(f)
        if n == 0:
            writer.writerow(labels[0:1])
        elif n == 1:
            writer.writerow(labels[n:n+1])
        elif n == 2:
            writer.writerow(labels[n:n+1])
        elif n == 3:
            writer.writerow(labels[n:n+1])
        elif n == 4:
            writer.writerow(labels[n:n+1])
        elif n == 5:
            writer.writerow(labels[n:n+1])
        elif n == 6:
            writer.writerow(labels[n:n+1])
        elif n == 7:
            writer.writerow(labels[n:n+1])
        elif n == 8:
            writer.writerow(labels[n:n+1])
        elif n == 9:
            writer.writerow(labels[n:n+1])
        elif n == 10:
            writer.writerow(labels[n:])
        for i in range(0,418):
            writer.writerows([[p_data[n][i]]])
        f.close()


def IsFloatType(params=[]):
    ret = []
    for param in params:
        if param == '':
            ret.append(-1)
        # if you want replace "None" -> -1 used this conditional sentence
        else:
            ret.append(float(param))
    return ret


def draw_gp_pclass(filename):
    o = open(filename, "r", encoding="utf-8")
    rd = csv.reader(o)
    tot = []
    tot2 = []
    for i in rd:
        tot.append(i)
    for j in tot:
        tot2.append(j[0])

    upper = tot2.count('1')
    middle = tot2.count('2')
    lower = tot2.count('3')

    x = np.arange(3)
    val = [upper,middle,lower]
    kinds = ['1st','2nd','3rd']
    colors = ['b','g','yellow']

    plt.bar(x,val,color=colors,width=0.3)
    plt.xticks(x,kinds)
    plt.title("Rate of Class")
    plt.show()


def draw_gp_sex(filename):
    o = open(filename, "r", encoding="utf-8")
    rd = csv.reader(o)
    tot = []
    tot2 = []
    for i in rd:
        tot.append(i)
    for j in tot:
        tot2.append(j[0])

    men = tot2.count('male')
    women = tot2.count('female')

    x = np.arange(2)
    val = [men,women]
    kinds = ['male','female']
    colors = ['b','r']

    plt.bar(x,val,color=colors,width=0.3)
    plt.xticks(x,kinds)
    plt.title("Rate of Sex")
    plt.show()

    # Todo: check variable data type
    # params mean row lists
    # ex) [0,None,,1,2,3.1] --> [0,-1,-1,1,2,-1]
    def IsIntType(params=[]):
        ret = []
        for param in params:
            if param is int:
                ret.append(param)
            # if you want replace "None" -> -1 used this conditional sentence
            else:
                ret.append(-1)
        return ret


def draw_gp_age(filename,filename2):
    o = open(filename, "r", encoding="utf-8")
    p = open(filename2, "r", encoding="utf-8")
    rd = csv.reader(o)
    rd2 = csv.reader(p)
    tot = []
    tot2 = []
    for i in rd:
        tot.append(i)
    for j in tot:
        tot2.append(j[0])
    tot3 = tot2[1:]
    age_f = IsFloatType(tot3)

    pot = []
    pot2 = []
    for p in rd2:
        pot.append(p)
    for q in pot:
        pot2.append(q[0])
    pot3 = pot2[1:]
    fare_f = IsFloatType(pot3)

    plt.xlabel("Age")
    plt.ylabel("Fare")
    plt.scatter(age_f,fare_f,s=500,c='r',alpha=0.5)
    plt.show()



    # for i in tot3:
    #     if 0 < i <= 10:
    #         age0.append(i)
    #     elif 10 < i <= 20:
    #         age10.append(i)
    #     elif 20 < i <= 30:
    #         age20.append(i)
    #     elif 30 < i <= 40:
    #         age30.append(i)
    #     elif 40 < i <= 50:
    #         age40.append(i)
    #     elif 50 < i <= 60:
    #         age50.append(i)
    #     elif 60 < i <= 70:
    #         age60.append(i)
    #     elif 70 < i <= 80:
    #         age70.append(i)
    #     else:
    #         agen.append("None")
    # print(age0)




# def draw_graph(filename,num):
#     o = open(filename, "r", encoding="utf-8")
#     rd = csv.reader(o)
#     tot = []
#     tot2 = []
#     for i in rd:
#         tot.append(i)
#     for j in tot:
#         tot2.append(j[0])
#
#     var1 = tot2.count('male')
#     var2 = tot2.count('female')
#     var3 = tot2.count('')
#
#     x = np.arange(num)
#     val = [var1,var2]
#     kinds = ['male','female']
#     colors = ['b','r']
#
#     plt.bar(x,val,color=colors,width=0.3)
#     plt.xticks(x,kinds)
#     plt.title("Rate of Sex")
#     plt.show()


if __name__ == "__main__":
    rap = read_csv('test.csv')
    rap2 = parsing(rap)
    # save_csv(rap2,"fare.csv",8)
    # draw_gp_pclass("pclass.csv")
    draw_gp_age("age.csv","fare.csv")

