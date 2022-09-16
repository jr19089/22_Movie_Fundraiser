def not_blank(question,error):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error)
def int_check(question):
    error = "Please enter a Whole Number"

    Valid = False
    while not Valid:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)


name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    if count == 4:
        print("You have 1 seat left.")
    else:
        print("You have {} seats left.".format(MAX_TICKETS - count))

    name = not_blank("Name? ","This cannot be blank").lower()

    if name == "xxx":
        print("You sold {} seats and there are {} seats left.".format(count,MAX_TICKETS - count))
    elif name == "xxx" and count == 4:
        print("You sold 4 seats and there is 1 seat left.")
    elif count == MAX_TICKETS:
        print("You have sold every seat!")

    age = int_check("Age? ")
    if age < 12:
        print("You are too young for this movie")
        continue
    elif age > 130:
        print("This is too old. There must be a mistake.")
        continue

    count += 1
