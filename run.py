#variables for the game

hit = []
miss = []
comp = [] 
ship1_size2 = []
ship2_size2 = []
ship3_size3 = []
ship3_size3 = []
ship4_size4 = []
ship5_size5 = []
ship_choice = list(range(100))


def battle_board(hit, miss, comp):
    """
    function where I define the board for the game and what will be the types of shots for 
    the game when they land on water or on the ships.
    """
    

    print("          The Battleships Game\n")   # Title

    # making a numeric diagram
    print ("     0  1  2  3  4  5  6  7  8  9")
     
    place = 0  
    for x in range(10): 
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "
                
            row = row + ch
            place = place + 1
        print(x, " ", row)
        
def ships_choice():
    """
    ships_choice is the function where the player builds the ship fleet. 
    """
    
    print("please, place your ships in the board: vertically or horizontally")
    
    ak = y:
    while ak == y:
        try:
            input(int("ship 1 of two sections: " ,ship_choice))
            if ship_choice >= 0 and ship_choice <= 99:
                ship_choice.append(ship1_size2)
                if ship1_size2(len) > 2:
                     print("Wrong ship size. Please try again")
                except ValueError:
                    print("incorrect entry. Please try again")
                    break
    

    input(int("ship 2 of two sections: " ,ship2_size2))
    if ship_choice >= 0 and ship_choice <= 99:
        ship_choice.append(ship2_size2)
    else:
        print("incorrect entry. Please try again")
    break
        
    input(int("ship 3 of three sections: " ,ship3_size3))
    if ship_choice >= 0 and ship_choice <= 99:
        ship_choice.append(ship3_size2)
    else:
        print("incorrect entry. Please try again")
    break
        
    input(int("ship 4 of three sections: " ,ship3_size3))
    if ship_choice >= 0 and ship_choice <= 99:
        ship_choice.append(ship4_size2)
    else:
        print("incorrect entry. Please try again")
    break
        
    input(int("ship 5 of four sections: " ,ship4_size4))
    if ship_choice >= 0 and ship_choice <= 99:
        ship_choice.append(ship5_size2)
    else:
        print("incorrect entry. Please try again")
    break
        
    input(int("ship 6 of five sections: " ,ship5_size5))
    if ship_choice >= 0 and ship_choice <= 99:
        ship_choice.append(ship6_size2)
    else:
        print("incorrect entry. Please try again")
    break
        
         
def get_shot(destiny):
    """enabling the player to enter the shot"""

ok = "n"
while ok == "n":
    try:
        shot = input("please enter your guess: ")
        shot = int(shot)
        if shot < 0 or shot > 99:
            print("incorrect number, try again")
        else:
            ok = 'y'
            if shot in hit or shot in miss or shot in comp:
                print("you have already guessed that, try again")
                ok = 'n'
            break
    except ValueError:
        print ("incorrect entry, try again")

def shot_destiny():
    destiny = hit + miss + comp
    
    


battle_board(hit, miss, comp) 
get_shot()  
ships_choice() 