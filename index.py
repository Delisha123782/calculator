print("WELCOME TO THE TIP CALCULATOR")
bill=float(input("what was the total bill?$"))
tip=int(input("what percentage tip would you like to give? 10 12 15"))
people=int(input("how many people would you like? "))
tip__as__percent=tip/100
total_bill_amount=bill*tip__as__percent
total_bill=bill+total_bill_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"your total bill is {final_amount}")