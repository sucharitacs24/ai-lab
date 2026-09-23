location = input("Enter location (A/B): ").upper()
status = input("Enter status (Clean/Dirty): ").capitalize()

if status == "Dirty":
    print("Suck")

elif location == "A":
    print("Move Right")

elif location == "B":
    print("Move Left")

else:
    print("Invalid input")
