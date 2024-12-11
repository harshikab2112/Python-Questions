num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not prime no.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime no.")
            break
    else:
        print(f"{num} is prime no.")
