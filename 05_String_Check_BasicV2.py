def string_checker(question,to_check):

    Valid = False
    while not Valid:
        response = input(question).lower()
        if response in to_check:
            return response
        else:
            print("That is Not a Valid Response.")

snax_want = string_checker("Do You Want Snacks? ",["yes","y","no","n"])
print ("You Answered: ", snax_want)
