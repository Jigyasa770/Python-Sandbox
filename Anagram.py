s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')
if len(s1) != len(s2):
    print("Not anagram")
else:
    for x in s1:
        if x not in s2:
            print('Not Anagram')
    else:
        print('Anagram')