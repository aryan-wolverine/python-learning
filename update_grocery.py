from datetime import date

today = date.today()

# Store details
store_name = 'Menon Stores'

# what items are we selling
items = {}
items["tomato"] = 30.0
items["potato"] = 25.0
items["rice"] = 100.0
items["onion"] = 15.0
items["aata"] = 30.0
items["ginger"] = 10.0
items["garlic"] = 15.0
items["oil"] = 25.0
items["chicken"] = 150.0
items["apples"] = 300.0
items["mangoes"] = 600.0
items["grapes"] = 100.0
items["pepsi"] = 40.0

inventory = {}
inventory["tomato"] = 100.0
inventory["potato"] = 100.0
inventory["rice"] = 100.0
inventory["onion"] = 100.0
inventory["aata"] = 100.0
inventory["ginger"] = 100.0
inventory["garlic"] = 100.0
inventory["oil"] = 100.0
inventory["chicken"] = 100.0
inventory["apples"] = 100.0
inventory["mangoes"] = 100.0
inventory["grapes"] = 100.0
inventory["pepsi"] = 100.0

# print what the store is selling
for i in items:
    print(i, '\t\t', items[i])

# take customer info
customer_name = input("Customer Name: ")

# do shopping
shopping_basket = {}

ans = "y"
while ans == 'y' or ans == 'Y':
  print ("==================================")
  what_item_i_want = input("What do you want to buy?")
  what_item_i_want = what_item_i_want.lower()

  if what_item_i_want in items:
      qty = float(input("Enter quantity: "))
      x = inventory[what_item_i_want] - qty
      if x < 0:
        print("{} for {} kg/l not in stock". format(what_item_i_want,qty))
      elif what_item_i_want in shopping_basket:
          shopping_basket[what_item_i_want] = shopping_basket[what_item_i_want] + qty
          inventory[what_item_i_want]=inventory[what_item_i_want] - qty
      else:
          shopping_basket[what_item_i_want] = qty
  else:
      print("ehhhh, not found")
  ans = input("Do you want to continue. y/n: ")

# print receipt
print('-'*80)
print("*"*10, store_name, '*'*10)
print('-'*80)
print('Receipt')
print("Customer Name: ", customer_name)
print("Date of Purchase: ", today)

total_amount = 0.0
for i in shopping_basket:
    temp = shopping_basket[i]*items[i]
    total_amount = total_amount + temp
    print(i, '\t\t', shopping_basket[i]*items[i])

print("Total Amount: Rs.", total_amount)
