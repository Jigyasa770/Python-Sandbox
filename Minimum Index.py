fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']
ind1 = 10
ind2 = 20
for i in range(len(fav1)):
        indx = fav2.index(fav1[i])

        if i + indx < ind1 + ind2:
            ind1 = i
            ind2 = indx

print(fav1[ind1],ind1 + ind2)
