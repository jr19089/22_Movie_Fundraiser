def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Name Cannot Be Blank")


#main Routine
name = not_blank("Please Enter Name:")
