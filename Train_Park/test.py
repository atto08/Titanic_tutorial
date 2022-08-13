import csv
import matplotlib.pyplot as plt


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


#생존 연결성 시작
def draw_suvpc(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    s1 = []
    s2 = []
    s3 = []
    d1 = []
    d2 = []
    d3 = []
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
    d_1st = len(d1)
    d_2nd = len(d2)
    d_3rd = len(d3)
    s_1st = len(s1)
    s_2nd = len(s2)
    s_3rd = len(s3)

    x = range(0,6)
    val = [s_1st,d_1st,s_2nd,d_2nd,s_3rd,d_3rd]
    kinds = ['1st','1st','2nd','2nd','3rd','3rd']
    colors = ['b','r','b','r','b','r']
    ad = ['alive','dead']
    for i in range(len(ad)):
        plt.bar(x, val, color=colors[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survived/Death by Pclass",size=15)
    plt.xlabel('Pclass',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
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

    x = range(0,4)
    val = [s_men,d_men,s_women,d_women]
    kinds = ['Men','Men','Women','Women']
    colors = ['b','r','b','r']
    ad = ['alive', 'dead']
    for i in range(len(ad)):
        plt.bar(x, val, color=colors[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survived/Death by Sex",size=15)
    plt.xlabel('Gender',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()


def draw_suvage(afn1,afn2):
    none=[]
    age0s=[]
    age10s=[]
    age20s=[]
    age30s=[]
    age40s=[]
    age50s=[]
    age60s=[]
    age70s=[]
    age80s=[]
    age90s=[]

    for i in range(0,891):
        if afn1[i]=="":
            afn1[i]=-1

    Age_int = []
    for i in afn1:
        if i is not float:
            Age_int.append(float(i))

    for i in range(0,891):
        if 0 <= Age_int[i] < 10:
            if afn2[i] == "0":
                age0s.append(0)
            else:
                age0s.append(1)
        elif 10 <= Age_int[i] < 20:
            if afn2[i] == "0":
                age10s.append(0)
            else:
                age10s.append(1)
        elif 20 <= Age_int[i] < 30:
            if afn2[i] == "0":
                age20s.append(0)
            else:
                age20s.append(1)
        elif 30 <= Age_int[i] < 40:
            if afn2[i] == "0":
                age30s.append(0)
            else:
                age30s.append(1)
        elif 40 <= Age_int[i] < 50:
            if afn2[i] == "0":
                age40s.append(0)
            else:
                age40s.append(1)
        elif 50 <= Age_int[i] < 60:
            if afn2[i] == "0":
                age50s.append(0)
            else:
                age50s.append(1)
        elif 60 <= Age_int[i] < 70:
            if afn2[i] == "0":
                age60s.append(0)
            else:
                age60s.append(1)
        elif 70 <= Age_int[i] < 80:
            if afn2[i] == "0":
                age70s.append(0)
            else:
                age70s.append(1)
        elif 80 <= Age_int[i] < 90:
            if afn2[i] == "0":
                age80s.append(0)
            else:
                age80s.append(1)
        elif 90 <= Age_int[i] < 100:
            if afn2[i] == "0":
                age90s.append(0)
            else:
                age90s.append(1)
        else:
            if afn2[i] == "0":
                none.append(0)
            else:
                none.append(1)

    d_n = none.count(0)
    d_0 = age0s.count(0)
    d_10 = age10s.count(0)
    d_20 = age20s.count(0)
    d_30 = age30s.count(0)
    d_40 = age40s.count(0)
    d_50 = age50s.count(0)
    d_60 = age60s.count(0)
    d_70 = age70s.count(0)
    d_80 = age80s.count(0)
    d_90 = age90s.count(0)

    s_n = none.count(1)
    s_0 = age0s.count(1)
    s_10 = age10s.count(1)
    s_20 = age20s.count(1)
    s_30 = age30s.count(1)
    s_40 = age40s.count(1)
    s_50 = age50s.count(1)
    s_60 = age60s.count(1)
    s_70 = age70s.count(1)
    s_80 = age80s.count(1)
    s_90 = age90s.count(1)

    x = range(0,22)
    #[s_n,s_0,s_10,s_20,s_30,s_40,s_50,s_60,s_70,s_80,s_90]
    val = [s_n,s_0,s_10,s_20,s_30,s_40,s_50,s_60,s_70,s_80,s_90,d_n,d_0,d_10,d_20,d_30,d_40,d_50,d_60,d_70,d_80,d_90]
    #['n','0s','10s','20s','30s','40s','50s','60s','70s','80s','90s']
    kinds = ['N','C','10','20','30','40','50','60','70','80','90','N','C','10','20','30','40','50','60','70','80','90']
    colors = ['b','b','b','b','b','b','b','b','b','b','b','r','r','r','r','r','r','r','r','r','r','r']
    color2 = ['b','r']
    ad = ['alive', 'dead']
    for i in range(len(ad)):
        plt.bar(x, val, color=color2[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survived/Death by Ages",size=15)
    plt.xlabel('Ages',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()


def draw_suvsib(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    survive = []
    dead = []

    f_suv = []
    f_dead = []

    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j[0] == '0':
            dead.append(j)
        else:
            survive.append(j)

    for k in survive:
        if k[1] == '0':
            f_suv.append(0)
        elif k[1] == '1':
            f_suv.append(1)
        elif k[1] == '2':
            f_suv.append(2)
        elif k[1] == '3':
            f_suv.append(3)
        else:
            f_suv.append(-1)

    for l in dead:
        if l[1] == '0':
            f_dead.append(0)
        elif l[1] == '1':
            f_dead.append(1)
        elif l[1] == '2':
            f_dead.append(2)
        elif l[1] == '3':
            f_dead.append(3)
        else:
            f_dead.append(-1)

    suv0 = f_suv.count(0)
    suv1 = f_suv.count(1)
    suv2 = f_suv.count(2)
    suv3 = f_suv.count(3)
    suv_over4 = f_suv.count(-1)
    dead0 = f_dead.count(0)
    dead1 = f_dead.count(1)
    dead2 = f_dead.count(2)
    dead3 = f_dead.count(3)
    dead_over4 = f_dead.count(-1)

    x = range(0,10)
    val = [suv0,suv1,suv2,suv3,suv_over4,dead0,dead1,dead2,dead3,dead_over4]
    kinds = ['0','1','2','3','Over 4','0','1','2','3','Over 4']
    colors = ['b','b','b','b','b','r','r','r','r','r']
    color2 = ['b','r']
    ad = ['alive', 'dead']
    for i in range(len(ad)):
        plt.bar(x, val, color=color2[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survived/Death by SibSp",size=15)
    plt.xlabel('The number of SibSp',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()


def draw_suvpar(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    survive = []
    dead = []

    f_suv = []
    f_dead = []

    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j[0] == '0':
            dead.append(j)
        else:
            survive.append(j)

    for k in survive:
        if k[1] == '0':
            f_suv.append(0)
        elif k[1] == '1':
            f_suv.append(1)
        elif k[1] == '2':
            f_suv.append(2)
        elif k[1] == '3':
            f_suv.append(3)
        else:
            f_suv.append(-1)

    for l in dead:
        if l[1] == '0':
            f_dead.append(0)
        elif l[1] == '1':
            f_dead.append(1)
        elif l[1] == '2':
            f_dead.append(2)
        elif l[1] == '3':
            f_dead.append(3)
        else:
            f_dead.append(-1)

    suv0 = f_suv.count(0)
    suv1 = f_suv.count(1)
    suv2 = f_suv.count(2)
    suv3 = f_suv.count(3)
    suv_over4 = f_suv.count(-1)
    dead0 = f_dead.count(0)
    dead1 = f_dead.count(1)
    dead2 = f_dead.count(2)
    dead3 = f_dead.count(3)
    dead_over4 = f_dead.count(-1)

    x = range(0,10)
    val = [suv0,suv1,suv2,suv3,suv_over4,dead0,dead1,dead2,dead3,dead_over4]
    kinds = ['0','1','2','3','Over 4','0','1','2','3','Over 4']
    colors = ['b','b','b','b','b','r','r','r','r','r']
    color2 = ['b','r']
    ad = ['alive', 'dead']
    for i in range(len(ad)):
        plt.bar(x, val, color=color2[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survived/Death by Parch",size=15)
    plt.xlabel('The number of Parch',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()


def draw_suvfare(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    survive = []
    dead = []

    s0 = []
    s10 = []
    s20 = []
    s30 = []
    s_over40 = []
    d0 = []
    d10 = []
    d20 = []
    d30 = []
    d_over40 = []

    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j[0] == '0':
            dead.append(j[1])
        else:
            survive.append(j[1])

    f_suv = IsFloatType(survive)
    f_dead = IsFloatType(dead)

    for k in f_suv:
        if 0 <= k <= 10:
            s0.append(k)
        elif 10 < k <= 20:
            s10.append(k)
        elif 20 < k <= 30:
            s20.append(k)
        elif 30 < k <= 40:
            s30.append(k)
        else:
            s_over40.append(k)

    for l in f_dead:
        if 0 <= l <= 10:
            d0.append(l)
        elif 10 < l <= 20:
            d10.append(l)
        elif 20 < l <= 30:
            d20.append(l)
        elif 30 < l <= 40:
            d30.append(l)
        else:
            d_over40.append(l)

    s_u10 = len(s0)
    s_u20 = len(s10)
    s_u30 = len(s20)
    s_u40 = len(s30)
    s_o40 = len(s_over40)
    d_u10 = len(d0)
    d_u20 = len(d10)
    d_u30 = len(d20)
    d_u40 = len(d30)
    d_o40 = len(d_over40)


    x = range(0,10)
    val = [s_u10,s_u20,s_u30,s_u40,s_o40,d_u10,d_u20,d_u30,d_u40,d_o40]
    kinds = ['0~10','10~20','20~30','30~40','40↑','0~10','10~20','20~30','30~40','40↑']
    colors = ['b','b','b','b','b','r','r','r','r','r']
    color2 = ['b','r']
    ad = ['alive', 'dead']
    for i in range(len(ad)):
        plt.bar(x, val, color=color2[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survived/Death by Fare",size=15)
    plt.xlabel('Fare',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()


def draw_suvcab(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    survive = []
    dead = []

    s_ca = []
    s_cb = []
    s_cc = []
    s_cd = []
    s_ce = []
    s_cf = []
    s_cg = []
    s_none = []
    d_ca = []
    d_cb = []
    d_cc = []
    d_cd = []
    d_ce = []
    d_cf = []
    d_cg = []
    d_none = []

    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j[0] == '0':
            dead.append(j[1])
        else:
            survive.append(j[1])

    for k in survive:
        if k[:1] == 'A':
            s_ca.append(k)
        elif k[:1] == 'B':
            s_cb.append(k)
        elif k[:1] == 'C':
            s_cc.append(k)
        elif k[:1] == 'D':
            s_cd.append(k)
        elif k[:1] == 'E':
            s_ce.append(k)
        elif k[:1] == 'F':
            s_cf.append(k)
        elif k[:1] == 'G':
            s_cg.append(k)
        else:
            s_none.append(-1)

    for l in dead:
        if l[:1] == 'A':
            d_ca.append(l)
        elif l[:1] == 'B':
            d_cb.append(l)
        elif l[:1] == 'C':
            d_cc.append(l)
        elif l[:1] == 'D':
            d_cd.append(l)
        elif l[:1] == 'E':
            d_ce.append(l)
        elif l[:1] == 'F':
            d_cf.append(l)
        elif l[:1] == 'G':
            d_cg.append(l)
        else:
            d_none.append(-1)

    SA = len(s_ca)
    SB = len(s_cb)
    SC = len(s_cc)
    SD = len(s_cd)
    SE = len(s_ce)
    SF = len(s_cf)
    SG = len(s_cg)
    SN = len(s_none)
    DA = len(d_ca)
    DB = len(d_cb)
    DC = len(d_cc)
    DD = len(d_cd)
    DE = len(d_ce)
    DF = len(d_cf)
    DG = len(d_cg)
    DN = len(d_none)

    x = range(0,16)
    val = [SA,SB,SC,SD,SE,SF,SG,SN,DA,DB,DC,DD,DE,DF,DG,DN]
    kinds = ['A','B','C','D','E','F','G','None','A','B','C','D','E','F','G','None']
    colors = ['b','b','b','b','b','b','b','b','r','r','r','r','r','r','r','r']
    color2 = ['b','r']
    ad = ['alive', 'dead']
    for i in range(len(ad)):
        plt.bar(x, val, color=color2[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survived/Death by Cabin",size=15)
    plt.xlabel('Cabin',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()


def draw_suvem(csv_n):
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

    x = range(0,6)
    val = [s_cherb,d_cherb,s_queen,d_queen,s_south,d_south]
    kinds = ['<Cher','bourg>','<Queen','stown>','<South','ampton>']
    colors = ['b','r','b','r','b','r']
    ad = ['alive', 'dead']
    for i in range(len(ad)):
        plt.bar(x, val, color=colors[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survived/Death by Embarked",size=15)
    plt.xlabel('Embarked',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()


def dv_suvage(afn1,afn2):
    none=[]
    age0s=[]
    age10s=[]
    age20s=[]
    age30s=[]
    age40s=[]
    age50s=[]
    age60s=[]
    age70s=[]
    age80s=[]
    age90s=[]

    for i in range(0,891):
        if afn1[i]=="":
            afn1[i]=-1

    Age_int = []
    for i in afn1:
        if i is not float:
            Age_int.append(float(i))

    for i in range(0,891):
        if 0 <= Age_int[i] < 10:
            if afn2[i] == "0":
                age0s.append(0)
            else:
                age0s.append(1)
        elif 10 <= Age_int[i] < 20:
            if afn2[i] == "0":
                age10s.append(0)
            else:
                age10s.append(1)
        elif 20 <= Age_int[i] < 30:
            if afn2[i] == "0":
                age20s.append(0)
            else:
                age20s.append(1)
        elif 30 <= Age_int[i] < 40:
            if afn2[i] == "0":
                age30s.append(0)
            else:
                age30s.append(1)
        elif 40 <= Age_int[i] < 50:
            if afn2[i] == "0":
                age40s.append(0)
            else:
                age40s.append(1)
        elif 50 <= Age_int[i] < 60:
            if afn2[i] == "0":
                age50s.append(0)
            else:
                age50s.append(1)
        elif 60 <= Age_int[i] < 70:
            if afn2[i] == "0":
                age60s.append(0)
            else:
                age60s.append(1)
        elif 70 <= Age_int[i] < 80:
            if afn2[i] == "0":
                age70s.append(0)
            else:
                age70s.append(1)
        elif 80 <= Age_int[i] < 90:
            if afn2[i] == "0":
                age80s.append(0)
            else:
                age80s.append(1)
        elif 90 <= Age_int[i] < 100:
            if afn2[i] == "0":
                age90s.append(0)
            else:
                age90s.append(1)
        else:
            if afn2[i] == "0":
                none.append(0)
            else:
                none.append(1)

    d_n = none.count(0)
    d_0 = age0s.count(0)
    d_10 = age10s.count(0)
    d_20 = age20s.count(0)
    d_30 = age30s.count(0)
    d_40 = age40s.count(0)
    d_50 = age50s.count(0)
    d_60 = age60s.count(0)
    d_70 = age70s.count(0)
    d_80 = age80s.count(0)
    d_90 = age90s.count(0)

    s_n = none.count(1)
    s_0 = age0s.count(1)
    s_10 = age10s.count(1)
    s_20 = age20s.count(1)
    s_30 = age30s.count(1)
    s_40 = age40s.count(1)
    s_50 = age50s.count(1)
    s_60 = age60s.count(1)
    s_70 = age70s.count(1)
    s_80 = age80s.count(1)
    s_90 = age90s.count(1)

    x = range(0,11)
    #[s_n,s_0,s_10,s_20,s_30,s_40,s_50,s_60,s_70,s_80,s_90]
    val = [d_n,d_0,d_10,d_20,d_30,d_40,d_50,d_60,d_70,d_80,d_90]
    #['n','0s','10s','20s','30s','40s','50s','60s','70s','80s','90s']
    kinds = ['N','C','10','20','30','40','50','60','70','80','90']
    colors = ['brown','yellow','skyblue','blue','green','pink','red','purple','magenta','olive','orange']
    leg = ['None', 'Children','10~19','20~29','30~39','40~49','50~59','60~69','70~79','80~89','90~99']
    for i in range(len(kinds)):
        plt.bar(x, val, color=colors[i], label=leg[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Deaths by Age",size=15,color='r')
    plt.xlabel('Ages',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()


    x = range(0,11)
    val = [s_n,s_0,s_10,s_20,s_30,s_40,s_50,s_60,s_70,s_80,s_90]
    kinds = ['N','C','10','20','30','40','50','60','70','80','90']
    colors = ['brown','yellow','skyblue','blue','green','pink','red','purple','magenta','olive','orange']
    leg = ['None', 'Children','10~19','20~29','30~39','40~49','50~59','60~69','70~79','80~89','90~99']
    for i in range(len(kinds)):
        plt.bar(x, val, color=colors[i], label=leg[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survivers by Age",size=15,color='b')
    plt.xlabel('Ages',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()


def dv_suvfare(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    survive = []
    dead = []

    s0 = []
    s10 = []
    s20 = []
    s30 = []
    s_over40 = []
    d0 = []
    d10 = []
    d20 = []
    d30 = []
    d_over40 = []

    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j[0] == '0':
            dead.append(j[1])
        else:
            survive.append(j[1])

    f_suv = IsFloatType(survive)
    f_dead = IsFloatType(dead)

    for k in f_suv:
        if 0 <= k <= 10:
            s0.append(k)
        elif 10 < k <= 20:
            s10.append(k)
        elif 20 < k <= 30:
            s20.append(k)
        elif 30 < k <= 40:
            s30.append(k)
        else:
            s_over40.append(k)

    for l in f_dead:
        if 0 <= l <= 10:
            d0.append(l)
        elif 10 < l <= 20:
            d10.append(l)
        elif 20 < l <= 30:
            d20.append(l)
        elif 30 < l <= 40:
            d30.append(l)
        else:
            d_over40.append(l)

    s_u10 = len(s0)
    s_u20 = len(s10)
    s_u30 = len(s20)
    s_u40 = len(s30)
    s_o40 = len(s_over40)
    d_u10 = len(d0)
    d_u20 = len(d10)
    d_u30 = len(d20)
    d_u40 = len(d30)
    d_o40 = len(d_over40)


    x = range(0,5)
    #d_u10,d_u20,d_u30,d_u40,d_o40
    val = [s_u10,s_u20,s_u30,s_u40,s_o40]
    kinds = ['0~10','10~20','20~30','30~40','40↑']
    kind2 = ['0~10$','10~20$','20~30$','30~40$','Over 40$']
    colors = ['b','orange','yellow','green','brown']
    for i in range(len(val)):
        plt.bar(x, val, color=colors[i], label=kind2[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=11)
    plt.xticks(x,kinds)
    plt.title("The number of Survivers by Fare",size=15,color='b')
    plt.xlabel('Fare',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()

    x = range(0, 5)
    #
    val = [d_u10,d_u20,d_u30,d_u40,d_o40]
    kinds = ['0~10','10~20','20~30','30~40','40↑']
    kind2 = ['0~10$', '10~20$', '20~30$', '30~40$', 'Over 40$']
    colors = ['b','orange','yellow','green','brown']
    for i in range(len(val)):
        plt.bar(x, val, color=colors[i], label=kind2[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=11)
    plt.xticks(x, kinds)
    plt.title("The number of Deaths by Fare", size=15, color='r')
    plt.xlabel('Fare', size=12)
    plt.ylabel('Count', size=12)
    plt.legend()
    plt.show()



def dv_suvcab(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)

    ret = []
    survive = []
    dead = []

    s_ca = []
    s_cb = []
    s_cc = []
    s_cd = []
    s_ce = []
    s_cf = []
    s_cg = []
    s_none = []
    d_ca = []
    d_cb = []
    d_cc = []
    d_cd = []
    d_ce = []
    d_cf = []
    d_cg = []
    d_none = []

    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j[0] == '0':
            dead.append(j[1])
        else:
            survive.append(j[1])

    for k in survive:
        if k[:1] == 'A':
            s_ca.append(k)
        elif k[:1] == 'B':
            s_cb.append(k)
        elif k[:1] == 'C':
            s_cc.append(k)
        elif k[:1] == 'D':
            s_cd.append(k)
        elif k[:1] == 'E':
            s_ce.append(k)
        elif k[:1] == 'F':
            s_cf.append(k)
        elif k[:1] == 'G':
            s_cg.append(k)
        else:
            s_none.append(-1)

    for l in dead:
        if l[:1] == 'A':
            d_ca.append(l)
        elif l[:1] == 'B':
            d_cb.append(l)
        elif l[:1] == 'C':
            d_cc.append(l)
        elif l[:1] == 'D':
            d_cd.append(l)
        elif l[:1] == 'E':
            d_ce.append(l)
        elif l[:1] == 'F':
            d_cf.append(l)
        elif l[:1] == 'G':
            d_cg.append(l)
        else:
            d_none.append(-1)

    SA = len(s_ca)
    SB = len(s_cb)
    SC = len(s_cc)
    SD = len(s_cd)
    SE = len(s_ce)
    SF = len(s_cf)
    SG = len(s_cg)
    SN = len(s_none)
    DA = len(d_ca)
    DB = len(d_cb)
    DC = len(d_cc)
    DD = len(d_cd)
    DE = len(d_ce)
    DF = len(d_cf)
    DG = len(d_cg)
    DN = len(d_none)

    x = range(0,8)
    val = [SA,SB,SC,SD,SE,SF,SG,SN]
    kinds = ['A','B','C','D','E','F','G','None']
    colors = ['orange','yellow','magenta','blue','green','olive','purple','brown']
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=10)
    plt.xticks(x,kinds)
    plt.title("The number of Survivers by Cabin",size=15)
    plt.xlabel('Cabin',size=12)
    plt.ylabel('Count',size=12)
    plt.show()


def dv_suvem(csv_n):
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

    x = range(0,3)
    val = [s_cherb,s_queen,s_south]
    kinds = ['C','Q','S']
    colors = ['b','r','g']
    ad = ['Cherbourg','Queenstown','Southampton']
    for i in range(len(ad)):
        plt.bar(x, val, color=colors[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=11)
    plt.xticks(x,kinds)
    plt.title("The number of Survivers by Embarked",size=15,color='b')
    plt.xlabel('Embarked',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()

    x = range(0,3)
    val = [d_cherb,d_queen,d_south]
    kinds = ['C','Q','S']
    colors = ['b','r','g']
    ad = ['Cherbourg','Queenstown','Southampton']
    for i in range(len(ad)):
        plt.bar(x, val, color=colors[i], label=ad[i])
    bar = plt.bar(x, val, color=colors)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, height, ha="center", va="bottom", size=11)
    plt.xticks(x,kinds)
    plt.title("The number of Deaths by Embarked",size=15,color='r')
    plt.xlabel('Embarked',size=12)
    plt.ylabel('Count',size=12)
    plt.legend()
    plt.show()
#생존 연결성 끝


if __name__ == "__main__":
    readd = read_csv()
    pars = parsing(readd)
    # save_csv(pars)
    # u_save_csv(pars,'suvcab.csv',0,9)
    # # draw_graph('Age.csv','Pclass.csv')
    # draw_suvpc('suvpc.csv')
    # draw_suvsx('suvsx.csv')
    # d1 = csv_connect1("Age.csv")
    # d2 = csv_connect2()
    # draw_suvage(d1, d2)
    # dv_suvage(d1,d2)
    # draw_suvsib('suvsib.csv')
    # draw_suvpar('suvpar.csv')
    # draw_suvfare('suvfare.csv')
    # dv_suvfare('suvfare.csv')
    # draw_suvcab('suvcab.csv')
    dv_suvcab('sCabin.csv')
    # draw_suvem('suvemb.csv')
    # dv_suvem('suvemb.csv')
