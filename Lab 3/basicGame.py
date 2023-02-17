import random

ROCK = 1
PAPER = 2
SCISSORS = 3

print("Welcome to the AI Rock Paper Scissors Game.")

while (True):
    user = int(input("Play your move. Rock: 1, Paper: 2, Scissors: 3 \n"))
    comp = random.randint(1,3)
    if (user == comp):
        print("Computer played " + str(comp) + ". Tie \n")
    if (user == 1):
        if (comp == 2):
            print("Computer played " + str(comp) + ". Computer Wins! \n")
        elif (comp == 3):
            print("Computer played " + str(comp) + ". You Win! \n")
    elif (user == 2):
        if (comp == 3):
            print("Computer played " + str(comp) + ". Computer Wins! \n")
        elif (comp == 1):
            print("Computer played " + str(comp) + ". You Win! \n")
    elif (user == 3):
        if (comp == 1):
            print("Computer played " + str(comp) + ". Computer Wins! \n")
        elif (comp == 2):
            print("Computer played " + str(comp) + ". You Win! \n")
    else:
        print("Incorrect Input please try again.")

