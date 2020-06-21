import random
secret_num = random. randint(1, 20)
tries = 5
while tries >=1:
    guess = int(input("Enter a number from 1 to 20: "))
    if secret_num == guess:
        print("Hurray! Your guess was right.")
        break
    elif secret_num > guess:
        tries = tries - 1
        print("Too Low, you have {} more tries". format(tries))
    elif secret_num < guess:
        tries = tries - 1
        print("Too High, you have {} more tries". format(tries))
if tries == 0:
    print("You are out of tries, the secret number is {}". format(secret_num))
    

