num = int(input("Enter a no. : "))

if (num ** 0.5).is_integer():
    print(f"{num} is a perfect square of {int(num ** 0.5)}")
else:
    print(f"{num} is not a perfect square.")