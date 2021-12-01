print("Welcome to Human Behavior Prediction by Ramon Denia\nStudent from IE HST\nGroup D member")
try:
    option = int(input("Please choose the game type difficulty: \n1: Easy \n2: Difficult \nSelect:"))
except:
    print("An invalid value was input")
try:
    moves=int(input("Please enter the number of rounds you want to play against the machine: "))
except:
    print("An invalid value was input")
def player_move(i): # This function store the input's move
    try:
        actual_player_option = int(input("Choose your move for this Round %d \nRemember, you can either choose 1 o 0 \nSelect your move:" % (i+1)))
    except:
        print("An invalid value was input")
    return(actual_player_option)
def machine_move(xi): # Linear congruence function called this way because it gives us the machine move randomly
    """Function used to calculate linear congruences value and the machine option for the game """
    a=2269547
    b=1
    m=2**32
    xi_plus_1 = (a*xi + b) % m
    if xi_plus_1 <= 2**31 :
        machine_option=0
    else:
        machine_option=1
    return(machine_option, xi_plus_1)
def player_last_throw_0 (player_option, throw00, throw10): # This function gives us the machine move if the player's last move was 1
    if throw10 > throw00:
        mm=1  # Machine move is equals 1
    elif throw10 < throw00:
        mm=0  # Machine move is equals 0
    else:
        xi=1954
        mm, xi=machine_move(xi) # Machine move is random and we call the linear congruence function (machine_move(xi))
    return(mm)
def player_last_throw_1 (player_option, throw11, throw01): # This function gives us the machine move if the player's last move was 1
    if throw11 > throw01:
        mm=1
    elif throw11 < throw01:
        mm=0
    else:
        xi=2107
        mm, xi=machine_move(xi)
    return(mm)
def counting_throws (throw00, throw01, throw10, throw11): # This function is a counter based in the player's previous decision
    if actual_player_option == 0 and last_player_option == 0:
        throw00 +=1
    elif actual_player_option == 0 and last_player_option == 1:
        throw01 +=1
    elif actual_player_option == 1 and last_player_option == 0:
        throw10 +=1
    elif actual_player_option == 1 and last_player_option == 1:
        throw11 +=1
    else:
        print("The input value is wrong \nThe game finished")
    return(throw00, throw01, throw10, throw11)
def total_score (player_score, machine_score, total_player_score, total_machine_score, tie_games):
    if player_score > machine_score:
        total_player_score += 1
    elif player_score < machine_score:
        total_machine_score +=1
    else:
        tie_games +=1
    return(total_player_score, total_machine_score, tie_games) # This function is to calculate the total games won by each, also to calculate the tied games
xi=1234
player_score=0
machine_score=0
answer='Y'
total_player_score = 0
total_machine_score = 0
tie_games = 0
throw00=0
throw01=0
throw10=0
throw11=0

if option == 1:
    while answer == 'Y':
        player_score=0
        machine_score=0
        xi=1234
        for i in range(moves):
            print("\nROUND ", i+1)
            pm=player_move(i) # pm: player move
            mm, xi=machine_move(xi) # mm: machine move
            print("Player Move: ", pm)
            print("Machine Move: ", mm)
            if pm != mm:
                player_score += 1
                print("Player Wins!!!")
            else:
                machine_score += 1
                print("Machine Wins  :(")
            print("Score: Player: %d  Machine: %d" % (player_score, machine_score))
            print("PLAYER: " + "*"*player_score)
            print("MACHINE: " + "*"*machine_score)  
        if player_score > machine_score:
            print("\nPlayer Wins, Easy Game is Over\nFinal Result\nPlayer: %d - Machine: %d" %(player_score, machine_score))
        else:
            print("\nMachine Wins, Easy Game is Over\nFinal Result\nPlayer: %d - Machine: %d" %(player_score, machine_score))
        answer=input("Do you want to start a new game?\nIf you want to continue playing select Y otherwise select N ").upper()
        total_player_score, total_machine_score, tie_games = total_score(player_score, machine_score, total_player_score, total_machine_score, tie_games)
        print("TOTAL PLAYER WINS: %d" % total_player_score)
        print("TOTAL MACHINE WINS: %d" % total_machine_score)
        print("TOTAL GAMES TIED: %d" % tie_games)  
    else: 
        print("Thanks for playing")
elif option == 2:
    while answer == 'Y':
        player_score=0
        machine_score=0
        actual_player_option=0
        last_player_option=0
        xi=1957
        for i in range(moves):
            print("\nROUND ", i+1)
            mm, xi=machine_move(xi)
            pm=player_move(i)
            actual_player_option = pm # The actual player move is store in this variable
            throw00, throw01, throw10, throw11= counting_throws(throw00, throw01, throw10, throw11)
            if last_player_option == 0:
                mm= player_last_throw_0(actual_player_option, throw00, throw10)
            elif last_player_option == 1:
                mm=player_last_throw_1(actual_player_option, throw11, throw01)
            last_player_option = actual_player_option # This variable is crucial for the loops, because here is where we store the last player move for the next loop
            print("Player Move: ", pm)
            print("Machine Move: ", mm)
            if pm != mm:
                player_score += 1
                print("Player Wins!!!")
            else:
                machine_score += 1
                print("Machine Wins  :(")
            print("Score: Player: %d  Machine: %d" % (player_score, machine_score))
            print("PLAYER: " + "*"*player_score)
            print("MACHINE: " + "*"*machine_score)
        if player_score > machine_score:
            print("\nPlayer Wins, Easy Game is Over\nFinal Result\nPlayer: %d - Machine: %d" %(player_score, machine_score))
        else:
            print("\nMachine Wins, Easy Game is Over\nFinal Result\nPlayer: %d - Machine: %d" %(player_score, machine_score))
        answer=input("Do you want to start a new game?\nIf you want to continue playing select Y otherwise select N ").upper()
        total_player_score, total_machine_score, tie_games = total_score(player_score, machine_score, total_player_score, total_machine_score, tie_games)
        print("TOTAL PLAYER WINS: %d" % total_player_score)
        print("TOTAL MACHINE WINS: %d" % total_machine_score)
        print("TOTAL GAMES TIED: %d" % tie_games)  
    else: 
        print("Thanks for playing")
else:
    print("You couldn't play because you must type 1 or 2")    