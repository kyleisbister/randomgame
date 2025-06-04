import random

    #variables for counting
games = 0
wins = 0
draws = 0
losses = 0
print("Welcome to Kyle's Rock Paper Scissors Extravaganza! Type 'quit' to quit.")

while True:
    player = input("Rock, paper, or scissors?: ")
        #making opponent list and randomizing it
    opponent = ["rock", "paper", "scissors"]
    oppchoice = random.choice(opponent)
    #if player wants to quit
    games += 1
    if player == "quit":
        print("Hope you had fun!")
        break
    if player not in opponent:
        print("Woah thats not an option")
        continue
    #displaying player and computer answer
    print(f"Computer: {oppchoice}")
    print(f"Player:  {player}")
    
    #determine who wins
    if player == oppchoice:
        draws += 1
        print("Welp we tied")
        
    elif ((player == "scissors" and oppchoice == "paper") 
        or (player == "rock" and oppchoice == "scissors")
        or (player == "paper" and oppchoice == "rock")):
            wins += 1
            print("Congratulations Winner!!!")
            
    else:
        losses += 1
        print("Aww you lose")
        
print(f"You've played {games} games! Wins: {wins}, Losses: {losses}, Draws: {draws}")
