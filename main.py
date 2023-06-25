print("Welcome to the tip calculator.")
bill_total = float(input("What was the total bill? $"))
tip_input = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_percent = (float(tip_input) * .01) + 1
bill_plus_tip = bill_total * tip_percent
bill_per_person = round(bill_plus_tip / num_people, 2)
print(f"Each person should pay: ${bill_per_person}")