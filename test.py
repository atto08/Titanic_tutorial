import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import int64 , float64
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
    # rd = pd.read_csv("test.csv",
    #                  dtype={"PassengerId": int64, "Pclass": int64, "Name": object, "Sex": object, "Age": float64,"Sibsp": int64,
    #                         "Parch": int64, "Ticket": object, "Fare": float64, "Cabin": object, "Embarked": object})
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

# age = [float(i) for i in age]

def add_value_label(x_list,y_list):
    for i in range(1, len(x_list)+1):
        plt.annotate(y_list[i-1],(i,y_list[i-1]),ha="center")

#pclass(객실등급) //막대그래프
upper = pclass.count('1')
middle = pclass.count('2')
lower = pclass.count('3')

pclass_x = np.arange(3)
pclass_val = [upper,middle,lower]
pclass_kinds = ['1st','2nd','3rd']
pclass_color = ['r','g','b']

plt.bar(pclass_x,pclass_val,color=pclass_color,width=0.25)
add_value_label(pclass_x,pclass_val)
plt.xticks(pclass_x,pclass_kinds)
plt.title("Pclass")
plt.ylabel("Number of People")
plt.show()

#sex(성별) 그래프 //막대
man = sex.count('male')
women = sex.count('female')

sex_x = np.arange(2)
sex_val = [man,women]
sex_kinds = ['male','female']
sex_colors = ['b','r']

plt.bar(sex_x,sex_val,color=sex_colors,width=0.3)
add_value_label(sex_x,sex_val)
plt.xticks(sex_x,sex_kinds)
plt.title("Sex")
plt.ylabel("Number of People")
plt.show()


#embarked(승선항) //막대
cherbog = embarked.count('C')
queenst = embarked.count('Q')
shamton = embarked.count('S')

embarked_x = np.arange(3)
embarked_val = [cherbog,queenst,shamton]
embarked_kinds = ['Cherbourg','Queenstown','Southampton']
embarked_colors = ['orange','b','r']

plt.bar(embarked_x,embarked_val,color=embarked_colors,width=0.28)
add_value_label(embarked_x,embarked_val)
plt.xticks(embarked_x,embarked_kinds)
plt.title("Embarked")
plt.ylabel("Number of People")
plt.show()

#age(나이) 연령별 분포도//산점
# teenage = [ n for n in int(age) if n <= 11]
# twenty
# thirty
# fourty
# fifty
# sixty
# seventy
# eighty
# ninety
# hundred
# for i in range(len(passengerid)):
#     print(passengerid[i])


# def parsing(data):
#     read_csv()
#     data = list(rd)
#     print(data)


# def write():
#     f = open('test.csv', 'w', encoding='utf-8', newline='')
#     wt = csv.writer(f)
#     wt.writerows([i])
#     print()

