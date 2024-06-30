a = int(input("Enter a number: "))
count = 0
while a > 0:
    a = a // 10
    count = count + 1

print("Number of digits are: ", count)