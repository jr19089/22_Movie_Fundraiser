name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    name = input("Name: ")
    count += 1
if count == 5:
    print("All Tickets have been sold.")
