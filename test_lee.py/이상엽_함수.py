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
        for j in range(0,417):
            file2[i].append(file1[j][i])
    for k in file2:
        print(k)





if __name__ == "__main__":
    read_csv()
    rap = read_csv()
    parsing(rap)

    #TODO: 하루에 한번 PC종료전 git에 반드시 commit 할것