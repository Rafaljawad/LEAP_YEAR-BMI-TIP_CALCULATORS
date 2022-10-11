bill = float(input("what was the total bill?: $"))
percentage=float(input("what percentage you choose 10,12,15?:"))
split_people=int(input("How many people to split the bill among?"))
result=(bill*percentage/100)+bill
bill_for_each_customer=round(result/split_people,2)
print(bill_for_each_customer)