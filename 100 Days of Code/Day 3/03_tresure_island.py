print("Welcome to Tresure Island.\nYour goal is to find the Tresure.")
choice = input("Left or Right?").lower()
if choice == "left":
    choice = input("Swim or Wait?").lower()
    if choice == "wait":
        choice = input("Which door? Red, Blue or Yellow ")
        if choice == "yellow":
            print("You Win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")