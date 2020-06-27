##Create Dictionary
num = {}
##Ascending Order Function
def ascending(num):
    temp = 0
    for i in range(tot_num):
        for j in range(i, tot_num):
            if num[i] > num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
    print("Ascending order")
    for x in range(tot_num):
        print(num[x])

##Descending Order Function
def descending(num):
    temp = 0
    for i in range(tot_num):
        for j in range(i, tot_num):
            if num[i] < num[j]:
                temp = num[j]
                num[j] = num[i]
                num[i] = temp
    print("Descending order")
    for x in range(tot_num):
        print(num[x])
        
##Sum of values in the dictionary Function
def sum(num):
    sum = 0
    for i in range(tot_num):
        sum = num[i] + sum
    print("The sum is", sum)

def even(num):
    print("Even Numbers:")
    for i in range(tot_num):
        if num[i]%2 == 0:
            print(num[i])

def odd(num):
    print("Odd Numbers:")
    for i in range(tot_num):
        if num[i]%2 != 0:
            print(num[i])
        
    
choice = input("Press A for ASCENDING/ D for DESCENDING/ Press S for SUM/ Press E for EVEN/ Press O for ODD: ")
## Ask for total number of nos to be entered
tot_num = int(input("How many numbers do you want? "))

## Storing number in the dictionary starting from num[0] to num[tot_num - 1]
## Index number 0 to total number minus 1
for x in range(tot_num):
    num[x] = int(input("Enter number"))

if choice == "A":
    ascending(num)
elif choice == "D":
    descending(num)
elif choice == "S":
    sum(num)
elif choice == "E":
    even(num)
elif choice == "O":
    odd(num)
else:
    print("Invalid")

