import random

choices = ["Rock", "Paper", "Scissors"]
loop = True

while loop:
    print("\n1 = Rock, 2 = Paper, 3 = Scissors")
    playerChoice = input("Please Enter your choice: ")
    playerChoice = int(playerChoice)

    if playerChoice < 1 or playerChoice > 3:
        print("\nError: Enter the number between 1 to 3")
    else: 
        ramChoice = random.randint(1, 3)

        playerChoiceIndex = print("\nYou chose: ", choices[playerChoice - 1])
        ramChoiceIndex = print("Computer chose: ", choices[ramChoice - 1])

        if (playerChoice == 1 and ramChoice == 3) or \
            (playerChoice == 2 and ramChoice == 1) or \
            (playerChoice == 3 and ramChoice == 2):
            print("\nYou Win!\n")
            loop = False

        elif playerChoice == ramChoice:
            print("\nIt's a tie!\n")
            loop = False

        else:
            print("\nYou Lose!\n")
            loop = False
    
        
    