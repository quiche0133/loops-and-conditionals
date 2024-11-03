tempinput = input("Is your object small? (y or n) ")
if tempinput == "y":
    small = True
if tempinput == "n":
    small = False
tempinput = input("Is your object green? (y or n) ")
if tempinput == "y":
    green = True
if tempinput == "n":
    green = False
if small:
    if green:
        print("Your object is a pea.")
    else:
        print("Your object is a cherry.")
else:
    if green:
        print("Your object is a watermelon.")
    else:
        print("Your object is a pumpkin.")