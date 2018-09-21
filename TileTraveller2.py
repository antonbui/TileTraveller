def message(pos):
    if pos == 1.1:
        validdir = "(N)orth."
    if pos == 1.2:
        validdir = "(N)orth or (E)ast or (S)outh."
    if pos == 1.3:
        validdir = "(E)ast or (S)outh."
    if pos == 2.1:
        validdir = "(N)orth."
    if pos == 2.2:
        validdir = "(S)outh or (W)est."
    if pos == 2.3:
        validdir = "(E)ast or (W)est."
    if pos == 3.1:
        validdir = "(N)orth."
    if pos == 3.2:
        validdir = "(N)orth or (S)outh."
    if pos == 3.3:
        validdir = "(S)outh or (W)est."
    return validdir

position = 1.1
error = False
victory = False

while victory == False:
    if error == True:
        direction = input("Direction: ").lower()
        error = False
    else:
        print("You can travel:", message(position))
        direction = input("Direction: ").lower()
    if direction == "n":
        if position == 1.1 or position == 1.2 or position == 3.2 or position == 2.1:
            position = position + 0.1
        else:
            print("Not a valid direction!")
            error = True
    elif direction == "s":
        if  position == 1.2 or position == 1.3 or position == 2.2 or position == 3.3 or position == 3.2:
            position = position - 0.1
        else:
            print("Not a valid direction!")
            error = True
    elif direction == "w":
        if position == 2.3 or position == 2.2 or position == 3.3:
            position = position - 1
        else:
            print("Not a valid direction!")
            error = True
    elif direction == "e":
        if position == 1.2 or position == 1.3 or position == 2.3:
            position = position + 1
        else:
            print("Not a valid direction!")
            error = True
    else:
        print("Not a valid direction!")
        error = True
    position = round(position, 1)
    if position == 3.1:
        print("Victory!")
        victory = True
