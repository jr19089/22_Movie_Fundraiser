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


valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "mms", "mm", "m", "b"],
    ["pita chips", "chips", "pc", "p chips", "c"],
    ["orange juice", "oj", "o", "j", "juice", "o juice", "d"],
    ["water", "w", "e"]
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

snack_order = []

check_snack = "invalid choice"

while check_snack == "invalid choice":
    want_snack = input("Want Snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

    if check_snack == "Yes":
        desired_snack = ""
        while desired_snack != "xxx":

            desired_snack = input("Snack: ").lower().strip()
            if desired_snack == "xxx":
                break

            snack_choice = string_check(desired_snack, valid_snacks)
            print("Snack Choice:", snack_choice)

            if snack_choice != "xxx" and snack_choice != "invalid choice":
                snack_order.append(snack_choice)

print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")
else:
    print("Snacks Ordered: ")

    for item in snack_order:
        print(item)
