print("Welcome to the tip calculator!")
#receiving the amount of the bill 
bill = float(input("What was the total bill? $ "))
#receiving the percentage of the tip (10, 12, or 15)
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))  
#calculation of the total amount of the bill (amount of the bill + amount of the tipps)
total_bill = bill * (1 + tip/100)
#receiving amount of people 
people = int(input("How many people to split the bill? "))  
# calculation of the amount for each person 
bill_per_person = total_bill / people
# rounding the amount for paying by each person
final_amount = round(bill_per_person,2)
# output
print(f"Each person should pay : $ {final_amount}")
