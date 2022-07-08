def maak_vierkant(hoogte, breedte, teken):
    for i in range(hoogte):
        for j in range(breedte):
            print(teken, end=" ")
        print()


maak_vierkant(4, 7, "*")
