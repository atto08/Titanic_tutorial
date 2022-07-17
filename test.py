import csv
import matplotlib.pyplot as plt
import numpy as np
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

#sex(성별) 그래프 //막대
man = sex.count('male')
women = sex.count('female')

x = np.arange(2)
values = [man,women]
kinds = ['male','female']
plt.bar(x,values,color='b')
plt.xticks(x,kinds)
plt.show()

# for i in range(len(passengerid)):
#     print(passengerid[i])




def parsing(data):
    read_csv()
    data = list(rd)
    print(data)


# def write():
#     f = open('test.csv', 'w', encoding='utf-8', newline='')
#     wt = csv.writer(f)
#     wt.writerows([i])
#     print()

