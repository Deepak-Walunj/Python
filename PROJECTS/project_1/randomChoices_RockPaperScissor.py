# import random
# def Print(name):
#     print(f"you lost {name}!")
#     if(input("Do you want to play play again?(y/n) ").lower()=='n'):
#         quit()
    
# name=input('Enter yo name ')
# print(f"Hello {name}, lets play Rock, Paper and Scissors ")

# while True:
#     t=input("Enter rock, paper, scissor ").lower()
#     if t not in ["rock","paper","scissor"]:
#         print(f"Invalid option, {name}. Please enter correctly.")
#         continue
#     comp=random.choice(["rock","paper","scissor"])
#     print(f"Your choice is: {t}\computer choice is: {comp}")
#     if(comp==t):
#         print(f"Its a draw {name}, play again")
#         continue
#     elif((comp=="paper" and t=="rock") or (comp=="scissor" and t=="paper") or (comp=="rock" and t=="scissor")):
#         Print(name)
#         continue
#     else:
#         print(f"Well done {name}, you win!")
#         if(input("Do you want to play play again?(y/n)").lower()=='n'):
#             quit()
#         continue
    # 
    
import random
def get_user_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in CHOICES:
            print(f"Your choice is: {choice}")
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_again():
    return input("Do you want to play again? (y/n): ").lower() == 'y'

def print_result(result, user, computer, name):
    if result == "draw":
        print(f"It's a draw, {name}. Both chose {user}.")
    elif result == "user":
        print(f"Well done, {name}, you win! {user} beats {computer}.")
    else:
        print(f"You lost, {name}! {computer} beats {user}.")

def main():
    name = input("Enter your name: ")
    print(f"Hello {name}, let's play Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computers choice is {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print_result(result, user_choice, computer_choice, name)
        if not play_again():
            break

if __name__ == "__main__":
    CHOICES = ["rock", "paper", "scissors"]
    main()

