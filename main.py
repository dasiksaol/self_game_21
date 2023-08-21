import random
import os
import time

def clear_terminal():
    if os.name == 'nt':  
        _ = os.system('cls')

def info():
    name = input("Please Input Username: ")
    print(f"\nWelcome {name}, Let's Begin Our Game of 21.")
    return name

def start():
    player = random.randint(1, 13)
    bot = random.randint(5, 21)
    return player , bot

def hit(player):
    addition = random.randint(1,13)
    player += addition
    return player
       
def stand(player, bot, name):
    if player > bot:
        print(f"Player: {player} > House: {bot}")
        print(f"Congratulation {name}! You Won")
    elif player < bot:
        print(f"Player: {player} < House: {bot}")
        print(f"You Lose, {name}!!")
    elif player == bot:
        print(f"Player: {player} = House: {bot}")
        print(f"it's Draw, {name}!!")

def main():
    name = info()
    player, bot = start()
    clear_terminal()
    print(f"player: {player}")
    
    while player <= 21:
    
        print("Do you wish to Hit or Stand. Type 1 for Hit. Type 0 for Stand")
        hit_ = input("Hit or Stand? \n>>> ")
        try:
            hit_ = int(hit_)
        
            time.sleep(1)
            clear_terminal()
            if hit_ == 1:
                player = hit(player)
                if player < 21:
                    print(f"player: {player}")
                elif player > 21:
                    print(f"\nPlayer: {player} \nYou Lose, {name}. You Went Over 21")
                    break
            elif hit_ == 0:
                player = stand(player, bot, name)
                break
            
        except ValueError:
            print("Please Enter 1 (hit) or 0 (stand)")
            

        
                          
            
main()
        


    
