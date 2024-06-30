a = int(input("Enter number: "))
count = 0
for i in range(1, a+1):
    if a % i == 0:
        count += i

if count == 2:
    print("Prime")
else:
    print("Not Prime")
