#variables for the game

ship1_size2 = []
ship2_size2 = []
ship3_size3 = []
ship4_size3 = []
ship5_size4 = []
ship6_size5 = []
FLOW = "stop"
shots_rec = []


print("Welcome to the Battleship game. You will have to place your ships in the board and then shot to the enemy ships. The first player to sink all the enemy ships wins the game. Good luck!")


def battle_board():
    """
    function where I define how the board for the game will look like
    """
i = 0
cad = ""
for x in range(100):
    if x in shots_rec:
        if x in ship1_size2 or x in ship2_size2 or x in ship3_size3 or x in ship4_size3 or x in ship5_size4 or x in ship6_size5:
            cad = cad + " o "
            if len(ship1_size2) == 2 or len(ship2_size2) == 2 or len(ship3_size3) == 3 or len(ship4_size3) == 3 or len(ship5_size4) == 4 or len(ship6_size5) == 5:
                cad = cad + " O "
    else:
        cad = cad + " x "
    i = i + 1
    if i > 9:
        print(cad)
        i = 0
        cad = ""
    
        
def ships_choice():
    """
    ships_choice is the function where the player builds the ship fleet. 
    """
    
    print("Please, place your ships in the board: vertically or horizontally. They cannot cross or touch each other")
    
    ak = 'y'
    while ak == 'y':
        try:
            ship_choice1 = int(input("ship 1, Section 1: "))
            if ship_choice1 >= 0 and ship_choice1 <= 99:
                ship1_size2.append(ship_choice1)
            if int(len(ship1_size2)) < 2:
                ship_choice2 = int(input("ship 1, section 2: "))
                if ship_choice2 >= 0 and ship_choice2 <= 99:
                    ship1_size2.append(ship_choice2)
                if int(len(ship1_size2)) == 2:
                    print("Ship placed. Please, locate the next ship")
                        
                    
        except ValueError:
            print("incorrect entry. Please try again")
            
    
        try:
            ship_choice3 = int(input("ship 2, section 1: "))
            if ship_choice3 >= 0 and ship_choice3 <= 99:
                ship2_size2.append(ship_choice3)
            ship_choice4 = int(input("ship 2, section 2: "))
            if ship_choice4 >= 0 and ship_choice4 <= 99:
                ship2_size2.append(ship_choice4)
            if int(len(ship1_size2)) == 2:
                print('Ship placed. Please, locate the next ship')
        except ValueError:
            print("incorrect entry. Please try again")
          
        
        try:
            ship_choice5 = int(input("ship 3, section 1: "))
            if ship_choice5 >= 0 and ship_choice5 <= 99:
                ship3_size3.append(ship_choice5)
            if int(len(ship3_size3)) < 3:
                ship_choice6 = int(input("ship 3, section 2: "))
                if ship_choice6 >= 0 and ship_choice6 <= 99:
                    ship3_size3.append(ship_choice6)
            if int(len(ship3_size3)) < 3:
                ship_choice7 = int(input("ship 3, section 3: "))
                if ship_choice7 >= 0 and ship_choice7 <= 99:
                    ship3_size3.append(ship_choice7)
                if int(len(ship3_size3)) == 3:
                    print('Ship placed. Please, locate the next ship')  
                                
        except ValueError:
            print("incorrect entry. Please try again")

        
        try:
            ship_choice8 = int(input("ship 4, section 1: "))
            if ship_choice8 >= 0 and ship_choice8 <= 99:
                ship4_size3.append(ship_choice8)
            if int(len(ship4_size3)) < 3:
                ship_choice9 = int(input("ship 4, section 2: "))
                if ship_choice9 >= 0 and ship_choice9 <= 99:
                    ship4_size3.append(ship_choice9)
                if len(ship4_size3) < 3:
                    ship_choice10 = int(input("ship 4, section 3: "))
                    if ship_choice10 >= 0 and ship_choice10 <= 99:
                        ship4_size3.append(ship_choice10)
                    if int(len(ship4_size3)) == 3:
                        print('Ship placed. Please, locate the next ship')
                                    
        except ValueError:
            print("incorrect entry. Please try again")
            
    
        try:
            ship_choice11 = int(input("ship 5, section 1. "))
            if ship_choice11 >= 0 and ship_choice11 <= 99:
                ship5_size4.append(ship_choice11)
            if int(len(ship5_size4)) < 4:
                ship_choice12 = int(input("ship 5, section 2: "))
                if ship_choice12 >= 0 and ship_choice12 <= 99:
                    ship5_size4.append(ship_choice12)
                if len(ship5_size4) < 4:
                    ship_choice13 = int(input("ship 5, section 3: "))
                    if ship_choice13 >= 0 and ship_choice13 <= 99:
                        ship5_size4.append(ship_choice13)
                if len(ship5_size4) < 4:
                    ship_choice14 = int(input("ship 5, section 4: "))
                    if ship_choice14 >= 0 and ship_choice14 <= 99:
                        ship5_size4.append(ship_choice14)
                    if int(len(ship5_size4)) == 4:
                        print('Ship placed. Please, locate the next ship')
                                    
        except ValueError:
            print("incorrect entry. Please try again")
            
        
        try:
            ship_choice15 = int(input("ship 6, section 1: "))
            if ship_choice15 >= 0 and ship_choice15 <= 99:
                ship6_size5.append(ship_choice15)
            if int(len(ship6_size5)) < 5:
                ship_choice16 = int(input("ship 6, section 2: "))
                if ship_choice16 >= 0 and ship_choice16 <= 99:
                    ship6_size5.append(ship_choice16)
                if len(ship6_size5) < 5:
                    ship_choice17 = int(input("ship 6, section 3: "))
                    if ship_choice17 >= 0 and ship_choice17 <= 99:
                        ship6_size5.append(ship_choice17)
                if len(ship6_size5) < 5:
                    ship_choice18 = int(input("ship 6, section 4: "))
                    if ship_choice18 >= 0 and ship_choice18 <= 99:
                        ship6_size5.append(ship_choice18)
                if len(ship6_size5) < 5:
                    ship_choice19 = int(input("ship 6, section 5: "))
                    if ship_choice19 >= 0 and ship_choice19 <= 99:
                        ship6_size5.append(ship_choice19)    
                    if int(len(ship6_size5)) == 5:
                       print('ALL YOUR SHIPS ARE ON THE WATER. PREPARE TO BATTLE!')
                       battle_board()
                    break
        except ValueError:
            print("incorrect entry. Please try again")
            
    

def get_shot():
    """enabling the player to enter the shot"""
    
    FLOW = "stop"
    while FLOW == "stop":
        try:
            shot = int(input("enemy shoots: "))
            shots_rec.append(shot)
            if shot not in ship1_size2 and shot not in ship2_size2 and shot not in ship3_size3 and shot not in ship4_size3 and shot not in ship5_size4 and shot not in ship6_size5:
                print ("Your enemy missed")
            else:
                if sank_check_ship1() == True:
                    print("Your ship 1 is sank")
                elif shot in ship1_size2:
                    print("Your enemy damaged one of your ships")
                if sank_check_ship2() == True:
                    print("Your ship 2 is sank")
                elif shot in ship2_size2:
                    print("Your enemy damaged one of your ships")
                if sank_check_ship3() == True:
                    print("Your ship 3 is sank")
                elif shot in ship3_size3:
                    print("Your enemy damaged one of your ships")
                if sank_check_ship4() == True:
                    print("Your ship 4 is sank")
                elif shot in ship4_size3:
                    print("Your enemy damaged one of your ships")
                if sank_check_ship5() == True:
                    print("Your ship 5 is sank")
                elif shot in ship5_size4:
                    print("Your enemy damaged one of your ships")
                if sank_check_ship6() == True:
                    print("Your ship 6 is sank")
                elif shot in ship6_size5:
                    print("Your enemy damaged one of your ships")
                end_game()
 
        except ValueError:
            print ("wrong entry, repeat your shot")
            battle_board()
            
def sank_check_ship1():
    for i in ship1_size2:
        if i not in shots_rec:
            return False
    return True

def sank_check_ship2():
    for i in ship2_size2:
        if i not in shots_rec:
            return False
    return True

def sank_check_ship3():
    for i in ship3_size3:
        if i not in shots_rec:
            return False
    return True

def sank_check_ship4():
    for i in ship4_size3:
        if i not in shots_rec:
            return False
    return True

def sank_check_ship5():
    for i in ship5_size4:
        if i not in shots_rec:
            return False
    return True

def sank_check_ship6():
    for i in ship6_size5:
        if i not in shots_rec:
            return False
    return True

def end_game():
    if sank_check_ship1() == True and sank_check_ship2() == True and sank_check_ship3() == True and sank_check_ship4() == True and sank_check_ship5() == True and sank_check_ship6() == True:
        print("YOUR ENEMY WON THE BATTLE")
        print("GAME OVER")
            
battle_board() 
ships_choice()
get_shot()
sank_check_ship1()
sank_check_ship2()
sank_check_ship3()
sank_check_ship4()
sank_check_ship5()
sank_check_ship6()
end_game()