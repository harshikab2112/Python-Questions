# Write a program to solve this formula: x = ((a+b)/(a-b)) * (c/d) with inputs for a, b, c, and d.

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))

if (a - b) == 0 or d == 0:
    print("Error: Division by zero! Please enter valid values for a, b, and d.")
else:
    x = ((a + b) / (a - b)) * (c / d)
    print(f"Solution is {x:.2f}")
