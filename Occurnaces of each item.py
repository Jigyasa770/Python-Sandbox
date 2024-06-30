L1 = ['A', 'B', 'D', 'E', 'A', 'B', 'E', 'B', 'D', 'B', 'E']

result = []

for item in L1:
    if item not in result:
        result.append(item)
        count = L1.count(item)
        result.append(count)

print(result)