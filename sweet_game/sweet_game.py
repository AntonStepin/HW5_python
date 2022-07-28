import random

def check_for_digit(str_for_enter: str, str_for_error: str):
    result = input(str_for_enter)
    while 1:
        if not result.isdigit():
            result = input(str_for_error)
            continue
        else: 0
        return int(result)

def check_for_optins(str_for_enter: str, str_for_error: str):
    result = input(str_for_enter)
    while True or  result >3 or result<1:
        if not result.isdigit():
            result = input(str_for_error)
            continue
        elif int(result) > 3 or int(result) < 1:
            result = input("More or less than options")
            continue
        else: False
        return int(result)

def game_core (name_player, sweets_left, game_step):
    print (f"There are {sweets_left} left")
    player = check_for_digit(f"{name_player}'s move: ", "You enter not a digit, try again: ")
    while player > game_step or player < 1:
        print(f"Error -min point 1 & max point {game_step}")
        player = check_for_digit(f"{name_player} try again: ", "You enter not a digit, try again: ")
    return player

def game_core_stupid_bot (sweets_left, game_step, name_player = "Stupid_Computer"):
    print (f"There are {sweets_left} left")
    player = random.randint(0,game_step+10)
    print ((f"{name_player}'s move: {player}"))
    while player > game_step or player < 1:
        print(f"Error -min point 1 & max point {game_step}")
        player = random.randint(0,game_step+10)
        print (f"{name_player} try again: {player}")
    return player

def game_core_smart_bot(sweets_left, game_step, history, name_player = "Smart_Computer"):
    print (f"There are {sweets_left} left")
    memory = True
    with open("Memory.txt", "r") as memory:
        history_temp = history
        history_temp = history.split(",")
        for line in memory:
            player = 0
            history_temp = history
            history_temp = history.split(",")
            temp = line.split(",")
            temp.remove("\n")
            if history in line and len(temp)>len(history_temp):
                player = int(temp[len(history_temp)])
                break
        if player == 0:
            if sweets_left / game_step > 1:
                player = game_step
            elif sweets_left // game_step == 0 and sweets_left - 1 !=0:
                player = sweets_left - 1
            elif sweets_left // game_step == 1:
                player = game_step-1
            else:
                player = 1
    print(print(f"{name_player}'s move: {player}"))
    return player

def options(user_options,sweets_left, game_step, history, name_player):
    if user_options == 1:
        return game_core (name_player, sweets_left, game_step)
    elif user_options == 2:
        return game_core_stupid_bot (sweets_left, game_step, name_player = "Stupid_Computer")
    else:
        return game_core_smart_bot (sweets_left, game_step, history, name_player = "Smart_Computer")

def sweets():
    print ("Helloooo!!! This is a sweets game!!!")
    print ("Whoever take the last sweet loses")
    print ("You can chose 1 of 3 options for each player. 1. Play with person. 2. Play with stupid bot. 3. Play with smart bot")
    option_pl1 = check_for_optins("Chose option for player 1: ", "You enter not a digit, try again: ")   
    if option_pl1 == 1: name_player1 = str(input("What's your name player: "))
    elif option_pl1 == 2: name_player1 = "Stupid_Computer"
    else: name_player1 = "Smart_Computer"
    option_pl2 = check_for_optins ("Chose option for player 2: ", "You enter not a digit, try again: ")
    if option_pl2 == 1: name_player2 = str(input("What's your name other player: "))
    elif option_pl2 == 2: name_player2 = "Stupid_Computer"
    else: name_player2 = "Smart_Computer"
    number_of_points = check_for_digit("How many sweets are there in the game in total?: ", "You enter not a digit, try again: ")
    game_step = check_for_digit("How many sweets can take in one round?: ", "You enter not a digit, try again: ")
    sweets_left = int(number_of_points)
    move_line = random.randint(1,2)
    if move_line == 1:    
        print(f"{name_player1} goes first")
        next_move = 1
    else:
        print(f"{name_player2} goes first")
        next_move = 2    
    history = f"{move_line},{number_of_points},{game_step}"
    while sweets_left > 0:
        if next_move == 1:
            name_player = name_player1
            points = options(option_pl1,sweets_left, game_step, history, name_player)
            sweets_left -= points
            next_move = 2
        else:
            name_player = name_player2
            points = options(option_pl2, sweets_left, game_step, history, name_player)
            sweets_left-= points
            next_move = 1
        history+=f",{points}"
    if next_move == 1: 
        winner = name_player1
        if move_line == 1 and name_player1 != "Smart_Computer": history = "2" +  history[1:len(history)]
        else: history = "1" +  history[1:len(history)]
    else: 
        winner = name_player2
        if move_line == 2 and name_player2 != "Smart_Computer": history = "2" +  history[1:len(history)]
        else: history = "1" +  history[1:len(history)]
    with open("Memory.txt", "r") as memory:
        for line in memory:
            if history in line:
                break
            else:
                with open("Memory.txt", "a") as memory:
                    memory.writelines(f"{history},\n")
                    break        
    print(f"{winner} win!!!" )
    print(history)

sweets()

















