print("Student Percentage Calculator")
maths = int(input("Enter Maths marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
english = int(input("Enter English marks: "))
computer = int(input("Enter Computer marks: "))
total = maths + physics + chemistry + english + computer
percentage = (total / 500) * 100
print("----------")
print(f"Total marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print("-----------")