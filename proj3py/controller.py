#controller.py

#WELCOME TO TEAM FORTRESS 2!
from char import Demoman
from char import Soldier
from map import Map

print ("WELCOME TO TEAM FORTRESS 2!")
pname=raw_input("Now, what's your name, mercenary?")
print ("You're on BLU. Which offensive class would you like to play?")
classchoice=raw_input("Soldier (high atk) or Demo (high def)? [s][d]")
if classchoice is "d":
    player=Demoman(pname)
elif classchoice is "s":
    player=Soldier(pname)
else:
    print("You gotta pick soldier or demo.")
    #come back to this

print ("Alright, {}. You've spawned as a {}. Get out there and kick some RED butt!".format(pname, player.__class__.__name__))
arena=Map()
while(player.life is True):
    command=raw_input()
    commands=["go", "help", "attack", "health", "quit"]
    command=command.split(" ")

    if command[0] in commands:
        if (command[0] == "go") and (command[1] != None):
            player.go(command[1], player, arena)
        
        elif command[0]=="help":
            player.help()
        
        elif command[0]=="health":
            player.health(player)
        else:
            pass
    else:
        pass
        
