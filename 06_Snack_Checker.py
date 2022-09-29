valid_snacks = [
    ["popcorn","p","corn","a"],
    ["M&Ms","m&ms","mms","mm","m", "b"],
    ["pita chips","chips","pc","p chips","c"],
    ["orange juice","oj","o","j","juice","o juice","d"],
    ["water","w","e"]
]

snack_ok = ""
snack = ""

for item in range (0,3):
    desired_snack = input("Snack: ").lower()

    for var_list in valid_snacks:
         if desired_snack in var_list:
             snack = var_list[0].title()
             snack_ok = "yes"
             break
         else:
             snack_ok = "no"

    if snack_ok == "yes":
        print("Snack Choice:",snack)
    else:
        print("invalid choice")
