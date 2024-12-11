num = int(input("Enter a no. : "))

if num % 5 == 0 and num % 7 == 0:
    print(f"{num} is a multiple of both 5 and 7")
elif num % 5 == 0:
    print(f"{num} is a multiple of only 5")
elif num % 7 == 0:
    print(f"{num} is a multiple of only 7")
else:
    print(f"{num} is a not multiple of both 5 and 7")
