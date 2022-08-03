import csv

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
        for j in range(0,891):
            file2[i].append(file1[j][i])

    return file2


def save_csv(data2):
    name = {"0": "PassengerId", "1": "Survived", "2": "Pclass", "3": "Name", "4": "Sex", "5": "Age", "6": "SibSp",
            "7": "Parch", "8": "Ticket", "9": "Fare", "10": "Cabin", "11": "Embarked"}

    for n in range(0,12):
        with open(name[str(n)]+".csv", "w", newline="") as f:
            writer = csv.writer(f)

            for i in range(0,891):
                writer.writerows([[data2[n][i]]])

            f.close()



def data_zip(name):
    o = open(name + ".csv", "r", encoding="utf-8")
    rd = csv.reader(o)
    name = []
    for i in rd:
        for j in i:
            name.append(j)
    name.pop(0)

    return name

def Age_gr(label):
    Age_int = []
    for i in label:
        if i == "":
            label.append(-1)
        elif i is not float:
            Age_int.append(float(i))

    Age_group = [[], [], [], [], [], [], [], [], [], []]

    for j in Age_int:
        if j >= 0 and j < 10:
            Age_group[0].append(j)
        elif j >= 10 and j < 20:
            Age_group[1].append(j)
        elif j >= 20 and j < 30:
            Age_group[2].append(j)
        elif j >= 30 and j < 40:
            Age_group[3].append(j)
        elif j >= 40 and j < 50:
            Age_group[4].append(j)
        elif j >= 50 and j < 60:
            Age_group[5].append(j)
        elif j >= 60 and j < 70:
            Age_group[6].append(j)
        elif j >= 70 and j < 80:
            Age_group[7].append(j)
        elif j >= 80 and j < 90:
            Age_group[8].append(j)
        elif j >= 90 and j < 100:
            Age_group[9].append(j)

def Cabin_gr(suv,cab):
    suvived={"O": 1, "X": 0}
    cabtin=["A","B","C","D","E","F",""]

    for i in suv:
        for j in cab:
            if j[0]



if __name__ == "__main__":
    Age=data_zip("Age")
    Cabin=data_zip("Cabin")
    Embarked=data_zip("Embarked")
    Fare=data_zip("Fare")
    Name=data_zip("Name")
    Parcch=data_zip("Parch")
    Passenger=data_zip("PassengerId")
    Pclass=data_zip("Pclass")
    Sex=data_zip("Sex")
    Sibsp=data_zip("Sibsp")
    Survived=data_zip("Survived")
    Ticket=data_zip("Ticket")
    Age_gr(Age)