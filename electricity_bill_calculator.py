units = int(input("Enter electricity units: "))
if units <= 100:
     bill: int = units*3
elif units <=200:
    bill: int = units*5
else:
    bill: int = units*8
print(f"Your electricity bill is: {bill}")