name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    if count == 4:
        print("You have 1 seat left.")
    else:
        print("You have {} seats left.".format(MAX_TICKETS - count))

    name = input("Name: ").lower()
    count += 1

    if name == "xxx" :
        print("You sold {} seats and there are {} seats left.".format(count,MAX_TICKETS - count))
    elif name == "xxx" and count == 4:
        print("You sold 4 seats and there is 1 seat left.")
    elif count == MAX_TICKETS:
        print("You have sold every seat!")
