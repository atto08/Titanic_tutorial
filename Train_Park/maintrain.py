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

    x = range(0,6)
    val = [len(s1),len(d1),len(s2),len(d2),len(s3),len(d3)]
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

def draw_suvage(csv_n):
    o = open(csv_n, 'r', encoding='utf-8')
    rd = csv.reader(o)
    ret = []
    survive = []
    dead = []
    s_none = []
    s_child = []
    s_age10s = []
    s_age20s = []
    s_age30s = []
    s_age40s = []
    s_age50s = []
    s_age60s = []
    s_age70s = []
    s_age80s = []
    d_none = []
    d_child = []
    d_age10s = []
    d_age20s = []
    d_age30s = []
    d_age40s = []
    d_age50s = []
    d_age60s = []
    d_age70s = []
    d_age80s = []

    for i in rd:
        ret.append(i)
    r_ret = ret[1:]
    for j in r_ret:
        if j[0] == '0':
            dead.append(j[1])
        else:
            survive.append(j[1])
    f_survive = IsFloatType(survive)
    f_dead = IsFloatType(dead)

    for k in f_survive:
        if k == -1:
            s_none.append(k)
        elif 0 <= k < 10:
            s_child.append(k)
        elif 10 <= k < 20:
            s_age10s.append(k)
        elif 20 <= k < 30:
            s_age20s.append(k)
        elif 30 <= k < 40:
            s_age30s.append(k)
        elif 40 <= k < 50:
            s_age40s.append(k)
        elif 50 <= k < 60:
            s_age50s.append(k)
        elif 60 <= k < 70:
            s_age60s.append(k)
        elif 70 <= k < 80:
            s_age70s.append(k)
        else:
            s_age80s.append(k)

    for l in f_dead:
        if l == -1:
            d_none.append(l)
        elif 0 <= l < 10:
            d_child.append(l)
        elif 10 <= l < 20:
            d_age10s.append(l)
        elif 20 <= l < 30:
            d_age20s.append(l)
        elif 30 <= l < 40:
            d_age30s.append(l)
        elif 40 <= l < 50:
            d_age40s.append(l)
        elif 50 <= l < 60:
            d_age50s.append(l)
        elif 60 <= l < 70:
            d_age60s.append(l)
        elif 70 <= l < 80:
            d_age70s.append(l)
        else:
            d_age80s.append(l)

    x = range(0,20)
    val = [len(s_none),len(s_child),len(s_age10s),len(s_age20s),len(s_age30s),len(s_age40s),len(s_age50s),len(s_age60s),len(s_age70s),len(s_age80s),
           len(d_none),len(d_child),len(d_age10s),len(d_age20s),len(d_age30s),len(d_age40s),len(d_age50s),len(d_age60s),len(d_age70s),len(d_age80s)]
    kinds = ['N','C','10','20','30','40','50','60','70','80','N','C','10','20','30','40','50','60','70','80']
    colors = ['b','b','b','b','b','b','b','b','b','b','r','r','r','r','r','r','r','r','r','r']
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
        else:
            f_suv.append(3)

    for l in dead:
        if l[1] == '0':
            f_dead.append(0)
        elif l[1] == '1':
            f_dead.append(1)
        elif l[1] == '2':
            f_dead.append(2)
        else:
            f_dead.append(3)

    x = range(0,8)
    val = [f_suv.count(0),f_suv.count(1),f_suv.count(2),f_suv.count(3),f_dead.count(0),f_dead.count(1),f_dead.count(2),f_dead.count(3)]
    kinds = ['0','1','2','Over 3','0','1','2','Over 3']
    colors = ['b','b','b','b','r','r','r','r']
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
        else:
            f_suv.append(3)

    for l in dead:
        if l[1] == '0':
            f_dead.append(0)
        elif l[1] == '1':
            f_dead.append(1)
        elif l[1] == '2':
            f_dead.append(2)
        else:
            f_dead.append(3)

    x = range(0,8)
    val = [f_suv.count(0),f_suv.count(1),f_suv.count(2),f_suv.count(3),f_dead.count(0),f_dead.count(1),f_dead.count(2),f_dead.count(3)]
    kinds = ['0','1','2','Over 3','0','1','2','Over 3']
    colors = ['b','b','b','b','r','r','r','r']
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

    x = range(0,10)
    val = [len(s0),len(s10),len(s20),len(s30),len(s_over40),len(d0),len(d10),len(d20),len(d30),len(d_over40)]
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
    s_a = []
    s_b = []
    s_c = []
    s_d = []
    s_e = []
    s_f = []
    s_g = []
    s_n = []
    d_a = []
    d_b = []
    d_c = []
    d_d = []
    d_e = []
    d_f = []
    d_g = []
    d_n = []

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
            s_a.append(k)
        elif k[:1] == 'B':
            s_b.append(k)
        elif k[:1] == 'C':
            s_c.append(k)
        elif k[:1] == 'D':
            s_d.append(k)
        elif k[:1] == 'E':
            s_e.append(k)
        elif k[:1] == 'F':
            s_f.append(k)
        elif k[:1] == 'G':
            s_g.append(k)
        else:
            s_n.append(-1)

    for l in dead:
        if l[:1] == 'A':
            d_a.append(l)
        elif l[:1] == 'B':
            d_b.append(l)
        elif l[:1] == 'C':
            d_c.append(l)
        elif l[:1] == 'D':
            d_d.append(l)
        elif l[:1] == 'E':
            d_e.append(l)
        elif l[:1] == 'F':
            d_f.append(l)
        elif l[:1] == 'G':
            d_g.append(l)
        else:
            d_n.append(-1)

    x = range(0,16)
    val = [len(s_a),len(s_b),len(s_c),len(s_d),len(s_e),len(s_f),len(s_g),len(s_n),len(d_a),len(d_b),len(d_c),len(d_d),len(d_e),len(d_f),len(d_g),len(d_n)]
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

    x = range(0,6)
    val = [len(s_c),len(d_c),len(s_q),len(d_q),len(s_s),len(d_s)]
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

if __name__ == "__main__":
    readd = read_csv()
    pars = parsing(readd)
    # save_csv(pars)
    # u_save_csv(pars,'sEmbarked.csv',0,10)
    # # draw_graph('Age.csv','Pclass.csv')
    # draw_suvpc('suvpc.csv')
    # draw_suvsx('suvsx.csv')
    draw_suvage('sAge.csv')
    # draw_suvsib('suvsib.csv')
    # draw_suvpar('suvpar.csv')
    # draw_suvfare('suvfare.csv')
    # draw_suvcab('suvcab.csv')
    # draw_suvem('suvemb.csv')
