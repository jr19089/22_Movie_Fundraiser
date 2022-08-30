def not_blank(question,error):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error)


#main Routine
name = not_blank("Please Enter Name:","This Section Cannot Be Blank")
