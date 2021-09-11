import random
partition="----------------------------------------"
choices=['s','p','c']
mach_score = player_score = 0
no_of_matches = 5

print(partition)
print("GAME: STONE PAPER SCISSORS\n-->press s - for stone\n-->press p - for paper\n-->press c - for scissors")
print(partition)

while no_of_matches > 0:
    mach_c = random.choice(choices)
    player_c = input("choice : ")
    
    if player_c in choices:
        if mach_c =="s":
            if player_c=='s':
                print(f"machine = {mach_c}\t\tplayer = {player_c}")
                print("TIE")
            elif player_c=='p':
                print(f"machine = {mach_c}\t\tplayer = {player_c}") 
                print("WON")
                player_score += 1
            else:
                print(f"machine = {mach_c}\t\tplayer = {player_c}")
                print("LOST")
                mach_score += 1
                
        elif mach_c =="p":
            if player_c=='p':
                print(f"machine = {mach_c}\t\tplayer = {player_c}")
                print("TIE")
            elif player_c=='c':
                print(f"machine = {mach_c}\t\tplayer = {player_c}") 
                print("WON")
                player_score += 1
            else:
                print(f"machine = {mach_c}\t\tplayer = {player_c}")
                print("LOST")
                mach_score += 1
                
        else:
            if player_c=='c':
                print(f"machine = {mach_c}\t\tplayer = {player_c}")
                print("TIE")
            elif player_c=='s':
                print(f"machine = {mach_c}\t\tplayer = {player_c}") 
                print("WON")
                player_score += 1
            else:
                print(f"machine = {mach_c}\t\tplayer = {player_c}")
                print("LOST") 
                mach_score += 1
        no_of_matches -=1 
        print(partition)
    else:
        print("oops! choose again ")
print(partition)        
print(f"machine score = {mach_score}")  
print(f"player score = {player_score}")
print(partition)
if player_score>mach_score:
    print("YOU WIN")
elif player_score<mach_score:
    print("YOU LOSE")
else:
    print("ITS A TIE")
print(partition)    
