import random
import time

print("\n=====NUMBER GUESSING GAME=====")

name=str(input("Your Good Name :"))


def start_game():
    level=input("Choose Your difficulty level: Easy / Medium / Hard :").lower()
    if level=="easy":
        print("In this level you have to choose no. b/w (1-10).\nYou have only 5 attempts.")
        time.sleep(2)
        print("Gook Luck!!!👍,",name)

        target=random.randint(1,10)
        for attempt in range(1, 6):  # 1 se 5 tak (total 5 attempts)
            guess = int(input("Enter your guess: "))
            if guess == target:
                print("🎉 Correct!")
                break
            elif guess < target:
                print("Too low")
            else:
                print("Too high")
        else:
            print("❌ Out of attempts! The number was:", target)

    elif level=="medium":
        print("In this level you have to choose no. b/w (1-50).\nYou have only 5 attempts.")
        time.sleep(2)
        print("Gook Luck!!!👍,",name)

        target=random.randint(1,50)
        for attempt in range(1, 6):  # 1 se 5 tak (total 5 attempts)
            guess = int(input("Enter your guess: "))
            if guess == target:
                print("🎉 Correct!")
                break
            elif guess < target:
                print("Too low")
            else:
                print("Too high")
        else:
            print("❌ Out of attempts! The number was:", target)

    elif level=="hard":
        print("In this level you have to choose no. b/w (1-100).\nYou have only 5 attempts.")
        time.sleep(2)
        print("Gook Luck!!!👍,",name)

        target=random.randint(1,100)
        for attempt in range(1, 6):  # 1 se 5 tak (total 5 attempts)
            guess = int(input("Enter your guess: "))
            if guess == target:
                print("🎉 Correct!")
                break
            elif guess < target:
                print("Too low")
            else:
                print("Too high")
        else:
            print("❌ Out of attempts! The number was:", target)




def show_menu():
    time.sleep(2)
    print("WELCOME,",name)
    time.sleep(2)
    print("\nThis is a game of guessing a secret number.\nYou have given some attempts to guess correct number \naccording to your Level!!")
    time.sleep(2)
    want=input("\nDo you want to PLAY? (y/n):")
    if want.lower()=="y":
        print("Let's BEGIN!!!")
        start_game()
    else:
        print("Okay,Bye...👋")

show_menu()
        
