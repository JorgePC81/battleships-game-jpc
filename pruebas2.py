ship1_size2 = [1]
ship2_size2 = [2]
ship3_size3 = [3]
ship4_size3 = [4]
ship5_size4 = [5]
ship6_size5 = [6]
shots_rec = []
player_ships = ship1_size2 + ship2_size2 + ship3_size3 + ship4_size3 + ship5_size4 + ship6_size5 

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
                        print(ship1_size2)