import csv


f = open('../test.csv', 'r', encoding='UTF8')
lines = f.readlines()

labels = ['PassengerId','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
value1=[]
value2=[[],[],[],[],[],[],[],[],[],[],[]]
for line in lines:
    value1.append(line)
for i in range(0,11):
    for j in range(0,418):
        value2[i].append(value1[j][i])
for k in value2:
    print(k)
# with open("new.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(value2)

