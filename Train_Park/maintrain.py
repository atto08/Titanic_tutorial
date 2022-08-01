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


def u_save_csv(p_data,csv_name,n):
    labels = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
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
        for i in range(1,892):
            writer.writerows([[p_data[n][i],p_data[n+10][i]]])
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


def draw_suvsx(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    zz = []
    zo = []
    oz = []
    oo = []
    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j == ['0', 'male']:
            zz.append(1)
        elif j == ['0', 'female']:
            zo.append(2)
        elif j == ['1', 'male']:
            oz.append(3)
        else:
            oo.append(4)
    d_men = len(zz)
    d_women = len(zo)
    s_men = len(oz)
    s_women = len(oo)

    x = np.arange(4)
    val = [d_men,s_men,d_women,s_women]
    kinds = ['Dead_M','Survive_M','Dead_W','Survive_W']
    colors = ['b','r','b','r']

    plt.bar(x,val,color=colors)
    plt.xticks(x,kinds)
    plt.title("Survived/Death sex ratio")
    plt.ylabel('Count')
    plt.show()


def draw_suvpc(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    d1 = []
    d2 = []
    d3 = []
    s1 = []
    s2 = []
    s3 = []
    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j == ['0', '1']:
            d1.append(-1)
        elif j == ['0', '2']:
            d2.append(-2)
        elif j == ['0', '3']:
            d3.append(-3)
        elif j == ['1', '1']:
            s1.append(1)
        elif j == ['1', '2']:
            s1.append(1)
        else:
            s3.append(3)
    d_first = len(d1)
    d_second = len(d2)
    d_third = len(d3)
    s_first = len(s1)
    s_second = len(s2)
    s_third = len(s3)
    print(d_first)
    print(d_second)
    print(d_third)
    print(s_first)
    print(s_second)
    print(s_third)


    x = np.arange(6)
    val = [d_first,s_first,d_second,s_second,d_third,s_third]
    kinds = ['D_1st','S_1st','D_2nd','S_2nd','D_3rd','S_3rd']
    colors = ['b','r','b','r','b','r']

    plt.bar(x,val,color=colors)
    plt.xticks(x,kinds)
    plt.title("Survived/Death pclass ratio")
    plt.ylabel('Count')
    plt.show()


def draw_test(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    d_c = []
    d_q = []
    d_s = []
    s_c = []
    s_q = []
    s_s = []
    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j == ['0', 'C']:
            d_c.append(-1)
        elif j == ['0', 'Q']:
            d_q.append(-2)
        elif j == ['0', 'S']:
            d_s.append(-3)
        elif j == ['1', 'C']:
            s_c.append(1)
        elif j == ['1', 'Q']:
            s_q.append(1)
        else:
            s_s.append(3)
    d_cherb = len(d_c)
    d_queen = len(d_q)
    d_south = len(d_s)
    s_cherb = len(s_c)
    s_queen = len(s_q)
    s_south = len(s_s)
    print(d_cherb)
    print(d_queen)
    print(d_south)
    print(s_cherb)
    print(s_queen)
    print(s_south)


    # x = np.arange(6)
    # val = [d_first,s_first,d_second,s_second,d_third,s_third]
    # kinds = ['D_1st','S_1st','D_2nd','S_2nd','D_3rd','S_3rd']
    # colors = ['b','r','b','r','b','r']
    #
    # plt.bar(x,val,color=colors)
    # plt.xticks(x,kinds)
    # plt.title("Survived/Death pclass ratio")
    # plt.ylabel('Count')
    # plt.show()

if __name__ == "__main__":
    readd = read_csv()
    pars = parsing(readd)
    # save_csv(pars)
    # u_save_csv(pars,'suvemb.csv',0)
    # draw_graph('Sex.csv','Survived.csv')
    # draw_suvsx('suvsx.csv')
    draw_test('suvemb.csv')