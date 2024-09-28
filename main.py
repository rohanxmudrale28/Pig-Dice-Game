#print("Rohan Mudrale")

from random import randint

# We will be making a func where it will change the value to 0 if die value is 1 
def update_score(score, die_value):
        if die_value == 1:
         return 0
        else:
         return score + die_value
     
def display_scoreboard(player_score, computer_score):
        print()
        print("#" * 20)
        print(f"Player Score: {player_score}")
        print(f"Computer Score: {computer_score}")
        print("#" * 20)
        print()


player_score = 0
computer_score = 0

welcome_message = """
           Welcome to 'Pig' , a dice game!
           I am Rohan Mudrale and would love it if u guys will try this game.
    
    In this game , a user and a computer opponent roll a 6-sided die each round.
    If the value of the die is a 1, the player that rolled the 1 loses all of their points.
    Otherwise, the player gets the value of die added to their points.
    The first player to reach 30 points wins!
    """
    
print(welcome_message)  

username = input("What is your name?")

while True:
    input(f"Press 'Enter' to roll the die {username}!\n")
    player_die_value = randint(1, 6)
    print(f"{username} rolls a {player_die_value}")
    computer_die_value = randint(1, 6)
    print(f"Computer rolls a {computer_die_value}")
    player_score = update_score(player_score, player_die_value)
    computer_score = update_score(computer_score, computer_die_value)
    
    
  #  print(f"{player_score=}")
  #  print(f"{computer_score=}")
  
    display_scoreboard(player_score, computer_score)
    
    
    
    if player_score >= 20:
        print(f"{username} wins!")
        break
    elif computer_score >= 20:
        print("Computer wins!")
        break

 #   break



  
    