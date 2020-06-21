players = []
players = [{'Name': "Aubameyang", 'Goals': 16, 'Age': 28, 'Appearances': 20, 'Salary': 60000, 'Nationality': 'Gabon'},{'Name':'Lacazette', 'Goals': 12, 'Age': 24, 'Appearances': 22, 'Salary': 55000, 'Nationality': "France"},{'Name': 'Martinelli', 'Goals': 11, 'Age': 17, 'Appearances': 9, 'Nationality': 'Brazil', 'Salary': 30000}, {'Name': 'Pepe', 'Goals': 9, 'Age': 28, 'Appearances': 20, 'Nationality': 'France', 'Salary': 55000}]
for x in players:
    print(x['Name'], "is originally from", x['Nationality'])
