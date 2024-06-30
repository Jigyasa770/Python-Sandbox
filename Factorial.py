n = int(input("Enter a number: "))
fact = 1
for count in range(1, n+1):
    fact = fact * count

print("The factorial is ", fact)