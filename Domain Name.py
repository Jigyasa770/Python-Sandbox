email = input("Enter your email address: ")
atrate = email.find('@')
userid = email[:atrate]
domain_name = email[atrate+1:]
print(userid, domain_name)
