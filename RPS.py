
import random

print("Welcome to Rock Paper Scissors, made by Jadin Baillie. Please type 'rock', 'paper', or 'scissors'"   )


def computer_guess(): 

    a = ["rock", "paper", "scissors"]
    cmove = random.choice(a).strip()
    return cmove

def ask_user_for_move():
    
    move = input("Make a move:")
    return move.strip().upper()




def check_who_wins():
    
    if (cmove == "rock"):
        if (move == "ROCK"):
            return "Tie"
        elif (move == "PAPER"):
            return "You Win"
        elif (move == "SCISSORS"):
            return "You Lose"
        else:
            return "Please type 'rock', 'paper', or 'scissors'"   
    elif (cmove == "paper"):
        if (move == "ROCK"):
            return "You Lose"
        elif (move == "PAPER"):
            return "Tie"
        elif (move == "SCISSORS"):
            return "You Win" 
        else:
            return "Please type 'rock', 'paper', or 'scissors'"   
    elif (cmove == "scissors"):
        if (move == "ROCK"):
            return "You Win"
        elif (move == "PAPER"):
            return "You Lose"
        elif (move == "SCISSORS"):
            return "Tie"
        else:
            return "Please type 'rock', 'paper', or 'scissors'"   
        

keep = 1




while keep == 1:
    move = ask_user_for_move()
    cmove = computer_guess()
   
    print("Opponents move was " + cmove)    
    print(check_who_wins())
    

    
    


        