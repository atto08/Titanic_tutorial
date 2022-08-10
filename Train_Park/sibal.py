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
    file1 = []
    file2 = [[],[],[],[],[],[],[],[],[],[],[]]
    for line in data:
        file1.append(line)
    for i in range(0,11):
        for j in range(0,892):
            file2[i].append(file1[j][i])
    return file2


def save_csv(data2):
    name = {"0": "Survived", "1": "Pclass", "2": "Name", "3": "Sex", "4": "Age", "5": "SibSp", "6": "Parch"
            ,"7":"Ticket", "8": "Fare", "9": "Cabin", "10": "Embarked"}
    for n in range(0,11):
        with open(name[str(n)]+".csv", "w",newline="") as f:
            writer = csv.writer(f)

            for i in range(0,892):
                     writer.writerows([[data2[n][i]]])
            f.close()


def u_save_csv(p_data,csv_name,n,m):
    labels = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    with open(csv_name, "w", newline="") as f:
        writer = csv.writer(f)
        if n == 0:
            writer.writerow(labels[n:n+1])
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
        for i in range(1,892):
            writer.writerows([[p_data[n][i],p_data[m][i]]])
        f.close()


def IsFloatType(params=[]):
    ret = []
    for param in params:
        if param == '':
            ret.append(-1)
        else:
            ret.append(float(param))
    return ret


def IsIntType(params=[]):
    ret = []
    for param in params:
        if param == '':
            ret.append(-1)
        else:
            ret.append(int(param))
    print(ret)
    return ret


def StrToInt(params=[]):
    ret = []
    for param in params:
        if param == 'male':
            ret.append(0)
        else:
            ret.append(1)
    return ret


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


def draw_graph(csv1_n,csv2_n):
    o = open(csv1_n,'r',encoding='utf-8')
    o2 = open(csv2_n,'r',encoding='utf-8')
    rd = csv.reader(o)
    rd2 = csv.reader(o2)

    x_ret = []
    x_ret2 = []
    for i in rd:
        x_ret.append(i)
    for j in x_ret:
        x_ret2.append(j[0])
    s_x = x_ret2[1:]
    f_x = StrToInt(s_x)
    non_val_x = f_x.count(-1)

    y_ret = []
    y_ret2 = []
    for k in rd2:
        y_ret.append(k)
    for l in y_ret:
        y_ret2.append(l[0])
    s_y = y_ret2[1:]
    f_y = IsFloatType(s_y)
    non_val_y = f_y.count(-1)

    plt.title('Survivor/Death sex ratio')
    plt.xlabel('Sex')
    plt.ylabel('Survived')
    plt.scatter(f_x,f_y,500,'b',alpha=0.2)
    plt.show()
#객실등급 연결성 시작
# def draw_pcsx(csv_n):
#     o = open(csv_n,'r',encoding='utf-8')
#     rd = csv.reader(o)
#
#     ret = []
#     f_m = []
#     s_m = []
#     t_m = []
#     f_f = []
#     s_f = []
#     t_f = []
#     for i in rd:
#         ret.append(i)
#     r_ret = ret[1:]
#     for j in r_ret:
#         if j == ['1', 'male']:
#             f_m.append(-1)
#         elif j == ['2', 'male']:
#             s_m.append(-2)
#         elif j == ['3', 'male']:
#             t_m.append(-3)
#         elif j == ['1', 'female']:
#             f_f.append(1)
#         elif j == ['2', 'female']:
#             s_f.append(2)
#         else:
#             t_f.append(3)
#     m_1st = len(f_m)
#     m_2nd = len(s_m)
#     m_3rd = len(t_m)
#     f_1st = len(f_f)
#     f_2nd = len(s_f)
#     f_3rd = len(t_f)
#
#     x = range(0,6)
#     val = [m_1st,f_1st,m_2nd,f_2nd,m_3rd,f_3rd]
#     kinds = ['1st','1st','2nd','2nd','3rd','3rd']
#     colors = ['b','r','b','r','b','r']
#
#     plt.bar(x,val,color=colors)
#     plt.xticks(x,kinds)
#     plt.title("Pclass Sex ratio")
#     plt.ylabel('Count')
#     plt.show()
#
#
# def draw_pcages(csv1_n,csv2_n):
#     o = open(csv1_n,'r',encoding='utf-8')
#     o2 = open(csv2_n,'r',encoding='utf-8')
#     rd = csv.reader(o)
#     rd2 = csv.reader(o2)
#
#     x_ret = []
#     x_ret2 = []
#     for i in rd:
#         x_ret.append(i)
#     for j in x_ret:
#         x_ret2.append(j[0])
#     s_x = x_ret2[1:]
#     f_x = IsFloatType(s_x)
#     non_val_x = f_x.count(-1)
#
#     y_ret = []
#     y_ret2 = []
#     for k in rd2:
#         y_ret.append(k)
#     for l in y_ret:
#         y_ret2.append(l[0])
#     s_y = y_ret2[1:]
#     f_y = IsFloatType(s_y)
#     non_val_y = f_y.count(-1)
#
#     plt.title('Pclass sex ratio')
#     plt.xlabel('Ages')
#     plt.ylabel('Pclass')
#     plt.scatter(f_x,f_y,500,'b',alpha=0.2)
#     plt.show()
#
#
# def draw_pcage(afn1,afn2,v):
#     none=[]
#     age0s=[]
#     age10s=[]
#     age20s=[]
#     age30s=[]
#     age40s=[]
#     age50s=[]
#     age60s=[]
#     age70s=[]
#     age80s=[]
#     age90s=[]
#
#     for i in range(0,891):
#         if afn1[i]=="":
#             afn1[i]=-1
#
#     Age_int = []
#     for i in afn1:
#         if i is not float:
#             Age_int.append(float(i))
#     for i in range(0,891):
#         if 0 <= Age_int[i] < 10:
#             if afn2[i] == "1":
#                 age0s.append(1)
#             elif afn2[i] == "2":
#                 age0s.append(2)
#             else:
#                 age0s.append(3)
#         elif 10 <= Age_int[i] < 20:
#             if afn2[i] == "1":
#                 age10s.append(1)
#             elif afn2[i] == "2":
#                 age10s.append(2)
#             else:
#                 age10s.append(3)
#         elif 20 <= Age_int[i] < 30:
#             if afn2[i] == "1":
#                 age20s.append(1)
#             elif afn2[i] == "2":
#                 age20s.append(2)
#             else:
#                 age20s.append(3)
#         elif 30 <= Age_int[i] < 40:
#             if afn2[i] == "1":
#                 age30s.append(1)
#             elif afn2[i] == "2":
#                 age30s.append(2)
#             else:
#                 age30s.append(3)
#         elif 40 <= Age_int[i] < 50:
#             if afn2[i] == "1":
#                 age40s.append(1)
#             elif afn2[i] == "2":
#                 age40s.append(2)
#             else:
#                 age40s.append(3)
#         elif 50 <= Age_int[i] < 60:
#             if afn2[i] == "1":
#                 age50s.append(1)
#             elif afn2[i] == "2":
#                 age50s.append(2)
#             else:
#                 age50s.append(3)
#         elif 60 <= Age_int[i] < 70:
#             if afn2[i] == "1":
#                 age60s.append(1)
#             elif afn2[i] == "2":
#                 age60s.append(2)
#             else:
#                 age60s.append(3)
#         elif 70 <= Age_int[i] < 80:
#             if afn2[i] == "1":
#                 age70s.append(1)
#             elif afn2[i] == "2":
#                 age70s.append(2)
#             else:
#                 age70s.append(3)
#         elif 80 <= Age_int[i] < 90:
#             if afn2[i] == "1":
#                 age80s.append(1)
#             elif afn2[i] == "2":
#                 age80s.append(2)
#             else:
#                 age80s.append(3)
#         elif 90 <= Age_int[i] < 100:
#             if afn2[i] == "1":
#                 age90s.append(1)
#             elif afn2[i] == "2":
#                 age90s.append(2)
#             else:
#                 age90s.append(3)
#         else:
#             if afn2[i] == "1":
#                 none.append(1)
#             elif afn2[i] == "2":
#                 none.append(2)
#             else:
#                 none.append(3)
#
#     a_n = none.count(v)
#     a_0 = age0s.count(v)
#     a_10 = age10s.count(v)
#     a_20 = age20s.count(v)
#     a_30 = age30s.count(v)
#     a_40 = age40s.count(v)
#     a_50 = age50s.count(v)
#     a_60 = age60s.count(v)
#     a_70 = age70s.count(v)
#     a_80 = age80s.count(v)
#     a_90 = age90s.count(v)
#
#     x = range(0,11)
#     val = [a_n,a_0,a_10,a_20,a_30,a_40,a_50,a_60,a_70,a_80,a_90]
#     kinds = ['N','C','10','20','30','40','50','60','70','80','90']
#     colors = ['b','b','b','b','b','b','b','b','b','b','b']
#
#     plt.bar(x,val,color=colors)
#     plt.xticks(x,kinds)
#     plt.title("Pclass Ages ratio")
#     plt.xlabel('Ages')
#     plt.ylabel('Count')
#     plt.show()
#
#
# def draw_pcfare(afn1,afn2,v):
#     none=[]
#     age0s=[]
#     age10s=[]
#     age20s=[]
#     age30s=[]
#     age40s=[]
#     age50s=[]
#     age60s=[]
#     age70s=[]
#     age80s=[]
#     age90s=[]
#
#     for i in range(0,891):
#         if afn1[i]=="":
#             afn1[i]=-1
#
#     Age_int = []
#     for i in afn1:
#         if i is not float:
#             Age_int.append(float(i))
#     for i in range(0,891):
#         if 0 <= Age_int[i] < 10:
#             if afn2[i] == "1":
#                 age0s.append(1)
#             elif afn2[i] == "2":
#                 age0s.append(2)
#             else:
#                 age0s.append(3)
#         elif 10 <= Age_int[i] < 20:
#             if afn2[i] == "1":
#                 age10s.append(1)
#             elif afn2[i] == "2":
#                 age10s.append(2)
#             else:
#                 age10s.append(3)
#         elif 20 <= Age_int[i] < 30:
#             if afn2[i] == "1":
#                 age20s.append(1)
#             elif afn2[i] == "2":
#                 age20s.append(2)
#             else:
#                 age20s.append(3)
#         elif 30 <= Age_int[i] < 40:
#             if afn2[i] == "1":
#                 age30s.append(1)
#             elif afn2[i] == "2":
#                 age30s.append(2)
#             else:
#                 age30s.append(3)
#         elif 40 <= Age_int[i] < 50:
#             if afn2[i] == "1":
#                 age40s.append(1)
#             elif afn2[i] == "2":
#                 age40s.append(2)
#             else:
#                 age40s.append(3)
#         elif 50 <= Age_int[i] < 60:
#             if afn2[i] == "1":
#                 age50s.append(1)
#             elif afn2[i] == "2":
#                 age50s.append(2)
#             else:
#                 age50s.append(3)
#         elif 60 <= Age_int[i] < 70:
#             if afn2[i] == "1":
#                 age60s.append(1)
#             elif afn2[i] == "2":
#                 age60s.append(2)
#             else:
#                 age60s.append(3)
#         elif 70 <= Age_int[i] < 80:
#             if afn2[i] == "1":
#                 age70s.append(1)
#             elif afn2[i] == "2":
#                 age70s.append(2)
#             else:
#                 age70s.append(3)
#         elif 80 <= Age_int[i] < 90:
#             if afn2[i] == "1":
#                 age80s.append(1)
#             elif afn2[i] == "2":
#                 age80s.append(2)
#             else:
#                 age80s.append(3)
#         elif 90 <= Age_int[i] < 100:
#             if afn2[i] == "1":
#                 age90s.append(1)
#             elif afn2[i] == "2":
#                 age90s.append(2)
#             else:
#                 age90s.append(3)
#         else:
#             if afn2[i] == "1":
#                 none.append(1)
#             elif afn2[i] == "2":
#                 none.append(2)
#             else:
#                 none.append(3)
#
#     a_n = none.count(v)
#     a_0 = age0s.count(v)
#     a_10 = age10s.count(v)
#     a_20 = age20s.count(v)
#     a_30 = age30s.count(v)
#     a_40 = age40s.count(v)
#     a_50 = age50s.count(v)
#     a_60 = age60s.count(v)
#     a_70 = age70s.count(v)
#     a_80 = age80s.count(v)
#     a_90 = age90s.count(v)
#
#     x = range(0,11)
#     val = [a_n,a_0,a_10,a_20,a_30,a_40,a_50,a_60,a_70,a_80,a_90]
#     kinds = ['N','0','10','20','30','40','50','60','70','80','90']
#     colors = ['b','b','b','b','b','b','b','b','b','b','b']
#
#     plt.bar(x,val,color=colors)
#     bar = plt.bar(x,val,color=colors)
#
#     plt.xticks(x,kinds)
#     plt.title("Pclass Fare ratio")
#     plt.xlabel('Fare')
#     plt.ylabel('Count')
#     plt.legend()
#     plt.show()
#
# def draw_test(csv_n):
#     o = open(csv_n,'r',encoding='utf-8')
#     rd = csv.reader(o)
#
#     ret = []
#     f_m = []
#     s_m = []
#     t_m = []
#     f_f = []
#     s_f = []
#     t_f = []
#     for i in rd:
#         ret.append(i)
#     r_ret = ret[1:]
#     for j in r_ret:
#         if j == ['1', 'male']:
#             f_m.append(-1)
#         elif j == ['2', 'male']:
#             s_m.append(-2)
#         elif j == ['3', 'male']:
#             t_m.append(-3)
#         elif j == ['1', 'female']:
#             f_f.append(1)
#         elif j == ['2', 'female']:
#             s_f.append(2)
#         else:
#             t_f.append(3)
#     m_1st = len(f_m)
#     m_2nd = len(s_m)
#     m_3rd = len(t_m)
#     f_1st = len(f_f)
#     f_2nd = len(s_f)
#     f_3rd = len(t_f)
#
#     x = range(0,6)
#     val = [m_1st,f_1st,m_2nd,f_2nd,m_3rd,f_3rd]
#     kinds = ['1st','1st','2nd','2nd','3rd','3rd']
#     colors = ['b','r','b','r','b','r']
#
#     plt.bar(x,val,color=colors)
#     plt.xticks(x,kinds)
#     plt.title("Pclass Sex ratio")
#     plt.ylabel('Count')
#     plt.show()


if __name__ == "__main__":
    d1 = csv_connect1("Fare.csv")
    # d2 = csv_connect1("Pclass.csv")
    # draw_pcage(d1,d2,1)
    # draw_pcfare(d1,d2,3)