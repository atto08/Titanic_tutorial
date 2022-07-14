import csv
import matplotlib.pyplot as plt
import pandas

o = open('test.csv', 'r', encoding="utf-8")
rd = csv.DictReader(o)

# for row in rd:
#     print(row)

data = list(rd)
print(data)

def read_csv():
    o = open('test.csv', 'r', encoding="utf-8")
    rd = csv.reader(o)
    return rd

def parsing(data):
    read_csv()
    # data = list(rd)
    # print(data)


#     passengerid = []
#     pclass = []
#     names = []
#     sex = []
#     age = []
#     sibsp = []
#     parch = []
#     ticket = []
#     fare = []
#     cabin = []
#     embarked = []
#     passengerid.append(line[0])
#     pclass.append(line[1])
#     names.append(line[2])
#     sex.append(line[3])
#     age.append(line[4])
#     sibsp.append(line[5])
#     parch.append(line[6])
#     ticket.append(line[7])
#     fare.append(line[8])
#     cabin.append(line[9])
#     embarked.append(line[10])
#
# def write():
#     f = open('test.csv', 'w', encoding='utf-8', newline='')
#     wt = csv.writer(f)
#     wt.writerows([i])
#     print()

# labels = ['PassengerId','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
# print(labels[0])
# for line in rd:
#     passengerId = []
#     passengerId.append(line[0])
#     print(passengerId)
    # passengerid = []
    # pclass = []
    # names = []
    # sex = []
    # age = []
    # sibsp = []
    # parch = []
    # ticket = []
    # fare = []
    # cabin = []
    # embarked = []
    # dic = {
    #     'PassengerId': passengerid,
    #     'pclass': pclass,
    #     'name': names,
    #     'sex': sex,
    #     'age': age,
    #     'sibsp': sibsp,
    #     'parch': parch,
    #     'ticket': ticket,
    #     'fare': fare,
    #     'cabin': cabin,
    #     'embarked': embarked
    # }
    # passengerid.append(line[0])
    # pclass.append(line[1])
    # names.append(line[2])
    # sex.append(line[3])
    # age.append(line[4])
    # sibsp.append(line[5])
    # parch.append(line[6])
    # ticket.append(line[7])
    # fare.append(line[8])
    # cabin.append(line[9])
    # embarked.append(line[10])
