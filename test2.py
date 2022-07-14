import csv

with open('C:/Users/user/Desktop/sparta/Titanic_tutorial/csv_savefile.csv', 'w', newline='') as f :
    writer = csv.writer(f)

    writer.writerow()