height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

int_height=float(height)
int_weight=float(weight)
bmi_result=int_weight/(int_height**2)
print(f"your bmi is: {round(bmi_result)}")