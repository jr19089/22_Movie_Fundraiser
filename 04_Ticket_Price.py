name = ""
profit = 0


while name != "xxx":

    name = input("Name: ")

    if name == "xxx":
        break

    age = int(input("Age: "))

    if age >= 12 and age <=15:
        ticket_price = 7.5
    elif age >= 16 and age <=64:
        ticket_price = 10.5
    elif age >= 65:
        ticket_price = 6.5

    profit_made = ticket_price - 5
    profit += profit_made

    print("{} : {:.2f}".format(name,ticket_price))
print("Made {:.2f} profit".format(profit))
