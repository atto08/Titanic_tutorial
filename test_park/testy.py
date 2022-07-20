import csv

field_names = ['No', 'Name', 'Car Model']

cars = [
    {'No': 1, 'Name': 'Benzema', 'Car Model': '488 GTB'},
    {'No': 2, 'Name': 'Kroos', 'Car Model': '918 Spyder'},
    {'No': 3, 'Name': 'Casemiro', 'Car Model': 'La Voiture Noire'},
    {'No': 4, 'Name': 'Vinicius', 'Car Model': 'Phantom'},
    {'No': 5, 'Name': 'Modric', 'Car Model': 'BMW X7'},
]

with open('Real.csv', 'w',newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(cars)