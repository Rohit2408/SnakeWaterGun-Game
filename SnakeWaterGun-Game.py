import random
import playsound

def winning_music():

    win_music = ["anime wow.mp3"]

def loosing_music():
    loose_music = ["Nope.mp3"]

def tie():

    tie_match = ["Awkward Cricket.mp3"]


print("\n Welcome to the Snake Water Gun game!\n")
print("Game Rules:")
print("1. Snake and Water: Snake wins \n2. Water and Gun: Water wins \n3. Gun and Snake: Gun Wins")

attempts = 1
your_point = 0
computer_point = 0

while(attempts<=5):

        lst = ["s", "w", "g"]
        ran = random.choice(lst)

        inp = input("\nEnter your choice: 1. Snake(s) \n2. Water(w) \n3. Gun(g)\n")
        inp = inp.lower()

        if(inp == ran):

            print("ITS A TIE")
            print("Computer: 0")
            print("You: 0")
            tie()
        elif(inp == "w" and ran == "s"):

            computer_point = computer_point+1
            print("Computer chose snake and you chose water.")
            print("YOU LOST!!")
            print("Computer got 1 point.")
            loosing_music()
        elif(inp == "s" and ran == "w"):

            your_point = your_point+1
            print("Computer chose water and you chose snake.")
            print("YOU WON!!")
            print("You got 1 point.")
            winning_music()
        elif(inp == "w" and ran == "g"):

            your_point = your_point+1
            print("Computer chose gun and you chose water.")
            print("YOU WON!!")
            print("You got 1 point.")
            winning_music()
        elif (inp == "g" and ran == "w"):

            computer_point = computer_point+1
            print("Computer chose water and you chose gun.")
            print("YOU LOST!!")
            print("Computer got 1 point.")
            loosing_music()
        elif (inp == "g" and ran == "s"):

            your_point = your_point + 1
            print("Computer chose snake and you chose gun.")
            print("YOU WON!!")
            print("You got 1 point.")
            winning_music()
        elif (inp == "s" and ran == "g"):

            computer_point = computer_point + 1
            print("Computer chose gun and you chose snake.")
            print("YOU LOST!!")
            print("Computer got 1 point.")
            loosing_music()
        else:
            print("Invalid Input.")


        print("\n Number of guesses left: {}".format(5-attempts))
        attempts = attempts+1
if(attempts>5):
        print("GAME OVER!")

if computer_point > your_point:
        print("\nComputer wins and you lose!")

if computer_point < your_point:
        print("\nYou win and the computer loses!")

print(f"\nYour points are {your_point} and Computer's points are {computer_point}!\n")






