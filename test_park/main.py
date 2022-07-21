import csv

def read_csv(ccc):
    o=open(ccc,"r",encoding="utf-8")
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
        elif n== 1:
            writer.writerow(labels[n:n+1])
        elif n== 2:
            writer.writerow(labels[n:n+1])
        elif n== 3:
            writer.writerow(labels[n:n+1])
        elif n== 4:
            writer.writerow(labels[n:n+1])
        elif n== 5:
            writer.writerow(labels[n:n+1])
        elif n== 6:
            writer.writerow(labels[n:n+1])
        elif n== 7:
            writer.writerow(labels[n:n+1])
        elif n== 8:
            writer.writerow(labels[n:n+1])
        elif n== 9:
            writer.writerow(labels[n:n+1])
        elif n== 10:
            writer.writerow(labels[n:])
        for i in range(0,418):
            writer.writerows([[p_data[n][i]]])

        f.close()


if __name__ == "__main__":
    rap = read_csv('test.csv')
    rap2 = parsing(rap)
    save_csv(rap2,"sex.csv",3)