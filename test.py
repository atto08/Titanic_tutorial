import csv
import matplotlib.pyplot as plt
import numpy as np
from typing import List


def read_csv(): #CSV읽는 함수
    o=open("test.csv","r",encoding="utf-8")
    rd=csv.reader(o)
    ret=[]
    for i in rd:
        ret.append(i)
        return rd


def parsing(data): #CSV파싱 함수
    file1=[]
    file2=[[],[],[],[],[],[],[],[],[],[],[]]
    for line in data:
        file1.append(line)
    for i in range(0,11):
        for j in range(0,418):
            file2[i].append(file1[j][i])
    for k in file2:
        print(k)

def write(data2):
    field_names = ['PassengerId']
    file1=[]
    file2=[[],[],[],[],[],[],[],[],[],[],[]]
    passengerid = [{'PassengerId':{}}]
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
    for line in data2:
        file1.append(line)
    for i in range(0,11):
        for j in range(0,418):
            file2[i].append(file1[j][i])
    passengerid.append(file2[0])
    pclass.append(file2[1])
    name.append(file2[2])
    sex.append(file2[3])
    age.append(file2[4])
    sibsp.append(file2[5])
    parch.append(file2[6])
    ticket.append(file2[7])
    fare.append(file2[8])
    cabin.append(file2[9])
    embarked.append(file2[10])
    with open('test1.csv','w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(passengerid[0])
        # for a in range(0,11):
        #     if a == 0:
        #         field_names = ['PassengerId']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(passengerid)
        #     elif a == 1:
        #         field_names = ['Pclass']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(pclass)
        #     elif a == 2:
        #         field_names = ['Name']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(name)
        #     elif a == 3:
        #         field_names = ['Sex']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(sex)
        #     elif a == 4:
        #         field_names = ['Age']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(age)
        #     elif a == 5:
        #         field_names = ['SibSp']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(sibsp)
        #     elif a == 6:
        #         field_names = ['Parch']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(parch)
        #     elif a == 7:
        #         field_names = ['Ticket']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(ticket)
        #     elif a == 8:
        #         field_names = ['Fare']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(fare)
        #     elif a == 9:
        #         field_names = ['Cabin']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(cabin)
        #     elif a == 10:
        #         field_names = ['Embarked']
        #         writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #         writer.writeheader()
        #         writer.writerows(embarked)


def add_value_label(x_list,y_list):
    for i in range(1, len(x_list)+1):
        plt.annotate(y_list[i-1],(i,y_list[i-1]),ha="center")




if __name__ == "__main__":
    read_csv()
    rap = read_csv()
    write(rap)
    # parsing(rap)



# #pclass(객실등급) //막대그래프
# upper = pclass.count('1')
# middle = pclass.count('2')
# lower = pclass.count('3')
#
# pclass_x = np.arange(3)
# pclass_val = [upper,middle,lower]
# pclass_kinds = ['1st','2nd','3rd']
# pclass_color = ['r','g','b']
#
# plt.bar(pclass_x,pclass_val,color=pclass_color,width=0.25)
# add_value_label(pclass_x,pclass_val)
# plt.xticks(pclass_x,pclass_kinds)
# plt.title("Pclass")
# plt.ylabel("Number of People")
# plt.show()
#
# #sex(성별) 그래프 //막대
# man = sex.count('male')
# women = sex.count('female')
#
# sex_x = np.arange(2)
# sex_val = [man,women]
# sex_kinds = ['male','female']
# sex_colors = ['b','r']
#
# plt.bar(sex_x,sex_val,color=sex_colors,width=0.3)
# add_value_label(sex_x,sex_val)
# plt.xticks(sex_x,sex_kinds)
# plt.title("Sex")
# plt.ylabel("Number of People")
# plt.show()
#
#
# #embarked(승선항) //막대
# cherbog = embarked.count('C')
# queenst = embarked.count('Q')
# shamton = embarked.count('S')
#
# embarked_x = np.arange(3)
# embarked_val = [cherbog,queenst,shamton]
# embarked_kinds = ['Cherbourg','Queenstown','Southampton']
# embarked_colors = ['orange','b','r']
#
# plt.bar(embarked_x,embarked_val,color=embarked_colors,width=0.28)
# add_value_label(embarked_x,embarked_val)
# plt.xticks(embarked_x,embarked_kinds)
# plt.title("Embarked")
# plt.ylabel("Number of People")
# plt.show()

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