#Set Creation
s1 = {1, 2, 4.9, 'hi', True}
s2 = set((1, 2, 3, 4.8, 'hi', True))
s2.discard(2)
s1.add('bob')
print('1. ', s1)
print('2. ', s2)

#Set Methods
A = {1, 2, 3, 5, 7}
B = {5, 7, 9, 10, 11}
print('3. ', A.union(B))
print('4. ', A.intersection(B))
print('5. ', A.difference(B))
print('6. ', B.difference(A))
print('7. ', A.symmetric_difference(B))
A.intersection_update(B)
print('8. ', A)
B.difference_update(A)
print('9. ', B)
A.symmetric_difference_update(B)
print('10. ', A)

#More Set Methods
s3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s4 = {1, 2, 3, 5, 7}
s5 = {4, 6, 8, 10}
print('11. ', s4.issubset(s3))
print('12. ', s3.issuperset(s5))
print('13. ', s4.isdisjoint(s5))

#Set Operators
s6 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s7 = {1, 2, 3, 5, 7}
s8 = {5, 7, 9, 10, 11}
print('14. ', s7 | s8)
print('15. ', s7 & s8)
print('16. ', s7 - s8)
print('17. ', s7 ^ s8)
print('18. ', s7 < s6)
print('19. ', s7 <= s6)
print('20. ', s6 > s7)
print('21. ', s6 >= s7)
print('22. ', s6 == s7)
print('23. ', s6 != s7)
print('24. ', 10 in s6)
print('25. ', 5 not in s7)

#Adding Elements
s9 = {10, 20, 30, 40, 50}
s9.add(60)
s10 = s9.copy()
s9.update([1, 2, 3])
print('26. ', s9)

#Deleting ELements
s10 = s9.copy()
s10.pop()
s10.discard(40)
s10.remove(50)
s11 = s10.copy()
s11.clear()
print('27. ', s10)
print('28. ', s11)

#Set Comprehension
s12 = {x for x in range(10)}
s13 = {x**2 for x in [-2, -1, 0, 1, 2]}
s14 = {x for x in (10, 8, 7, 9, 20, 12, 6) if x % 2 == 0}
s15 = {x.upper() for x in 'philippines'}
print('29. ', s12)
print('30. ', s13)
print('31. ', s14)
print('32. ', s15)