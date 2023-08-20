import random

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
        
def main():
    name = info()
    player, bot = start()
    print(player)
    
    while True:
        hit_ = input("Hit?")
        try:
            hit_ = int(hit_)
            if hit_ == 1 and player <= 21:
                hit_number = hit(player)
                print(hit_number)
            elif player > 21:
                print(f"{player}, You Lose")
                break

        except ValueError:
            print("Please Enter 1 (hit) or 0 (stand)")
            

        
                          
            
main()
        


    
