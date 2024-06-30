a = int(input("Enter number of numbers: "))
count = 0
maximum = 0
while count < a:
    b = int(input("Enter a number: "))
    if maximum < b:
        maximum = b
    count = count + 1

print("The max of the numbers is ", maximum)
