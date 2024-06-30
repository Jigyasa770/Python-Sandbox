from re import *
s2 = match('[a-zA-z0-9]+', 'ABCEH').group()
s3 = match('[a-z]+', 'python').group()
s4 = match('[^a-z]+', 'A-23+@').group()
s5 = match('[a-zA-z0-9]+', 'ABCEH').group()
s6 = match('([a-z]+)| ([A-z]+)', 'abc').group()

print(s2, s3, s4, s5, s6)
