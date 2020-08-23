import random
options = ["rock", "scissors", "paper"]
comp_choice = random.choice(options)
round=1
comp_win=0
user_win=0
while round<=3:
    user_choice=input(f"{round} round: Please enter your weapon: ").lower()
    print(f"Computer has selected: {comp_choice}")
    if user_choice=="rock":
        if comp_choice=="rock":
            print("Tie - no one wins")
        elif comp_choice=="scissors":
            user_win+=1
            print("Rock beats scissors - user wins")
        elif comp_choice=="paper":
            comp_win+=1   
            print("Paper beats rock - computer wins")    
        round+=1
    elif user_choice=="scissors":
        if comp_choice=="rock":
            comp_win+=1 
            print("Rock beats scissors - computer wins")
        elif comp_choice=="scissors":
            print("Tie - no one wins")
        elif comp_choice=="paper":
            user_win+=1
            print("Scissors beats paper - user wins")
        round+=1
    elif user_choice=="paper":
        if comp_choice=="rock":
            user_win+=1 
            print("Paper beats rock - user wins")  
        elif comp_choice=="scissors":
            comp_win+=1 
            print("Scissors beats paper - computer wins")
        elif comp_choice=="paper":
            print("Tie - no one wins")
        round+=1    
    else:
        print("Please enter valid weapon [rock, paper or scissors]")

if comp_win>user_win:
    print(f"-- Final results: User won {user_win} time(s) and computer won {comp_win} time(s).")
    print("-- Champion: Computer has won the game!")
elif user_win>comp_win:
    print(f"-- Final results: User won {user_win} time(s) and computer won {comp_win} time(s).")
    print("-- Champion: User has won the game!")
else:
    print("-- Final result: Tie - play again:)")