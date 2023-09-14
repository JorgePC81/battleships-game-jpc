ship1_size2 = [1]
ship2_size2 = [2]
ship3_size3 = [3]
ship4_size3 = [4]
ship5_size4 = [5]
ship6_size5 = [6]
shots_rec = []


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
            sp = " o "
            if len(ship1_size2) == 2 or len(ship2_size2) ==2 or len(ship3_size3) == 3 or len(ship4_size3) == 3 or len(ship5_size4) == 4 or len(ship6_size5) == 5:
                sp = " O " #sank ship
                    
        row = row + sp
        shot = shot + 1
    print(x, " ", row)
         
        