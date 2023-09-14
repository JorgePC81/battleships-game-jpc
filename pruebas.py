shots_rec = []
shots_rec.append(1)
shots_rec.append(5)

ship1_size2 = []
ship1_size2.append(1)
ship1_size2.append(2)

i = 0
cad = ""
for x in range(99):
    if x in shots_rec:
        if x in ship1_size2:
            cad = cad + " o "
        else:
            cad = cad + " O "
    else:
        cad = cad + " x "
    i = i + 1
    if i > 9:
        print(cad)
        i = 0
        cad = ""