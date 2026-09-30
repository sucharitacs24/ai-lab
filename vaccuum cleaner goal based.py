location = "A"
status_A = "Dirty"
status_B = "Dirty"

goal = False

while not goal:

   
    if location == "A":
        current_status = status_A
    else:
        current_status = status_B

    
    if current_status == "Dirty":
        action = "Suck"

    elif location == "A" and status_B == "Dirty":
        action = "Move Right"

    elif location == "B" and status_A == "Dirty":
        action = "Move Left"

    else:
        action = "Stop"

    
    if action == "Suck":
        if location == "A":
            status_A = "Clean"
        else:
            status_B = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

   
    if status_A == "Clean" and status_B == "Clean":
        goal = True

    print("Location:", location, "| Action:", action)
    print("Room A:", status_A, "| Room B:", status_B)
    print()

print("GOAL ACHIEVED: Both rooms are clean!")
