num=int(input("Enter the no. you want multiplication table of: "))

print(f"\nMultiplication Table of {num}:")

for i in range(1,11):
    table=num*i
    print(f"{num} X {i} = {table}")