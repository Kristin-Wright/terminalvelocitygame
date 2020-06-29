import random
import sys
import time

age = random.randint(12,70)

# def start_again()
#     Print("Press ENTER to try again")
#     input("")
#     character()

planet = [
    "Ego", 
    "Capria", 
    "Solaris", 
    "Cybertron", 
    "Worlorn",
    "Titan Prime",
    "Gamilon",
    "Contraxia",
    "Vormir",
    "Jotunheim",
    "Gamora",
    "Xandar",
    "Knowhere",
    "Neptune"
]
my_planet = random.choice(planet)
personality = [
    "Architect",
    "Logician",
    "Commander",
    "Debater",
    "Advocate",
    "Mediator",
    "Protagonist",
    "Campaigner",
    "Logistician",
    "Defender",
    "Executive",
    "Consul",
    "Virtuoso",
    "Adventurer",
    "Entrepreneur",
    "Entertainer"
]

# typewriter effects

type_of_player = random.choice(personality)

def print_slow(str):
    for char in str:
        time.sleep(.01)
        sys.stdout.write(char)
        sys.stdout.flush()

def print_slow2(str):
    for char in str:
        time.sleep(.08)
        sys.stdout.write(char)
        sys.stdout.flush()

def print_fast(str):
    for char in str:
        time.sleep(.001)
        sys.stdout.write(char)
        sys.stdout.flush()


# End game

def end_game():
    print("")
    print_slow(u"\u001b[36m     You emerge from the government unit a hero!")
    print("")
    print_slow("     You receive a message from your team on {}.".format(my_planet))
    print("")
    print_slow("     'You have saved us all {}, we cannot thank you enough for your service.'".format(name))
    print("")
    print_slow("     You return to your ship and head back to your home planet.")
    print("")
    print_slow("     Thank you for playing!")

# level 3

def level_3():
    print("")
    print_slow(u"\u001b[31m  Level Three.")
    print("")
    print_slow(u"\u001b[36m     You finally enter the control room.")
    print("")
    print_slow("     You search the whole room, to find the main terminal located at the back.")
    print("")
    print_slow("     This is it! This is your chance {} to save {} once and for all.".format(name,my_planet))
    print("")
    print_slow("     You see written on the terminal 'STOP LAUNCH' ")
    print("")
    password= input(u"\u001b[31m     Enter the correct passowrd" + "\u001b[33m [if no code enter 0]")
    if password == "codenation":
        print("")
        print(u"\u001b[33m ")
        print("""    ::::    ::::  :::::::::::  ::::::::   ::::::::  :::        ::::::::::       :::            :::     :::    ::: ::::    :::  ::::::::  :::    ::: 
    +:+:+: :+:+:+     :+:     :+:    :+: :+:    :+: :+:        :+:              :+:          :+: :+:   :+:    :+: :+:+:   :+: :+:    :+: :+:    :+: 
    +:+ +:+:+ +:+     +:+     +:+        +:+        +:+        +:+              +:+         +:+   +:+  +:+    +:+ :+:+:+  +:+ +:+        +:+    +:+ 
    +#+  +:+  +#+     +#+     +#++:++#++ +#++:++#++ +#+        +#++:++#         +#+        +#++:++#++: +#+    +:+ +#+ +:+ +#+ +#+        +#++:++#++ 
    +#+       +#+     +#+            +#+        +#+ +#+        +#+              +#+        +#+     +#+ +#+    +#+ +#+  +#+#+# +#+        +#+    +#+ 
    #+#       #+#     #+#     #+#    #+# #+#    #+# #+#        #+#              #+#        #+#     #+# #+#    #+# #+#   #+#+# #+#    #+# #+#    #+# 
    ###       ### ###########  ########   ########  ########## ##########       ########## ###     ###  ########  ###    ####  ########  ###    ### 
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                
                :::    :::     :::      ::::::::         ::::::::  :::::::::::  ::::::::  :::::::::  :::::::::  :::::::::: :::::::::                
                :+:    :+:   :+: :+:   :+:    :+:       :+:    :+:     :+:     :+:    :+: :+:    :+: :+:    :+: :+:        :+:    :+:               
                +:+    +:+  +:+   +:+  +:+              +:+            +:+     +:+    +:+ +:+    +:+ +:+    +:+ +:+        +:+    +:+               
                +#++:++#++ +#++:++#++: +#++:++#++       +#++:++#++     +#+     +#+    +:+ +#++:++#+  +#++:++#+  +#++:++#   +#+    +:+               
                +#+    +#+ +#+     +#+        +#+              +#+     +#+     +#+    +#+ +#+        +#+        +#+        +#+    +#+               
                #+#    #+# #+#     #+# #+#    #+#       #+#    #+#     #+#     #+#    #+# #+#        #+#        #+#        #+#    #+#               
                ###    ### ###     ###  ########         ########      ###      ########  ###        ###        ########## #########                """)
        print("")
        end_game()
    elif password == "python":
        print("")
        print_slow(u"\u001b[31m     ALARMS ACTIVATED")
        print("")
        print_slow(u"\u001b[36m     OH NO! It seems you have set off the alarms, now all guards are aware.")
        print("")
        print_slow("     You are captured by guards and taken hostage.")
        print("")
        print_slow("     Return to level 2 to find the correct password.")
        print("")
        level_2()
    else:
        print_slow(u"\u001b[36m     No code")
        print("")
        print_slow("     Return to level 2 to find the correct password.")
        print("")
        level_2()


# level 2

def level_2():
    print("")
    print_slow(u"\u001b[31m   Level Two.")
    print("")
    print_slow(u"\u001b[36m     You recognise your old scientist colleague Kingsley from college on {}, who was reported missing many years ago.".format(my_planet))
    print("")
    print_slow("     Kingsley explains he was taken by Earth government officials to build the missile that would destroy your home planet. ")
    print("")
    print_slow("     But he says he's managed to get hold of the password for the terminal that controls the missile launch. If you get there in time and input the password you can stop the missile launch!")
    print("")
    print_slow("     You're about to write the password down but you remember the rumours that Kingsley had defected to the earth government willingly.")
    print("")
    trust= input("     Do you trust Kingsley? [Y/N]" )
    if trust == "N" or trust == "n":
        print("")
        print_slow("     You decide that Kingsley is trying to sabotage your mission. You throw a chair at Kingsley! And escape through the door.")
        level_3()
    elif trust == "Y" or trust == "y":
        print("")
        print_slow("     Kingsley says, 'I just need to make sure you are {}! If so, you would know what the output of this code is... for i in range (10): print (i).'".format(name))
        print("")
        answer= input("     What's your answer?" )
        if answer == "0123456789":
            print_slow("     That's correct! Here is the password: 'codenation'.")
        else:
            print_slow("     Kingsley thinks that you're a fake. He throws a nearby computer at you! He says, 'Take this password anyways: 'python' '.")
            print("")
            print_slow("     You walk through the door. As you leave, you notice he stares at you with a shifty look on his face. You decide to press on and make your way to the control room.")
        level_3()
        
# # Level 1

def middle_corridor():
    print("")
    print_slow("     You sprint down the corridor, turn the corner and you see a guard approaching you!")
    print("")
    print_slow(u"\u001b[34m     Press" + "\u001b[31m ENTER" + "\u001b[34m to find out what happens....")
    input("")
    print("")
    options = [
        "capture",
        "escape"
    ]
    capture_escape = random.choice(options)
    if capture_escape == "capture":
        print_slow(u"\u001b[36m     Oh no! After a brief skirmish the guard overpowers you and you are captured... You've failed the mission and {} is destroyed...".format(my_planet))  
        print("")
        level_1()
    else:
        print_slow(u"\u001b[36m     You run back through the maze of corridors and manage to lose the guard. Well done! You take the staircase down to the next level.")
        print("")
        print_slow("     When you open the security door you glimpse a shadowy figure standing against the wall, looking at you with confusion...")
        print("")
        kingsley()
def kingsley():
    time.sleep(4.0)
    print(u"\u001b[35m ")
    print("""              .--..--..--..--..--..--.
            .' \  (`._   (_)     _   .
          .'    |  '._)         (_)  |
          \ _.')\      .----..---.   /
          |(_.'  |    /    .-\-.  \  |
          \     0|    |   ( O| O) | o|
           |  _  |  .--.____.'._.-.  |
           \ (_) | o         -` .-`  |
            |    \   |`-._ _ _ _ _\ /
            \    |   |  `. |_||_|   |
            | o  |    \_      \     |     -.   .-.
            |.-.  \     `--..-'   O |     `.`-' .'
          _.'  .' |     `-.-'      /-.__   ' .-'
        .' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
        `-._  `.  |________/\_____|    `-.'
           .'   ).| '=' '='\/ '=' |
           `._.`  '---------------'
                   //___\   //___.
                     ||       ||
                     ||_.-.   ||_.-.
                    (_.--__) (_.--__) """)
    level_2()
def right_corridor():
    print("")
    print_slow("     You sprint down the long corridor and take the staircase down to the next level.")
    print("")
    print_slow("     When you open the security door you glimpse a shadowy figure standing against the wall, looking at you with confusion...")
    print("")
    print("")
    print("")
    print("")
    kingsley()
def left_corridor():
    print("")
    print_slow("     You sprint down the corridor, turn the corner and find... a dead end. There seems to be no exit so you retrace your steps back to the elevator.")
    print("")
    level_1()
def level_1():
    print("")
    print_slow(u"\u001b[31m   Level One.")
    print("")
    print_slow(u"\u001b[36m     You take the elevator to the first floor. Ahead of you are three corridors.")
    print("")
    print("")
    left_right_mid = input("     Which do you choose, {}? [L/R/M] " .format(name))
    if left_right_mid == "L" or left_right_mid == "l":
        left_corridor()
    elif left_right_mid == "R" or left_right_mid == "r":
        right_corridor()
    elif left_right_mid == "M" or left_right_mid == "m":
        middle_corridor()
    else:
        print("")
        print_slow("    Please select [L/R/M] ")
        level_1()



# Character Creator


def character():
    print(u"\u001b[32m")
    print_fast("""    ::::::::::: :::::::::: :::::::::  ::::    ::::  ::::::::::: ::::    :::     :::     :::        
        :+:     :+:        :+:    :+: +:+:+: :+:+:+     :+:     :+:+:   :+:   :+: :+:   :+:        
        +:+     +:+        +:+    +:+ +:+ +:+:+ +:+     +:+     :+:+:+  +:+  +:+   +:+  +:+        
        +#+     +#++:++#   +#++:++#:  +#+  +:+  +#+     +#+     +#+ +:+ +#+ +#++:++#++: +#+        
        +#+     +#+        +#+    +#+ +#+       +#+     +#+     +#+  +#+#+# +#+     +#+ +#+        
        #+#     #+#        #+#    #+# #+#       #+#     #+#     #+#   #+#+# #+#     #+# #+#        
        ###     ########## ###    ### ###       ### ########### ###    #### ###     ### ########## 
    
    :::     ::: :::::::::: :::        ::::::::   :::::::: ::::::::::: ::::::::::: :::   :::        
    :+:     :+: :+:        :+:       :+:    :+: :+:    :+:    :+:         :+:     :+:   :+:        
    +:+     +:+ +:+        +:+       +:+    +:+ +:+           +:+         +:+      +:+ +:+         
    +#+     +:+ +#++:++#   +#+       +#+    +:+ +#+           +#+         +#+       +#++:          
     +#+   +#+  +#+        +#+       +#+    +#+ +#+           +#+         +#+        +#+           
      #+#+#+#   #+#        #+#       #+#    #+# #+#    #+#    #+#         #+#        #+#           
        ###     ########## ########## ########   ######## ###########     ###        ###       """)
    print("") 
    print("")
    global name
    print_slow(u"\u001b[31m     Welcome to your mission  \n")
    print("")
    print_slow(u"\u001b[34m     Press" + "\u001b[31m ENTER" + "\u001b[34m to create character.....  ")
    input("")
    print("")
    print_slow("    RANDOMISING PLANET")
    print("")
    print_slow2(u"\u001b[37m      ###############")
    print("")
    print_slow(u"\u001b[34m    RANDOMISING PERSONALITY")
    print("")
    print_slow2(u"\u001b[37m      ###############")
    print("")
    print_slow(u"\u001b[34m    RANDOMISING AGE")
    print("")
    print_slow2(u"\u001b[37m      ###############")
    time.sleep(1.0)
    print("")
    name = input(u"\u001b[34m     What is your name? ").capitalize()
    print("")
    gender = input("     Are you Male or Female? [M/F] ")
    print("")
    if gender == "M" or gender == "m":
        print_slow(u"\u001b[36m     Welcome {}! You are male and {} years old - a {} from the planet {}.You have just landed on Earth, where a covert government unit is launching a missile to destroy your home planet.".format(name,age,type_of_player,my_planet))
    elif gender == "F" or gender == "f":
        print_slow(u"\u001b[36m    Welcome {}! You are female and {} years old - a {} from the planet {}. You have just landed on Earth, where a covert government unit is launching a missile to destroy your home planet.".format(name,age,type_of_player,my_planet))
    print("")
    print("")
    print("")
    print(u"\u001b[33m")
    time.sleep(2.0)
    print_fast("""                        `. ___
                        __,' __`.                _..----....____
           __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
      _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
    ,'________________                          \`-._`-','
     `._              ```````````------...___   '-.._'-:
        ```--.._      ,.                     ````--...__\-.
                `.--. `-`                       ____    |  |`
                  `. `.                       ,'`````.  ;  ;`
                    `._`.        __________   `.      \'__/`
                       `-:._____/______/___/____`.     \  `
                                   |       `._    `.    .
                                   `._________`-.   `.   `.___
                                                     `------'`              """)

                                                       
    print(u"\u001b[37m      ")                                             
    print("""     ____^/\___^--____/\____O______________/\/\---/\___________---______________
       /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
             --           -            --  -      -         ---  __       ^
       --  __                      ___--  ^  ^                         --  __                    """)
    print("")
    print("")
    print("")
    print_slow(u"\u001b[36m     You leave your ship and make your way to the command centre. After a long walk, you arrive at the large concrete structure and make your way inside.")    
    print("")
    print_slow(u"\u001b[31m     Your mission is to stop the missile launch by any means possible.")
    print("")
    level_1()

character()
