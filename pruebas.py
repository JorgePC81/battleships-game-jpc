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
        
def ships_choice():
    print("please, place your ships")
    

    input(int("ship 1 of two sections: "))
    input(int("ship 1 of two sections: "))
    input(int("ship 1 of two sections: "))
    input(int("ship 1 of two sections: "))
    input(int("ship 1 of two sections: "))
    input(int("ship 1 of two sections: "))
         
        
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

return shot

def shot_destiny():
hit = []
miss = []
comp = [] 
destiny = hit + miss + comp


battle_board(hit, miss, comp) 

def get_shot()   