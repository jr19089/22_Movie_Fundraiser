def yes_no(question):

    error = "Please Answer Yes or No"

    Valid = False
    while not Valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "Yes"
        elif response == "no" or response == "n":
            return "No"
        else:
            print(error)

snack_want = yes_no("Do you want snacks? ")
print("You answered: ",snack_want)
