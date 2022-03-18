#INPORTS
import random
import getpass
import ctypes

#TITLE
ctypes.windll.kernel32.SetConsoleTitleW("Rock, Paper, Scissors")

#LEADERSTATS
comp_wins = 0
plr_wins = 0


#MAIN
    
print("")
print("")
print("     ##############################################################################################################    ")
print("     ##############################################################################################################    ")
print("     ###                                                                                                        ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                        Rock, Paper, Scissors                                           ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                                OPTIONS                                                 ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                       *1*  ---  Play                                                   ###    ")
print("     ###                                       *2*  ---  Info                                                   ###    ")
print("     ###                                       *3*  ---  Exit                                                   ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                                                                                        ###    ")
print("     ###                                                                                                        ###    ")
print("")
print("                                                   SELECT A OPTION                                                     ")
print("")
print("     ###                                                                                                        ###    ")
print("     ###                                                                                                        ###    ")
print("     ##############################################################################################################    ")
print("     ##############################################################################################################    ")
select = input("")

if select == "2":
        ctypes.windll.kernel32.SetConsoleTitleW("Infomation - Rock, Paper, Scissors")
        print("")
        print("")
        print("     ##############################################################################################################       ")
        print("     ##############################################################################################################       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###                   How To Play                    ###                         Build                     ###       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###   Rock Paper Scissors Is A Family Friendly Game  ###                                                   ###       ")
        print("     ###   You Can Pick Between Rock, Paper, Scissors.    ###             Name:       TaggerX                   ###       ")
        print("     ###   See If You Can Win!                            ###             Desc:   TaggerX Is A User Friendly    ###       ")
        print("     ###                                                  ###                    Interface With No Terminal     ###       ")
        print("     ###                                                  ###                    No Need.                       ###       ")
        print("     ###                      Info                        ###                                                   ###       ")
        print("     ###                                                  ###             Vers:   1.2                           ###       ")
        print("     ###    1. Scissors Cuts Paper                        ###                                                   ###       ")
        print("     ###    2. Paper Wraps The Rock                       ###                                                   ###       ")
        print("     ###    3. The Rock Can Break Scissors                ###             Stat:   Running                       ###       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###                                                  ###                                                   ###       ")
        print("     ###               PRESS ENTER TO EXIT                ###                   PRESS ENTER TO EXIT             ###       ")
        print("     ##############################################################################################################       ")
        print("     ##############################################################################################################       ")
        info = input("")
return 
if select == "3":
        quit()
if select == "1":

    def Choose_Option():
        print("")
        print("")
        print("")
        print("                       Game On! Rock, Paper, Scissors ")
        plr_choice = input(" $ ")
        if plr_choice == "rock":
            user_choice = "Rock"
        elif plr_choice == "paper":
            user_choice = "Paper"
        elif plr_choice == "scissors":
            user_choice = "Scissors"
        else:
            print(" -- Please Check Your Spelling And Try Again! In Lowercase.")
            return user_choice
    def Computer_Option():
        comp_choice = random.randint(1,3)
        if comp_choice == 1:
            comp_choice = "Rock"
            print("BOT - Rock")
        elif comp_choice == 2:
            comp_choice = "Paper"
            print("BOT - Paper")
        else:
            comp_choice = "Scissors"
            print("BOT - Scissors")
        return comp_choice
    while True:
        user_choice = Choose_Option()
        comp_choice = Computer_Option()

        if user_choice == "Rock":
            if comp_choice == "Rock":
                print("")
                print("################")
                print("##  You Tied  ##")
                print("################")
                print("")
        if user_choice == "Paper":
            if comp_choice == "Paper":
                print("")
                print("################")
                print("##  You Tied  ##")
                print("################")
                print("")
        if user_choice == "Scissors":
            if comp_choice == "Scissors":
                print("")
                print("################")
                print("##  You Tied  ##")
                print("################")
                print("")
        if user_choice == "Paper":
            if comp_choice == "Scissors":
                print("")
                print("################")
                print("##  You Lost  ##")
                print("################")
                print("")
        if user_choice == "Scissors":
            if comp_choice == "Rock":
                print("")
                print("################")
                print("##  You Lost  ##")
                print("################")
                print("")

        if user_choice == "Rock":
            if comp_choice == "Paper":
                print("")
                print("################")
                print("##  You Lost  ##")
                print("################")
                print("")
        if user_choice == "Scissors":
            if comp_choice == "Paper":
                print("")
                print("################")
                print("##  You Won!  ##")
                print("################")
                print("")
        if user_choice == "Paper":
            if comp_choice == "Rock":
                print("")
                print("################")
                print("##  You Won!  ##")
                print("################")
                print("")
        if user_choice == "Rock":
            if comp_choice == "Scissors":
                print("")
                print("################")
                print("##  You Won!  ##")
                print("################")
                print("")
                pass
