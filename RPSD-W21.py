import random as Random

import time as Time
# RPSD
# to toggle hardmode on or off.
hard_mode=False
# Weapons represented by integers and also as the indices of the weapon set list
ROCK_W=0
PAPER_W=1
SCISSOR_W=2
DYNAMITE_W=3

# Comp win count
wins_comp=0.0
# player win count
wins_player=0.0
# comp weapon set
weaponSet_comp=[0,0,0,0]
# player weapon set
weaponSet_player=[0,0,0,0]

# win score threshold
WIN_LIMIT=6



# Tells if the weapon is replicable or not in case of tie.
# takes weapon as input and
# return True if the weapon is replicable otherwise False
def isReplicable(weapon):
    if weapon==DYNAMITE_W:
        return False
    else:
        return True


# return True if weaponset is empty otherwise False
def weaponSetisEmpty(weaponSet):
    for i in range(len(weaponSet)):
        if weaponSet[i]>0:
            return False
    
    return True
    

# Takes two arguments as weapon and its counter and tell if the weapon is a winner or not
def isWinner(weapon,counter):
    if weapon==ROCK_W and counter==SCISSOR_W:
        return True
    elif weapon==ROCK_W and counter==PAPER_W:
        return False
    elif weapon==ROCK_W and counter==DYNAMITE_W:
        return False
    elif weapon==PAPER_W and counter==ROCK_W:
        return True
    elif weapon==PAPER_W and counter==SCISSOR_W:
        return False
    elif weapon==PAPER_W and counter==DYNAMITE_W:
        return False
    elif weapon==SCISSOR_W and counter==PAPER_W:
        return True
    elif weapon==SCISSOR_W and counter==ROCK_W:
        return False
    elif weapon==SCISSOR_W and counter==DYNAMITE_W:
        return True
    elif weapon==DYNAMITE_W and counter==ROCK_W:
        return True
    elif weapon==DYNAMITE_W and counter==PAPER_W:
        return True
    elif weapon==DYNAMITE_W and counter==SCISSOR_W:
        return False
    else:
        return False


# gets weapon and its counter as arguments and returns a proper victor insult as String
def getInsult(weapon,counter):
    if weapon==ROCK_W and counter==SCISSOR_W or weapon==SCISSOR_W and counter==ROCK_W:
        return "Rock crushed Scissor!"
    elif weapon==ROCK_W and counter==PAPER_W or weapon==PAPER_W and counter==ROCK_W:
        return "Paper wrapped Rock!"
    elif weapon==ROCK_W and counter==DYNAMITE_W or weapon==DYNAMITE_W and counter==ROCK_W :
        return "Dynamite exploded and destroyed Rock with it!"
    elif weapon==PAPER_W and counter==SCISSOR_W or weapon==SCISSOR_W and counter==PAPER_W:
        return "Scissor cutted through Paper!"
    elif weapon==PAPER_W and counter==DYNAMITE_W or weapon==DYNAMITE_W and counter==PAPER_W:
        return "Dynamite expoded and burned paper with it!"
    elif weapon==SCISSOR_W and counter==DYNAMITE_W or weapon==DYNAMITE_W and counter==SCISSOR_W:
        return "Scissor cut the burning fuse of Dynamite, rederning it useless!"
    elif weapon==DYNAMITE_W and counter==DYNAMITE_W :
        return "Both Dynamites exploded and annihilating each other! "
    else:
        return getWeaponName(weapon)+" cannot harm "+getWeaponName(counter)


# returns a string as the name of the weapon passed
def getWeaponName(weapon):
    if weapon==SCISSOR_W:
        return "Scissors"
    elif weapon==ROCK_W:
        return "Rock"
    elif weapon==PAPER_W:
        return "Paper"
    elif weapon==DYNAMITE_W:
        return "Dynamite"
    else:
        return "ERROR_ILLEGAL_ARGUMENT"


# checks if the given string value is integer or not
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

# game intialization


print("\n\n--------------------------- Start-----------------------------\n")
print("RPSD-W21")

# data validation flag
flag=True
while flag:
    weapon_set=str(input("\nDo you want to play with 1 or 2 weapon sets?\n1 or 2> "))
    if isInt(weapon_set):
        weapon_set=int(weapon_set)
        if weapon_set==1 or weapon_set==2:
            
            for i in range(len(weaponSet_player)):
                weaponSet_player[i]=weapon_set
                weaponSet_comp[i]=weapon_set
            
            flag=False
          

        else:
            print("Select weapon set from 1 or 2 ")
    else:
        print("Please, enter a valid Positive Integer value.")


flag=True
while flag:
    difficulty=str(input("\nDifficulty easy, hard? (type i for more info about game modes)\ne, h> "))
    difficulty=difficulty.lower()
    if(difficulty=="hard" or difficulty=="easy" or difficulty=="e" or difficulty=="h" ):
        if(difficulty=="hard" or difficulty=="h"):
            hard_mode=True
        else:
            hard_mode=False
        flag=False
    elif difficulty=="i" or difficulty=="info":
        print("\nInfo:")
        print("\nEasy mode: Standard RPSD-W21 Rules.")
        print("Hard mode: 1.) Computer begins with one extra Dynamite and Comp's dynamite can be replicated on Tie.\n               Player can choose 1 additional ammunition to add to it's current weapon loadout except Scissors.\n"+
        "           2.) Tie will result in player loss (comp will gain half point by the RULE: Win by default).\n")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("\nRPSD Rules:")  
        print("Rock beats scissors (smashes scissors)\n"+
            "Paper beats rock (covers rock, disabling it)\n"+
            "Scissors beats paper and dynamite (cuts paper and fuses)\n"+
            "Dynamite beats rock and paper (exploding rock and paper)\n\n\n"+

            "* When a weapon is destroyed or disabled,\n"+
            "it is removed from play, and cannot be thrown.\n\n\n"+

            "* When a weapon wins, you get to use it again,\n"+
            "unless it is dynamite which always explodes.\n\n\n"+

            "* When rock, paper, or scissors ties,\n"+
            "both players get the same additional random item.\n"+
            "There is no upper limit to how many items a player may collect through ties.\n\n\n"+

            "* When dynamite explodes or is disabled,\n"+
            "dynamite is gone, (even if a tie) - no random item is awarded.\n\n\n"+

            "First to win 6 battles or\n"+
            "exhaust their opponent's weapons\n"+
            "WINS the whole game.\n")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

        print("-------------------------------------------------------------------------")
        print("For more info, visit: https://en.wikipedia.org/wiki/Rock_paper_scissors")
        print("-------------------------------------------------------------------------")
    else: 
        print("Please, choose from valid options--->")

# increasing weapon set of comp if player chooses hard mode and asking player to select additonal ammunition
if(hard_mode):
    print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!Comp has recieved extra supplies from enemy HQ, Tread carefully!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
    
    
    weaponSet_comp[DYNAMITE_W]=weaponSet_comp[DYNAMITE_W]+1

    Time.sleep(0.6)
    print("We could also make request for supplies from Main HQ!")
    flag=True
    while flag:
        response=str(input("\nDo you want to send a request to Main HQ for Extra supplies?\ny ,n>     "))
        response=response.lower()
        if response=="y" or response=="n" or response=="yes" or response=="no":
            if response=="y" or response=="yes":
                print("\n Understood,Now requesting Supplies from Main HQ")
                print("CONNECTING TO HQ...")
                Time.sleep(0.8)
                print("CONNECTION ESTABLISHED!\nNOW SENDING REQUEST...")
                Time.sleep(0.7)
                print("\nMain HQ has accepted the request but can only send 1 quantity of one type of ammunition!")
                flag_in=True
                while flag_in:
                    weapon_request=str(input("What Type of Weapon you want to request?\n R,P,D>    "))
                    if weapon_request=="r" or weapon_request=="rock" or weapon_request=="p" or weapon_request=="paper" or weapon_request=="s" or weapon_request=="scissors" or weapon_request=="d" or weapon_request=="dynamite":
                        flag_in=False
                        if weapon_request=="r" or weapon_request=="rock":
                            weaponSet_player[ROCK_W]=weaponSet_player[ROCK_W]+1
                        elif weapon_request=="p" or weapon_request=="paper":
                            weaponSet_player[PAPER_W]=weaponSet_player[PAPER_W]+1
                        elif weapon_request=="d" or weapon_request=="dynamite":
                            weaponSet_player[DYNAMITE_W]=weaponSet_player[DYNAMITE_W]+1
                        else:
                            print("\nUnfortunately,It seems there is no Supply of Scissors for now!\nChoose some other weapon!")
                            flag_in=True
                        if not flag_in:
                            print("\nSUPPLY REQUEST SENT,\nWAITING FOR RESPONSE...")
                            Time.sleep(0.5)
                            print("REQUEST RESPONSE: AFFIRMATIVE!, SENDING SUPPLIES!\nRESULT: OK")
                            Time.sleep(0.3)
                            print("Supplies recieved>>>>>>>")
                            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                            print("!Requested Weapon has been added to your current loadout!")
                            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        flag=False
                        
                    else:
                        print("\nPlease, choose from valid options--->")

            else:
                print(">>>>>>>>>\nUnderstood,\nNo supplies were requested from Main HQ.")
                print("\n!!!!!!!!!!!!!!!!!!!!")
                print("!To the Battlefield!")
                print("!!!!!!!!!!!!!!!!!!!!")
                flag=False
        else:
            print("Please, choose from valid options--->")

                

# game starts
# game message variable
meassage=""
# game flag
play=True
# score board codeblock initial
print("\n\nPlayer Wins :"+str(wins_player))
print("Comp Wins :"+str(wins_comp))

# show ammunition codeblock
print("\nWeapons Remaining:")
meassage="Player:"
for i in range(len(weaponSet_player)):
    meassage=meassage+" "+getWeaponName(i)+": "+str(weaponSet_player[i])
print(meassage)
meassage="Comp:"
for i in range(len(weaponSet_comp)):
    meassage=meassage+" "+getWeaponName(i)+": "+str(weaponSet_comp[i])
print(meassage)
# game starts
while play:
    player_move=-1
    comp_move=-1
    
    
    # player move code block
    flag=True
    while flag:
        move=str(input("\nYour Move (RPSD)>     "))
        move=move.lower()
        if move=="r" or move=="rock" or move=="p" or move=="paper" or move=="s" or move=="scissors" or move=="d" or move=="dynamite":
            if move=="r" or move=="rock":
                player_move=ROCK_W
            elif move=="p" or move=="paper":
                player_move=PAPER_W
            elif move=="s" or move=="scissors":
                player_move=SCISSOR_W
            else:
                player_move=DYNAMITE_W
            
            if weaponSet_player[player_move]<=0:
                print("\nAmmunation of "+getWeaponName(player_move)+" has been depleted, Choose another type of weapon.")
            else:
                weaponSet_player[player_move]=weaponSet_player[player_move]-1
                if weaponSet_player[player_move]<0:
                    weaponSet_player[player_move]=0
                print("\nPlayer uses "+ getWeaponName(player_move))
                flag=False
        else:
            print("Please, choose from valid options--->")
    
    # pause 
    Time.sleep(0.8)
    # simulating comp move
    flag= True
    while flag:
        comp_move=Random.randint(0,3)
        if not weaponSet_comp[comp_move]<=0:
            flag=False
            weaponSet_comp[comp_move]=weaponSet_comp[comp_move]-1
            if weaponSet_comp[comp_move]<=0:
                weaponSet_comp[comp_move]=0
            print("Comp uses "+getWeaponName(comp_move))
    
    # result codeblock
    
    if isWinner(player_move,comp_move):
        wins_player=wins_player+1
        print(getInsult(player_move,comp_move))
        print("\n!!!!!!!!!!!!!")
        print("!Player Wins!")
        print("!!!!!!!!!!!!!\n")
    elif isWinner(comp_move,player_move):
        wins_comp=wins_comp+1
        print(getInsult(comp_move,player_move))
        print("\n!!!!!!!!!!!!")
        print("!Comp Wins !")
        print("!!!!!!!!!!!!\n")
    else:
        if not hard_mode:
            print(getInsult(comp_move,player_move))
            print("\n!!!!!!!!!!!!")
            print("!It's a Tie!")
            print("!!!!!!!!!!!!\n")
            if isReplicable(player_move):
                weaponSet_player[player_move]=weaponSet_player[player_move]+1
                print("Player gets new ammunition for "+ getWeaponName(player_move))
            else:
                print("Non-Replicable item "+ getWeaponName(player_move)+" cannot be built again for the player!")
            if isReplicable(comp_move):
                weaponSet_comp[comp_move]=weaponSet_comp[comp_move]+1
                print("Comp gets new ammunition for "+ getWeaponName(player_move))
            else:
                print("Non-Replicable item "+ getWeaponName(player_move)+" cannot be built again for the Comp!")
        else:
            print(getInsult(comp_move,player_move))
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!It's a Tie(Hard  Mode), Comp gets half point by The RULE: Win by Default!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            wins_comp=wins_comp+0.5
            if isReplicable(player_move):
                weaponSet_player[player_move]=weaponSet_player[player_move]+1
                print("Player gets new ammunition for "+ getWeaponName(player_move))
            else:
                print("Non-Replicable item "+ getWeaponName(player_move)+" cannot be built again for the player! ")
            
            weaponSet_comp[comp_move]=weaponSet_comp[comp_move]+1
            print("Comp gets new ammunition for "+ getWeaponName(player_move))
        
    
    # removing case of infinite play
    # weapon type count
    weapon_type_left=len(weaponSet_player)
    for i in range(len(weaponSet_player)):
        if weaponSet_player[i]<=0 and weaponSet_comp[i]<=0:
            weapon_type_left=weapon_type_left-1
    
    if weapon_type_left==1 and not( weaponSetisEmpty(weaponSet_player) or weaponSetisEmpty(weaponSet_comp)):
        print(" \n\nSame type of Both Weapons remains, Remaining arsenal is Siezed!")
        for i in range(len(weaponSet_player)):
            weaponSet_player[i]=0
            weaponSet_comp[i]=0

    # score board codeblock
    print("\n\nPlayer Wins :"+str(wins_player))
    print("Comp Wins :"+str(wins_comp))

    # show ammunition codeblock
    print("\nWeapons Remaining:")
    meassage="Player:"
    for i in range(len(weaponSet_player)):
        meassage=meassage+" "+getWeaponName(i)+": "+str(weaponSet_player[i])
    print(meassage)
    meassage="Comp:"
    for i in range(len(weaponSet_comp)):
        meassage=meassage+" "+getWeaponName(i)+": "+str(weaponSet_comp[i])
    print(meassage)
    
    # giving a pause before moving to next render
    Time.sleep(1)
    # check winner codeblock
    if wins_player>=WIN_LIMIT or wins_comp>=WIN_LIMIT or weaponSetisEmpty(weaponSet_player) or weaponSetisEmpty(weaponSet_comp):
        print("\n Game Over:")
        print("----------------------------------------------------------------")
        if wins_player>=WIN_LIMIT:
            print("Player has Won by "+str(wins_player-wins_comp)+" points!")
        elif wins_comp>=WIN_LIMIT:
            print("Comp has Won by "+str(wins_comp-wins_player)+" points!")
        elif weaponSetisEmpty(weaponSet_player) and weaponSetisEmpty(weaponSet_comp):
            if wins_player>wins_comp:
                 print("Player has Won by "+str(wins_player-wins_comp)+" points!")
            elif wins_player<wins_comp:
                print("Comp has Won by "+str(wins_comp-wins_player)+" points!")
            else:
                print("Both Players fought Fiercely, The Battle has resulted in Tie!")
        elif weaponSetisEmpty(weaponSet_comp):
            print("Player has Won by having more firepower than Comp!")
        elif weaponSetisEmpty(weaponSet_player):
            print("Comp has Won by having more firepower than Player!")
        print("----------------------------------------------------------------")
        play=False
    
   
print("\n\n Thank You for Playing!")
print("-------------------------------End--------------------------------")