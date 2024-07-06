import random
print("!!!!!!Welcome to Number Guessing Game!!!!!!")
levels = [ "easy","hard"]
print("I've chosen a number between 1 and 100")
num = random.randint(1,100)
choice=input("Enter the level(easy/hard): ")
if choice == levels[0]:
    print("You have 10 attempts to guess the number.")
    for i in range(10):
        guess = int(input("Enter your guess: "))
        if guess > num :
            print("Too high")
        elif guess < num :
            print("Too low")
        elif guess == num :
            print("You won!!")
            break
        if i == 9:
            print("You loss")
            break
        print("You have ",9-i," guesses more")
elif choice == levels[1]:
    print("You have 5 attempts to guess the number.")
    for i in range(5):
        guess = int(input("Enter your guess: "))
        if guess > num :
            print("Too high")
        elif guess < num :
            print("Too low")
        elif guess == num :
            print("You won!!")
            break
        if i == 4:
            print("You loss")
            break
        print("You have ",4-i," guesses more")

        
    