num = int(input("Enter a Nth number you want sum of numbers to: "))
sum=0
for i in range(1, num+1): 
    sum += i
print(f"Sum of numbers from 1 to {num} is : {sum}")
