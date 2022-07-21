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

    return file2

def save_csv(data2):

    with open("test2.csv", "w",newline="") as f:
        writer = csv.writer(f)

        writer.writerow((["pessenger ID"]))

        for i in range(0,417):
                writer.writerows([[data2[0][i]]])

        f.close()

if __name__ == "__main__":
    rap = read_csv()
    rap2 = parsing(rap)
    save_csv(rap2)