num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))
num3 = float(input("Enter the num3: "))

if (num1 >= num2) and (num1 >= num3):
    print(f"{num1} is largest of all three.")
elif (num2 >= num1) and (num2 >= num3):
    print(f"{num2} is largest of all three.")
else:
    print(f"{num3} is largest of all three.")
