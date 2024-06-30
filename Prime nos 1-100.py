for n in range(1, 100+1):
    count = 0
    for i in range(1, 1+n):
        if n % i == 0:
            count = count + 1
    if count == 2:
        print("Prime number: ", n)
        