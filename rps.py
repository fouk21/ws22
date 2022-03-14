import random 

actions = ["rock","paper","scissors"]
while True:
    user_action = input("Enter a Choice(rock, paper, scissors) or exit to exit game :")

    computer_action = random.choice(actions)

    print("User : " + user_action + " Copmuter : " + computer_action)
    
    if user_action == computer_action:
        print("Its a Draw!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("You Lose :(")
        else : print ("You Win!!")

    elif user_action == "paper":
        if computer_action == "scissors":
            print("You Lose :(")
        else : print ("You Win!!")

    elif user_action == "scissors":
        if computer_action == "rock":
            print("You Lose :(")
        else : print ("You Win!!")

    elif user_action == "exit":
        print("BYE!!!")
        exit()
        
    else: 
        print("Invalid Input")

