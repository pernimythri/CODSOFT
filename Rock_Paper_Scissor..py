
import random

class Game:
    
    def Rock_Paper_Scissor(self):
        player_score = 0
        computer_score = 0
        choices = ["rock", "paper", "scissor"]
        winning_chances = {
            "rock": "scissor",
            "paper": "rock",
            "scissor": "paper"
        }
        
        while True:
            print("******* Welcome to ROCK_PAPER_SCISSORS game *******")
        
            print("1. rock\n2. paper\n3. scissor")
            
            while True:
                try:
                    g = int(input(" ### Enter your choice number (1: rock, 2: paper, 3: scissor): "))
                    if g not in [1, 2, 3]:
                        raise ValueError("Please enter a valid choice (1 to 3)")
                    break
                except ValueError as e:
                    print(e)
            
            player_choice = choices[g - 1]
            c = random.randint(1, 3)
            computer_choice = choices[c - 1]
            print(f" *****Computer chose {computer_choice} *****")
            
            if player_choice == computer_choice:
                print("It's a draw!")
            elif computer_choice == winning_chances[player_choice]:
                print("*****You won this round!*****")
                player_score += 1
            else:
                print("***** Computer won this round.*****")
                computer_score += 1
            
            print(f"Score - Player: {player_score}, Computer: {computer_score}")
                
            while True:
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == "yes" or play_again == "no":
                    break
                else:
                    print("Please enter a valid choice (yes/no)")
            
            if play_again != "yes":
                print(f"Total Score - Player: {player_score}, Computer: {computer_score}")
                print("Ok Bye...Thanks for playing!")
                break


obj = Game()
obj.Rock_Paper_Scissor()
