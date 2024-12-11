num = int(input("Enter a no. : "))

if (num % 2 == 0) and (num % 3 == 0):
    print(f"{num} is a multiple of both 2 and 3")
elif num % 2 == 0:
    print(f"{num} is a multiple of only 2")
elif num % 3 == 0:
    print(f"{num} is a multiple of only 3")
else:
    print(f"{num} is a not multiple of both 2 and 3")
