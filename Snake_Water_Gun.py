# Snake, Water, Gun 
# We are building our version of snake, water, gun game 

# Gun beats the snake, water beats the gun, and snake beats the water 

import random 

def round():
    '''returns 1 on user victory, 0 on tie and -1 on computer victory''' 
    swg = ["S", "W", "G"] # represets Snake, Water and Gun for computer choice 
    swg1 = ["Snake", "Water", "Gun"]
    i = random.randint(0,2)
    comp_choice = swg[i]
    com_word = swg1[i]
    user_choice = None 

    while True:
        user_choice = input("Please enter your choice: 'S' for Snake, 'W' for Water, or 'G' for Gun. ").upper()
        if user_choice in swg:
            break 
        else: 
            print("Invalid Choice. Please provide input carefully")
    
    ui = swg.index(user_choice)
    user_word = swg1[ui]
    print(f"You chose {user_word}.")
    print(f"Computer chose {com_word}")
    print("Outcome : ")


    if user_choice == 'G':
        if comp_choice == 'G':
            print("A Tie")
            return 0
        elif comp_choice == 'W':
            print("Computer won")
            return -1
        else:
            print("You Won")
            return 1 
    elif user_choice == 'S':
        if comp_choice == 'S':
            print("A Tie")
            return 0
        elif comp_choice == 'G':
            print("Computer Won")
            return -1
        else:
            print("You Won")
            return 1 
    else:
        if comp_choice == 'W':
            print("A Tie")
            return 0
        elif comp_choice == 'G':
            print("You Won")
            return 1
        else:
            print("Computer Won")
            return -1


def game():

    print("Welcome to Snake, Water, Gun game.")

    user_score = 0
    comp_score = 0

    choice = None 

    while True:
        res = round()
        if res == 1:
            user_score += 1
        elif res == -1:
            comp_score += 1
        
        choice = input("Type 'q' or 'quit' to quit and anything else to continue. ").lower()

        if choice == 'q' or choice == 'quit':
            break 
    
    print("Game Over")
    print("Thanks for playing.")
    print(f"You won {user_score} time while computer won {comp_score} times.")

game()