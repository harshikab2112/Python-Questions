n = int(input("Enter the Nth no. you want average of: "))

sum=0

for i in range(1,n+1):
    sum+=i
avg=sum/n
print(f"Average of numbers from 1 to {n} is {avg}")