import csv
import matplotlib.pyplot as plt
'''얘를 전역변수로 선언하지않으면 parsing함수에서 rd를 못받음.'''
'''왜????????????????????'''
o = open('test.csv', 'r', encoding="utf-8")
rd = csv.reader(o)
#컬럼 별 전역변수 리스트 생성
passengerid = []
pclass = []
name = []
sex = []
age = []
sibsp = []
parch = []
ticket = []
fare = []
cabin = []
embarked = []

# for list in rd:
#     passengerid.append(list[0])
#     pclass.append(list[1])
#     name.append(list[2])
#     sex.append(list[3])
#     age.append(list[4])
#     sibsp.append(list[5])
#     parch.append(list[6])
#     ticket.append(list[7])
#     fare.append(list[8])
#     cabin.append(list[9])
#     embarked.append(list[10])
# print(passengerid[1:])



# for i in range(1,len(age)):
#     age1 = age[i]
#     print(age1)

# data = ()
#
# fig, simple_chart = plt.subplots()
#
# simple_chart.plot(data)
# plt.show()

# # data = list(rd)
# # print(data)

def read_csv(): #CSV읽는 함수
    o = open('test.csv', 'r', encoding="utf-8")
    rd = csv.reader(o)

    for list in rd:
        passengerid.append(list[0])
        pclass.append(list[1])
        name.append(list[2])
        sex.append(list[3])
        age.append(list[4])
        sibsp.append(list[5])
        parch.append(list[6])
        ticket.append(list[7])
        fare.append(list[8])
        cabin.append(list[9])
        embarked.append(list[10])

    return rd

read_csv()
passengerid = passengerid[1:]
pclass = pclass[1:]
name = name[1:]
sex = sex[1:]
age = age[1:]
sibsp = sibsp[1:]
parch = parch[1:]
ticket = ticket[1:]
fare = fare[1:]
cabin = cabin[1:]
embarked = embarked[1:]
print(passengerid)


def parsing(data):
    read_csv()
    data = list(rd)
    print(data)


# def write():
#     f = open('test.csv', 'w', encoding='utf-8', newline='')
#     wt = csv.writer(f)
#     wt.writerows([i])
#     print()

# labels = ['PassengerId','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
# print(labels[0])
# for line in rd:
