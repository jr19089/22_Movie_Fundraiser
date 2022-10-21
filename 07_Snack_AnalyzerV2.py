import re


def string_check(choice, options):
    chosen = ""

    for var_list in options:

        if choice in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        print()
        return "invalid choice"


def get_snack():

    number_regex = "^[1-9]"

    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&Ms", "m&ms", "mms", "mm", "m", "b"],
        ["pita chips", "chips", "pc", "p chips", "c"],
        ["orange juice", "oj", "o", "j", "juice", "o juice", "d"],
        ["water", "w", "e"]
    ]

    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        desired_snack = input("Snack: ").lower().strip()
        if desired_snack == "xxx":
            return snack_order

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()

        snack_choice = string_check(desired_snack, valid_snacks)
        print("Snack Choice:", snack_choice)

        if amount >= 5:
            print("Sorry, the max snacks is 4.")
            snack_choice = "invalid choice"

        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)


yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Want Snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

if check_snack == "Yes":
    get_order = get_snack()
else:
    get_order = []

print()
if len(get_order) == 0:
    print("Snacks Ordered: None")
else:
    print("Snacks Ordered: ")

    '''for item in snack_order:
        print(item)
        '''

    print(get_order)
