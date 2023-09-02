def get_shot():
    """enabling the player to enter the shot"""
    
    ok = "n"
    while ok == "n":
        shot = input("please enter your guess: ")
        shot = int(shot)
        if shot < 0 or shot > 99:
            print("incorrect number, try again")
        else:
            ok = 'y'
            break
    return shot
    

def battle_board(hit, miss, comp):

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

hit = [21,22]
miss = [20,24,12,13]
comp = [23] 

shot = get_shot()
battle_board(hit,miss,comp)
        
