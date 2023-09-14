#variables for the game

ship1_size2 = []
ship2_size2 = []
ship3_size3 = []
ship4_size3 = []
ship5_size4 = []
ship6_size5 = []
FLOW = "stop"
shots_rec = []
x = []
y = []



def battle_board():
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
            if shot not in ship1_size2 and shot not in ship2_size2 and shot not in ship3_size3 and shot not in ship4_size3 and shot not in ship5_size4 and shot not in ship6_size5:
                sp = " x "
            elif shot in ship1_size2 or shot in ship2_size2 or shot in ship3_size3 or shot in ship4_size3 or shot in ship5_size4 or shot in ship6_size5:
                sp = "o"
                if len(ship1_size2) == 2 or len(ship2_size2) ==2 or len(ship3_size3) == 3 or len(ship4_size3) == 3 or len(ship5_size4) == 4 or len(ship6_size5) == 5:
                    sp = " O " #sank ship
                    
            row = row + sp
            shot = shot + 1
        print(x, " ", row)
        
def ships_choice():
    """
    ships_choice is the function where the player builds the ship fleet. 
    """
    
    print("Please, place your ships in the board: vertically or horizontally. They cannot cross or touch each other")
    
    ak = 'y'
    while ak == 'y':
        try:
            ship_choice1 = input("ship 1, section 1. Coordenates X, Y (I.E: 3, 5): ")
            if ship_choice1 >= 0 and ship_choice1 <= 9:
                ship1_size2.append(ship_choice1)
                if int(len(ship1_size2)) < 2:
                    ship_choice2 = input("ship 1, section 2. Coordenates X, Y (I.E: 3, 5): ")
                    ship1_size2.append(ship_choice2)
                    if int(len(ship1_size2)) == 2:
                        print("Ship placed. Please, locate the next ship")
                        
                    
        except ValueError:
            print("incorrect entry. Please try again")
            
    
        try:
            ship_choice3 = input("ship 2, section 1. Coordenates X, Y (I.E: 3, 5): ")
            ship2_size2.append(ship_choice3)
            ship_choice4 = input("ship 2, section 2. Coordenates X, Y (I.E: 3, 5): ")
            ship2_size2.append(ship_choice4)
            if int(len(ship1_size2)) == 2:
                print('Ship placed. Please, locate the next ship')
        except ValueError:
            print("incorrect entry. Please try again")
          
        
        try:
            ship_choice5 = input("ship 3, section 1. Coordenates X, Y (I.E: 3, 5): ")
            if ship_choice5 >= 0 and ship_choice5 <= 9:
                ship3_size3.append(ship_choice5)
                if len(ship3_size3) < 3:
                    ship_choice6 = input("ship 3, section 2. Coordenates X, Y (I.E: 3, 5): ")
                    ship3_size3.append(ship_choice6)
                if int(len(ship3_size3)) < 3:
                    ship_choice7 = input("ship 3, section 3. Coordenates X, Y (I.E: 3, 5): ")
                    if ship_choice7 >= 0 and ship_choice7 <= 9:
                        ship3_size3.append(ship_choice7)
                        if int(len(ship3_size3)) == 3:
                            print('Ship placed. Please, locate the next ship')  
                                
        except ValueError:
            print("incorrect entry. Please try again")

        
        try:
            ship_choice8 = input("ship 4, section 1. Coordenates X, Y (I.E: 3, 5): ")
            if ship_choice8 >= 0 and ship_choice8 <= 9:
                ship4_size3.append(ship_choice8)
                if int(len(ship4_size3)) < 3:
                    ship_choice9 = input("ship 4, section 2. Coordenates X, Y (I.E: 3, 5): ")
                    ship4_size3.append(ship_choice9)
                if len(ship4_size3) < 3:
                    ship_choice10 = input("ship 4, section 3. Coordenates X, Y (I.E: 3, 5): ")
                    if ship_choice10 >= 0 and ship_choice10 <= 9:
                        ship4_size3.append(ship_choice10)
                    if int(len(ship4_size3)) == 3:
                        print('Ship placed. Please, locate the next ship')
                                    
        except ValueError:
            print("incorrect entry. Please try again")
            
    
        try:
            ship_choice11 = input("ship 5, section 1. Coordenates X, Y (I.E: 3, 5): ")
            if ship_choice11 >= 0 and ship_choice11 <= 9:
                ship5_size4.append(ship_choice11)
                if int(len(ship5_size4)) < 4:
                    ship_choice12 = input("ship 5, section 2. Coordenates X, Y (I.E: 3, 5): ")
                    ship5_size4.append(ship_choice12)
                if len(ship5_size4) < 4:
                    ship_choice13 = input("ship 5, section 3. Coordenates X, Y (I.E: 3, 5): ")
                    if ship_choice13 >= 0 and ship_choice10 <= 9:
                        ship5_size4.append(ship_choice13)
                if len(ship5_size4) < 4:
                    ship_choice14 = input("ship 5, section 4. Coordenates X, Y (I.E: 3, 5): ")
                    if ship_choice14 >= 0 and ship_choice14 <= 9:
                        ship5_size4.append(ship_choice14)
                    if int(len(ship5_size4)) == 4:
                        print('Ship placed. Please, locate the next ship')
                                    
        except ValueError:
            print("incorrect entry. Please try again")
            
        
        try:
            ship_choice15 = input("ship 6, section 1. Coordenates X, Y (I.E: 3, 5): ")
            if ship_choice15 >= 0 and ship_choice15 <= 9:
                ship6_size5.append(ship_choice15)
                if int(len(ship6_size5)) < 5:
                    ship_choice16 = input("ship 6, section 2. Coordenates X, Y (I.E: 3, 5): ")
                    ship6_size5.append(ship_choice16)
                if len(ship6_size5) < 5:
                    ship_choice17 = input("ship 6, section 3. Coordenates X, Y (I.E: 3, 5): ")
                    if ship_choice17 >= 0 and ship_choice17 <= 9:
                        ship6_size5.append(ship_choice17)
                if len(ship6_size5) < 5:
                    ship_choice18 = input("ship 6, section 4. Coordenates X, Y (I.E: 3, 5): ")
                    if ship_choice18 >= 0 and ship_choice18 <= 9:
                        ship6_size5.append(ship_choice18)
                if len(ship6_size5) < 5:
                    ship_choice19 = input("ship 6, section 5. Coordenates X, Y (I.E: 3, 5): ")
                    if ship_choice19 >= 0 and ship_choice19 <= 9:
                        ship6_size5.append(ship_choice19)    
                    if int(len(ship6_size5)) == 5:
                       print('ALL YOUR SHIPS ARE ON THE WATER. PREPARE TO SHOT!')
                       print(battle_board)
                    break
        except ValueError:
            print("incorrect entry. Please try again")
    

def get_shot():
    """enabling the player to enter the shot"""
    
    FLOW = "stop"
    while FLOW == "stop":
        try:
            shot = input("please enter your attack: "))
            if shot < 0 or shot > 9:
                print("incorrect entry, try again")
            else:
                shots_rec.append(shot)
                FLOW = "run"
                while FLOW == "run":
                    if shot not in ship1_size2:
                        sp = " x " #watter
                    else:
                        sp = " o "
                    #elif shot in ship1_size2 and len(ship1_size2) == 1 or len(ship2_size2) ==1 or len(ship3_size3) == 2 or len(ship4_size3) == 2 or len(ship5_size4) == 3 or len(ship6_size5) == 4:
                        #sp = " o " #damage
                        print("You damaged a ship")
                        #if len(ship1_size2) == 2 or len(ship2_size2) == 2 or len(ship3_size3) == 3 or len(ship4_size3) == 3 or len(ship5_size4) == 4 or len(ship6_size5) == 5:
                            #sp = " O " #sank ship
                            #print("Your ship is sank")
                        #elif shot in shots_rec:
                            #print("you have already shot here")
                            #print(battle_board)
                        
        except ValueError:
            print ("wrong entry, repeat your shot")
            
battle_board() 
ships_choice()
get_shot()