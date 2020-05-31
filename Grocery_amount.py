weight = int(input("Enter a weight: "))
tomatoes = 60
potatoes = 50 
rice = 100
oil = 20
onions = 10
output = tomatoes + potatoes + rice + oil + onions
amount = print("amount", output * weight)
answer = input("Would you like home delivery. y/n: ")
if answer == 'y':
  print("Your groceries will be delivered at the address given ")
else:
  print("Thank you for buying from us")
