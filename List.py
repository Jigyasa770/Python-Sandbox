#List Creation
mylist = [1, 2, 3, 4, 5]
mylist1 = list((1, 2, 3, 4, 5))
mylist2 = list((1, 'hello', True, 5+7j))
print('1. ', mylist, mylist1, mylist2)

#Mutable List
mylist3 = [1, 2, 3, 4, 5, 621]
mylist3[2] = 213
mylist3.append(20)
print('2. ', mylist3)

#Index and Slice Operators in List
mylist4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist4[3] = 12
mylist4[0:3] = [10, 20, 30]
print('3. ', mylist4[1], mylist4, mylist4[0:10:2], mylist4[-1:-11:-1])

# Concatenation and Repetition Operators in List
mylist5 = [1, 2, 3]
mylist6 = [8, 9, 10]
mylist5.extend([4,5,6,7])
mylist7 = mylist5 + [45]
mylist8 = mylist6 * 8
print('4. ', mylist5, mylist5 + mylist6, mylist7, mylist8)

#In Operator
mylist9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 4 in mylist9:
    print('5. ', 'Present')

#Not In Operator
mylist10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 44 not in mylist10:
    print('6. ', 'Absent')

#Iterating a list
mylist11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in mylist11:
    print('7. ', x)
for i in range(len(mylist11)):
    print('8. ', mylist11[i])
for u in range(len(mylist11)-1, -1, -1):
    print('9. ', mylist11[u])
y = 0
while y<len(mylist11):
    print('10. ', mylist11[y])
    y = y + 1

#Adding elements to list methods
mylist12 = [5, 6, 7, 8, 9]
mylist12.append(10)
mylist12[6:6] = [11]
mylist12.extend([12, 13, 14, 15])
mylist12.insert(11,20)
mylist13 = mylist12.copy()
print('11. ', mylist12, mylist13)

#Removing Elements from list
mylist14 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
mylist15 = [1, 2, 3, 4, 5]
mylist16 = [10, 20, 30, 40, 50]
mylist14.pop()
mylist15.pop(4)
del mylist15[1]
mylist14.remove(7)
mylist16.clear()
print('12. ', mylist14)
print('13. ', mylist15)
print('14. ', mylist16)

#Indexing and Sorting Methods
mylist17 = [5, 6, 7, 8, 7, 17, 10, 12, 13]
mylist18 = [1, 2, 3, 4, 5]
mylist19 = [10, 20, 30, 40, 50]
mylist18.sort()
mylist17.reverse()
mylist19.sort(reverse=True)
print('15. ', mylist17.index(7), mylist17.index(7,3), mylist17.index(7,2,5), mylist17.count(7), mylist17, mylist18, mylist19)

#List Comprehension
L1 = [x for x in range(10)]
L2 = [x**2 for x in range(1,6)]
L3 = [x for x in(10,5,7,8,12,3) if x%2==0]
L4 = [x.lower() for x in 'Python']
L5 = [x for x in 'ab12de-&fg4$hi2' if x.isalpha()]
print('16. ', L1, L2, L3, L4, L5)

#Nested List
L6 = [10, 20, ['a', 'b', [29, 45]], 30, 40]
L7 =[[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
L8 =[[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
print('17. ', L6[0], L6[2][0], L6[2][2][0])
C = []
for i in range(len(L7)):
    S =[]
    for j in range(len(L7[0])):
        S.append(L7[i][j] + L8[i][j])
    C.append((S))
print('18. ', C)



