n = int(input("Enter the number of terms: "))
a = int(input("Enter the initial term: "))
d = int(input("Enter the common difference: "))

for t in range(a, a + n * d, d):
    print("The AP series is: ", t)