from random import randint

def guess():
    x = randint(1,10)

    while True:
        try:
            user_guess = int(input("What number am i thinking of?: "))
            if user_guess != x:
                print("You are incorrect")
            else:
                print("You are correct")
                reply = input("Want to play again?: ")
                if reply != "yes":
                    return
                else:
                    guess()
                    return
        except ValueError:
            print("You must insert a number")

guess()