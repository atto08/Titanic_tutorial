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
    with open(csv_name, "w", newline="") as f:
        writer = csv.writer(f)
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
#그래프 그리기 시작.
def draw_pclass(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)
    ret = []
    pcl = []
    for i in rd:
        ret.append(i)
    for j in ret:
        if j == ['0', '1']:
            pcl.append(-1)
        elif j == ['0', '2']:
            pcl.append(-2)
        elif j == ['0', '3']:
            pcl.append(-3)
        elif j == ['1', '1']:
            pcl.append(1)
        elif j == ['1', '2']:
            pcl.append(2)
        else:
            pcl.append(3)
    x = range(0,6)
    val = [pcl.count(1),pcl.count(-1),pcl.count(2),pcl.count(-2),pcl.count(3),pcl.count(-3)]
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

def draw_sex(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)
    ret = []
    c_sex = []
    for i in rd:
        ret.append(i)
    for j in ret:
        if j == ['0', 'male']:
            c_sex.append(1)
        elif j == ['0', 'female']:
            c_sex.append(2)
        elif j == ['1', 'male']:
            c_sex.append(3)
        else:
            c_sex.append(4)
    x = range(0,4)
    val = [c_sex.count(3),c_sex.count(1),c_sex.count(4),c_sex.count(2)]
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

def draw_age(csv_n):
    o = open(csv_n, 'r', encoding='utf-8')
    rd = csv.reader(o)
    ret = []
    survive = []
    dead = []
    s_age = []
    d_age = []
    for i in rd:
        ret.append(i)
    for j in ret:
        if j[0] == '0':
            dead.append(j[1])
        else:
            survive.append(j[1])
    f_survive = IsFloatType(survive)
    f_dead = IsFloatType(dead)
    for k in f_survive:
        if k == -1:
            s_age.append(k)
        elif 0 <= k < 10:
            s_age.append(0)
        elif 10 <= k < 20:
            s_age.append(1)
        elif 20 <= k < 30:
            s_age.append(2)
        elif 30 <= k < 40:
            s_age.append(3)
        elif 40 <= k < 50:
            s_age.append(4)
        elif 50 <= k < 60:
            s_age.append(5)
        elif 60 <= k < 70:
            s_age.append(6)
        elif 70 <= k < 80:
            s_age.append(7)
        else:
            s_age.append(8)
    for l in f_dead:
        if l == -1:
            d_age.append(l)
        elif 0 <= l < 10:
            d_age.append(0)
        elif 10 <= l < 20:
            d_age.append(1)
        elif 20 <= l < 30:
            d_age.append(2)
        elif 30 <= l < 40:
            d_age.append(3)
        elif 40 <= l < 50:
            d_age.append(4)
        elif 50 <= l < 60:
            d_age.append(5)
        elif 60 <= l < 70:
            d_age.append(6)
        elif 70 <= l < 80:
            d_age.append(7)
        else:
            d_age.append(8)
    x = range(0,20)
    val = [s_age.count(-1),s_age.count(0),s_age.count(1),s_age.count(2),s_age.count(3),s_age.count(4),s_age.count(5),s_age.count(6),s_age.count(7),s_age.count(8),
           d_age.count(-1),d_age.count(0),d_age.count(1),d_age.count(2),d_age.count(3),d_age.count(4),d_age.count(5),d_age.count(6),d_age.count(7),d_age.count(8)]
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

def draw_sibsp(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)
    ret = []
    survive = []
    dead = []
    f_suv = []
    f_dead = []
    for i in rd:
        ret.append(i)
    for j in ret:
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
    val = [f_suv.count(0),f_suv.count(1),f_suv.count(2),f_suv.count(3),
           f_dead.count(0),f_dead.count(1),f_dead.count(2),f_dead.count(3)]
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

def draw_parch(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)
    ret = []
    survive = []
    dead = []
    f_suv = []
    f_dead = []
    for i in rd:
        ret.append(i)
    for j in ret:
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
    val = [f_suv.count(0),f_suv.count(1),f_suv.count(2),f_suv.count(3),
           f_dead.count(0),f_dead.count(1),f_dead.count(2),f_dead.count(3)]
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

def draw_fare(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)
    ret = []
    survive = []
    dead = []
    s_fare = []
    d_fare = []
    for i in rd:
        ret.append(i)
    for j in ret:
        if j[0] == '0':
            dead.append(j[1])
        else:
            survive.append(j[1])
    f_suv = IsFloatType(survive)
    f_dead = IsFloatType(dead)
    for k in f_suv:
        if 0 <= k <= 10:
            s_fare.append(0)
        elif 10 < k <= 20:
            s_fare.append(1)
        elif 20 < k <= 30:
            s_fare.append(2)
        elif 30 < k <= 40:
            s_fare.append(3)
        else:
            s_fare.append(4)
    for l in f_dead:
        if 0 <= l <= 10:
            d_fare.append(0)
        elif 10 < l <= 20:
            d_fare.append(1)
        elif 20 < l <= 30:
            d_fare.append(2)
        elif 30 < l <= 40:
            d_fare.append(3)
        else:
            d_fare.append(4)
    x = range(0,10)
    val = [s_fare.count(0),s_fare.count(1),s_fare.count(2),s_fare.count(3),s_fare.count(4)
        ,d_fare.count(0),d_fare.count(1),d_fare.count(2),d_fare.count(3),d_fare.count(4)]
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

def draw_cabin(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)
    ret = []
    survive = []
    dead = []
    s_cab = []
    d_cab = []

    for i in rd:
        ret.append(i)
    for j in ret:
        if j[0] == '0':
            dead.append(j[1])
        else:
            survive.append(j[1])
    for k in survive:
        if k[:1] == 'A':
            s_cab.append(1)
        elif k[:1] == 'B':
            s_cab.append(2)
        elif k[:1] == 'C':
            s_cab.append(3)
        elif k[:1] == 'D':
            s_cab.append(4)
        elif k[:1] == 'E':
            s_cab.append(5)
        elif k[:1] == 'F':
            s_cab.append(6)
        elif k[:1] == 'G':
            s_cab.append(7)
        else:
            s_cab.append(-1)
    for l in dead:
        if l[:1] == 'A':
            d_cab.append(1)
        elif l[:1] == 'B':
            d_cab.append(2)
        elif l[:1] == 'C':
            d_cab.append(3)
        elif l[:1] == 'D':
            d_cab.append(4)
        elif l[:1] == 'E':
            d_cab.append(5)
        elif l[:1] == 'F':
            d_cab.append(6)
        elif l[:1] == 'G':
            d_cab.append(7)
        else:
            d_cab.append(-1)
    x = range(0,16)
    val = [s_cab.count(1),s_cab.count(2),s_cab.count(3),s_cab.count(4),s_cab.count(5),s_cab.count(6),s_cab.count(7),s_cab.count(-1)
        ,d_cab.count(1),d_cab.count(2),d_cab.count(3),d_cab.count(4),d_cab.count(5),d_cab.count(6),d_cab.count(7),d_cab.count(-1)]
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

def draw_embarked(csv_n):
    o = open(csv_n,'r',encoding='utf-8')
    rd = csv.reader(o)
    ret = []
    emb = []
    for i in rd:
        ret.append(i)
    for j in ret:
        if j == ['0', 'C']:
            emb.append(-1)
        elif j == ['0', 'Q']:
            emb.append(-2)
        elif j == ['0', 'S']:
            emb.append(-3)
        elif j == ['1', 'C']:
            emb.append(1)
        elif j == ['1', 'Q']:
            emb.append(2)
        else:
            emb.append(3)
    x = range(0,6)
    val = [emb.count(1),emb.count(-1),emb.count(2),emb.count(-2),emb.count(3),emb.count(-3)]
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
    draw_pclass('sPclass.csv')
    draw_sex('sSex.csv')
    draw_age('sAge.csv')
    draw_sibsp('sSibsp.csv')
    draw_parch('sParch.csv')
    draw_fare('sFare.csv')
    draw_cabin('sCabin.csv')
    draw_embarked('sEmbarked.csv')