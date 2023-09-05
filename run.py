#variables for the game

hit = []
miss = []
comp = [] 
ship1_size2 = []
ship2_size2 = []
ship3_size3 = []
ship4_size3 = []
ship5_size4 = []
ship6_size5 = []




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
    
    ak = 'y'
    while ak == 'y':
        try:
            ship_choice1 = int(input("ship 1 of two sections: "))
            if ship_choice1 >= 0 and ship_choice1 <= 99:
                ship1_size2.append(ship_choice1)
                if len(ship1_size2) == 2:
                    print('Ship placed. Please, locate the next ship')
        except ValueError:
            print("incorrect entry. Please try again")
            break
    
        try:
            ship_choice2 = int(input("ship 2 of two sections: "))
            if ship_choice2 >= 0 and ship_choice2 <= 99:
                ship1_size2.append(ship_choice2)
                if len(ship2_size2) == 2:
                    print('Ship placed. Please, locate the next ship')
        except ValueError:
            print("incorrect entry. Please try again")
            break
        
        try:
            ship_choice3 = int(input("ship 3 of three sections: "))
            if ship_choice3 >= 0 and ship_choice3 <= 99:
                ship1_size2.append(ship_choice3)
                if len(ship3_size3) == 3:
                    print('Ship placed. Please, locate the next ship')
        except ValueError:
            print("incorrect entry. Please try again")
            break
        
        try:
            ship_choice4 = int(input("ship 4 of three sections: "))
            if ship_choice4 >= 0 and ship_choice4 <= 99:
                ship1_size2.append(ship_choice4)
                if len(ship4_size3) == 3:
                    print('Ship placed. Please, locate the next ship')
        except ValueError:
            print("incorrect entry. Please try again")
            break
        
        try:
            ship_choice5 = int(input("ship 5 of five sections: "))
            if ship_choice5 >= 0 and ship_choice5 <= 99:
                ship1_size2.append(ship_choice5)
                if len(ship5_size4) == 4:
                    print('Ship placed. Please, locate the next ship')
        except ValueError:
            print("incorrect entry. Please try again")
            break
        
        try:
            ship_choice6 = int(input("ship 6 of six sections: "))
            if ship_choice6 >= 0 and ship_choice6 <= 99:
                ship1_size2.append(ship_choice6)
                if len(ship6_size5) == 5:
                    print('Ship placed. Please, locate the next ship')
        except ValueError:
            print("incorrect entry. Please try again")
            break
    
        
         
def get_shot():
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
    


#battle_board(hit, miss, comp) 
#get_shot()
ships_choice()
