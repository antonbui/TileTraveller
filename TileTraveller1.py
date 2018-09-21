X = 1
Y = 1
Victory = False
validdirection = "n"
print("You can travel: (N)orth.")


while not Victory:
    direction = input("Direction: ")
    direction = direction.lower()
    if not direction in validdirection:
        print("Not a valid direction!")
    else:
        if direction == "n":
            Y += 1
        elif direction == "s":
            Y -= 1
        elif direction == "w":
            X -= 1
        elif direction == "e":
            X += 1

        if X == 3 and Y == 1:
            Victory = True
            print("Victory!")
        
        else: print("You can travel: ",end="")
        
        if X == 1 and Y == 1:
            validdirection = "n"
            print ("(N)orth.")
        elif X == 1 and Y == 2:
            validdirection = "nes"
            print ("(N)orth or (E)ast or (S)outh.")
        elif X == 1 and Y == 3:
            validdirection = "es"
            print ("(E)ast or (S)outh.")
        elif X == 2 and Y == 1:
            validdirection = "n"
            print ("(N)orth.")
        elif X == 2 and Y == 2:
            validdirection = "sw"
            print ("(S)outh or (W)est.")
        elif X == 2 and Y == 3:
            validdirection = "ew"
            print ("(E)ast or (W)est.")
        elif X == 3 and Y == 2:
            validdirection = "ns"
            print ("(N)orth or (S)outh.")
        elif X == 3 and Y == 3:
            validdirection = "sw"
            print ("(S)outh or (W)est.")