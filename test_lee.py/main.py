import csv

def read_csv():
    o=open("../test.csv","r",encoding="utf-8")
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

def save_csv(data2):
    name = {"0": "PassengerId", "1": "Pclass", "2": "Name", "3": "Sex", "4": "Age", "5": "SibSp", "6": "Parch"
            ,"7":"Ticket", "8": "Fare", "9": "Cabin", "10": "Embarked"}
    for n in range(0,11):
        with open(name[str(n)]+".csv", "w",newline="") as f:
            writer = csv.writer(f)

            writer.writerow(([name[str(n)]]))

            for i in range(0,418):
                     writer.writerows([[data2[n][i]]])

            f.close()

if __name__ == "__main__":
    rap = read_csv()
    rap2 = parsing(rap)
    save_csv(rap2)