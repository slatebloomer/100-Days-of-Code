print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
percentage = input("What percentage tip would you like to give? ")
if "%" in percentage:
    percentage = percentage.replace("%", " ")
percentage = int(percentage)
guests = int(input("How many people are splitting the bill? "))
per_person = format((bill * (percentage / 100)) / guests, ".2f")
print(f"Each person should pay £{per_person}")
