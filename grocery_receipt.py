#Display
print("Menon Stores")
print("Item    Price")
print("Tomato   30")
print("Potato   25")
print("Rice    100")
print("Onion    15")
print("Aata     30")
print("Ginger   10")
print("Garlic   15")
print("Oil      25")
print("Chicken  150")
print("Carrot   30")

#item_price - price of items
#item_total - total cost of each item
tom_price = 30
tom_total = 0
pot_price = 25
pot_total = 0
rice_price = 100
rice_total = 0
oni_price = 15
oni_total = 0
aata_price = 30
aata_total = 0
gin_price = 10
gin_total = 0
gar_price = 15
gar_total = 0
oil_price = 25
oil_total = 0
chic_price = 150
chic_total = 0
carr_price = 30
carr_total = 0

#item_temp - temporarily stores the cost of the grocery items
tom_temp = 0
pot_temp = 0
rice_temp = 0
oni_temp = 0
aata_temp = 0
gin_temp = 0
gar_temp = 0
oil_temp = 0
chic_temp = 0 
carr_temp = 0

#item_qty - temporarily stores the quantity of the grocery items
tom_qty = 0
pot_qty = 0
rice_qty = 0
oni_qty = 0
aata_qty = 0
gin_qty = 0
gar_qty = 0
oil_qty = 0
chic_qty = 0
carr_qty = 0

#item_qty - temporaily stores the quantity of the grocery items
tom_qty = 0
pot_qty = 0
rice_qty = 0
oni_qty = 0
aata_qty = 0
gin_qty = 0
gar_qty = 0
oil_qty = 0
chic_qty = 0
carr_qty = 0

#item_qty_tot - keeps a track on the total quantity ordered per item
tom_qty_tot = 0
pot_qty_tot = 0
rice_qty_tot = 0
oni_qty_tot = 0
aata_qty_tot = 0
gin_qty_tot = 0
gar_qty_tot = 0
oil_qty_tot = 0
chic_qty_tot = 0
carr_qty_tot = 0

#ans set to yes, so that it enters the while loop
ans = "y"
while ans == 'y':
  print ("==================================")
  choice = input("What do you want? ")
  if choice == "tomato":
    print("Tomato")
    print("Price = 30")
    tom_qty = float(input("Enter quantity: "))
    tom_qty_tot = tom_qty + tom_qty_tot 
    tom_temp = tom_qty * tom_price
    tom_total = tom_total + tom_temp
  elif choice == "potato":
    print("Potato")
    print("Price = 25")
    pot_qty = float(input("Enter quantity: "))
    pot_qty_tot = pot_qty_tot + pot_qty
    pot_temp = pot_qty * pot_price
    pot_total = pot_total + pot_temp
  elif choice == "rice":
    print("Rice")
    print("Price = 100")
    rice_qty = float(input("Enter quantity: "))
    rice_qty_tot = rice_qty_tot + rice_qty
    rice_temp = rice_qty * rice_price
    rice_total = rice_total + rice_temp
  elif choice == "onion":
    print("Onion")
    print("Price = 15")
    oni_qty = float(input("Enter quantity: "))
    oni_qty_tot = oni_qty_tot + oni_qty
    oni_temp = oni_qty * oni_price
    oni_total = oni_total + oni_temp
  elif choice == "aata":
    print("Aata")
    print("Price = 30")
    aata_qty = float(input("Enter quantity: "))
    aata_qty_tot = aata_qty_tot + aata_qty
    aata_temp = aata_qty * aata_price
    aata_total = aata_total + aata_temp
  elif choice == "ginger":
    print("Ginger")
    print("Price = 10")
    gin_qty = float(input("Enter quantity: "))
    gin_qty_tot = gin_qty_tot + gin_qty
    gin_temp = gin_qty * gin_price
    gin_total = gin_total + gin_temp
  elif choice == "garlic":
    print("Garlic")
    print("Price = 15")
    gar_qty = float(input("Enter quantity: "))
    gar_qty_tot = gar_qty_tot + gar_qty
    gar_temp = gar_qty * gar_price
    gar_total = gar_total + gar_temp
  elif choice == "oil":
    print("Oil")
    print("Price = 25")
    oil_qty = float(input("Enter quantity: "))
    oil_qty_tot = oil_qty_tot + oil_qty
    oil_temp = oil_qty * oil_price
    oil_total = oil_total + oil_temp
  elif choice == "chicken":
    print("Chicken")
    print("Price = 150")
    chic_qty = float(input("Enter quantity: "))
    chic_qty_tot = chic_qty_tot + chic_qty
    chic_temp = chic_qty * chic_price
    chic_total = chic_total + chic_temp
  elif choice == "carrot":  
    print("Carrot")
    print("Price = 20")
    carr_qty = float(input("Enter quantity: "))
    carr_qty_tot = carr_qty_tot + carr_qty
    carr_temp = carr_qty * carr_price
    carr_total = carr_total + carr_temp
  ans = input("Do you want to continue. y/n: ")
else:
  name = input ("Customer Name: ")
  amount = tom_total + pot_total + rice_total + oni_total + aata_total + gin_total + gar_total + oil_total + chic_total + carr_total
  from datetime import date
  today = date.today()
  print ("==================================")
  print("RECEIPT:")
  print("Customer Name: ", name)
  print ("Date: ", today)

 # if (tom_total!=0 OR pot_total!=0 OR rice_total!=0 OR oni_total!=0 OR aata_total!=0 OR gin_total!=0 OR gar_total!=0 OR oil_total!=0 OR chic_total!=0 OR carr_total!=0):
  print("Item    Quantity    Price")
  print("Tomato ", tom_qty_tot, tom_total)
  print("Potato ", pot_qty_tot, pot_total)
  print("Rice ", rice_qty_tot, rice_total)
  print("Onion ", oni_qty_tot, oni_total)
  print("Aata ", aata_qty_tot, aata_total)
  print("Ginger", gin_qty_tot, gin_total)
  print("Garlic ", gar_qty_tot, gar_total)
  print("Oil ", oil_qty_tot, oil_total)
  print("Chicken ", chic_qty_tot, chic_total)
  print("Carrot ", carr_qty_tot, carr_total)
  print("*****************************************")
  print("Final amount: ", amount)
