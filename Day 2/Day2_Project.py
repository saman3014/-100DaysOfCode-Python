#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip you want to give? 10 or 12 or 15? "))
people = int(input("No of people to split it? "))

tip_percent = tip/100
total_tip_amt = bill * tip_percent
total_bill = bill + total_tip_amt
bill_per_person = total_bill / people

final_amt = round(bill_per_person,2)

print(f"Each person should pay: ${final_amt}")
