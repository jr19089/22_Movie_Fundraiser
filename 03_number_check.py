def int_check(question,low_num,high_num):
    error = "Please enter a Whole Number between {} and {}!".format(low_num,high_num)

    Valid = False
    while not Valid:
        try:
            response = int(input(question))
            if response < low_num or response > high_num:
                print(error)
            else:
                Valid = True
                return response
        except ValueError:
            print(error)

age = int_check("Age? ",12,130)
