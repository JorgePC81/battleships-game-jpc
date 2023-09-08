
ship1_size2 = []
ship2_size2 = []
ship3_size3 = []
ship4_size3 = []
ship5_size4 = []
ship6_size5 = []

progress = "stop"
while progress == "stop":
    try:
        shot = input("please enter your attack: ")
        shot = int(shot)
        if shot < 0 or shot > 99 or shot == shot:
            print("incorrect number, try again")
        else:
            progress = "run"
            if shot not in ship1_size2 or shot not in ship2_size2 or shot not in ship3_size3 or shot not in ship4_size3 or shot not in ship5_size4 or shot not in ship6_size5:
                sp = " x "
            elif shot in ship1_size2 or shot in ship2_size2 or shot in ship3_size3 or shot in ship4_size3 or shot in ship5_size4 or shot in ship6_size5:
                sp = " o "
                if:
                    len(ship1_size2) == 1 or len(ship2_size2) ==1 or len(ship3_size3) == 2 or len(ship4_size3) == 2 or len(ship5_size4) == 3 or len(ship6_size5) == 4:
                    sp = " O "
                    print("Your ship is sank")
                    progress = 'run'
                break
    except ValueError:
        print ("wrong entry, repeat your shot")
         
          
            