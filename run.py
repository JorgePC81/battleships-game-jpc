#variables for the game

ship1_size2 = []
ship2_size2 = []
ship3_size3 = []
ship4_size3 = []
ship5_size4 = []
ship6_size5 = []
player_ships = ship1_size2 + ship2_size2 + ship3_size3 + ship4_size3 + ship5_size4 + ship6_size5
shots_rec = []
FLOW = "stop"



def battle_board(player_ships):
    """
    function where I define the board for the game and what will be the types of shots for 
    the game when they land on water or on the ships.
    """
    

    print("          The Battleships Game\n")   # Title

    # making a numeric diagram
    print ("     0  1  2  3  4  5  6  7  8  9")
    
    shot = 0  
    for x in range(10): 
        row = ""
        for y in range(10):
            sp = " _ "
            if shot not in player_ships:
                sp = " x "
            elif shot in player_ships:
                sp = " o " 
            elif shot in player_ships and len(ship1_size2) == 1 or len(ship2_size2) ==1 or len(ship3_size3) == 2 or len(ship4_size3) == 2 or len(ship5_size4) == 3 or len(ship6_size5) == 4:
                sp = " O " #sank ship
            row = row + sp
            shot = shot + 1
        print(x, " ", row)
        
def ships_choice(player_ships):
    """
    ships_choice is the function where the player builds the ship fleet. 
    """
    
    print("Please, place your ships in the board: vertically or horizontally. They cannot cross or touch each other")
    
    ak = 'y'
    while ak == 'y':
        try:
            ship_choice1 = int(input("ship 1 of two sections: "))
            if ship_choice1 >= 0 and ship_choice1 <= 99:
                ship1_size2.append(ship_choice1)
                if int(len(ship1_size2)) == 2:
                    print("Ship placed. Please, locate the next ship")
                else:
                    ship_choice2 = int(input("complete your ship: "))
                    ship1_size2.append(ship_choice2)
                    if int(len(ship1_size2)) == 2:
                        print("Ship placed. Please, locate the next ship")
                        
                    
        except ValueError:
            print("incorrect entry. Please try again")
            
    
        try:
            ship_choice3 = int(input("ship 2 of two sections: "))
            if ship_choice3 >= 0 and ship_choice3 <= 99:
                ship2_size2.append(ship_choice3)
                ship_choice4_= int(input("complete your ship: "))
                if int(len(ship1_size2)) == 2:
                    print('Ship placed. Please, locate the next ship')
        except ValueError:
            print("incorrect entry. Please try again")
          
        
        try:
            ship_choice5 = int(input("ship 3 of three sections: "))
            if ship_choice5 >= 0 and ship_choice5 <= 99:
                ship3_size3.append(ship_choice5)
                if len(ship3_size3) < 3:
                    ship_choice6 = int(input("complete your ship: "))
                    ship3_size3.append(ship_choice6)
                if int(len(ship3_size3)) < 3:
                    ship_choice7 = int(input("complete your ship: "))
                    if ship_choice7 >= 0 and ship_choice7 <= 99:
                        ship3_size3.append(ship_choice7)
                        if int(len(ship3_size3)) == 3:
                            print('Ship placed. Please, locate the next ship')  
                                
        except ValueError:
            print("incorrect entry. Please try again")

        
        try:
            ship_choice8 = int(input("ship 4 of three sections: "))
            if ship_choice8 >= 0 and ship_choice8 <= 99:
                ship4_size3.append(ship_choice8)
                if int(len(ship4_size3)) < 3:
                    ship_choice9 = int(input("complete your ship: "))
                    ship4_size3.append(ship_choice9)
                if len(ship4_size3) < 3:
                    ship_choice10 = int(input("complete your ship: "))
                    if ship_choice10 >= 0 and ship_choice10 <= 99:
                        ship4_size3.append(ship_choice10)
                    if int(len(ship4_size3)) == 3:
                        print('Ship placed. Please, locate the next ship')
                                    
        except ValueError:
            print("incorrect entry. Please try again")
            
    
        try:
            ship_choice11 = int(input("ship 5 of four sections: "))
            if ship_choice11 >= 0 and ship_choice11 <= 99:
                ship5_size4.append(ship_choice11)
                if int(len(ship5_size4)) < 4:
                    ship_choice12 = int(input("complete your ship: "))
                    ship5_size4.append(ship_choice12)
                if len(ship5_size4) < 4:
                    ship_choice13 = int(input("complete your ship: "))
                    if ship_choice13 >= 0 and ship_choice10 <= 99:
                        ship5_size4.append(ship_choice13)
                if len(ship5_size4) < 4:
                    ship_choice14 = int(input("complete your ship: "))
                    if ship_choice14 >= 0 and ship_choice14 <= 99:
                        ship5_size4.append(ship_choice14)
                    if int(len(ship5_size4)) == 4:
                        print('Ship placed. Please, locate the next ship')
                                    
        except ValueError:
            print("incorrect entry. Please try again")
            
        
        try:
            ship_choice15 = int(input("ship 6 of five sections: "))
            if ship_choice15 >= 0 and ship_choice15 <= 99:
                ship6_size5.append(ship_choice15)
                if int(len(ship6_size5)) < 5:
                    ship_choice16 = int(input("complete your ship: "))
                    ship6_size5.append(ship_choice16)
                if len(ship6_size5) < 5:
                    ship_choice17 = int(input("complete your ship: "))
                    if ship_choice17 >= 0 and ship_choice17 <= 99:
                        ship6_size5.append(ship_choice17)
                if len(ship6_size5) < 5:
                    ship_choice18 = int(input("complete your ship: "))
                    if ship_choice18 >= 0 and ship_choice18 <= 99:
                        ship6_size5.append(ship_choice18)
                if len(ship6_size5) < 5:
                    ship_choice19 = int(input("complete your ship: "))
                    if ship_choice19 >= 0 and ship_choice19 <= 99:
                        ship6_size5.append(ship_choice19)    
                    if int(len(ship6_size5)) == 5:
                       print('ALL YOUR SHIPS ARE ON THE WATER. PREPARE TO SHOT!')
                       print(battle_board(player_ships))
                    break
        except ValueError:
            print("incorrect entry. Please try again")
    

def get_shot(shots_rec, player_ships):
    """enabling the player to enter the shot"""
    
    FLOW = "stop"
    while FLOW == "stop":
        try:
            shot = int(input("please enter your attack: "))
            if shot < 0 or shot > 99:
                print("incorrect entry, try again")
            else:
                shots_rec.append(shot)
                FLOW = "run"
                while FLOW == "run":
                    if shot not in player_ships:
                        sp = " x " #watter
                    elif shot in player_ships:
                        sp = " o " #damage
                        print("You damaged a ship")
                        if len(ship1_size2) == 2 or len(ship2_size2) == 2 or len(ship3_size3) == 3 or len(ship4_size3) == 3 or len(ship5_size4) == 4 or len(ship6_size5) == 5:
                            sp = " O " #sank ship
                            print("Your ship is sank")
                        elif shot in shots_rec:
                            print("you have already shot here")
                            print(battle_board(player_ships))
                        
        except ValueError:
            print ("wrong entry, repeat your shot")
            
battle_board(player_ships) 
ships_choice(player_ships)
get_shot(shots_rec, player_ships)