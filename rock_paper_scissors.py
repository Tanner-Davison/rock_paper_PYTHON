import random 
options = {"rock":0,"paper":1, "sciccors":2}
computer = random.randint(0,2)
computers_move = list(options.keys())[computer]

players_choice = input("rock, paper or sciccors\n").lower()
    
while players_choice not in options.keys():
    players_choice = input("Invalid choice please enter rock, paper, or sciccors\n")
    
if options[players_choice] == options[computers_move]:
    print(f"It's a tie! you both chose {players_choice}")
elif options[players_choice] - options[computers_move] % 3 ==1:
    print(f"You win! {players_choice} beats {computers_move}")
else:
    print(f"Computer wins! {computers_move} beats {players_choice}")


    
