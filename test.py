import csv

def read_csv():
    o=open("test.csv","r",encoding="utf-8")
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

def save_csv(data2,csv_name,n):
    labels = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    with open(csv_name, "w", newline="") as f:
        writer = csv.writer(f)
        if n == 0:
            writer.writerow(labels[0:1])
        elif n== 1:
            writer.writerow(labels[1:2])
        elif n== 2:
            writer.writerow(labels[2:3])
        elif n== 3:
            writer.writerow(labels[3:4])
        elif n== 4:
            writer.writerow(labels[4:5])
        elif n== 5:
            writer.writerow(labels[5:6])
        elif n== 6:
            writer.writerow(labels[6:7])
        elif n== 7:
            writer.writerow(labels[7:8])
        elif n== 8:
            writer.writerow(labels[8:9])
        elif n== 9:
            writer.writerow(labels[9:10])
        elif n== 10:
            writer.writerow(labels[10:])
        for i in range(0,418):
            writer.writerows([[data2[n][i]]])

        f.close()


if __name__ == "__main__":
    rap = read_csv()
    rap2 = parsing(rap)
    save_csv(rap2,"embarked.csv",10)