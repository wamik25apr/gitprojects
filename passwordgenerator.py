import random
import string

a=[]
p=''
number=int(input('how many number do you want in your password ?'))
for i in range(number):
    a.append(str(random.randrange(0,9,1)))
letter=int(input('how many letter do you want in your password ?'))
for i in range(letter):
    a.append(random.choice(string.ascii_letters))
for i in a:
    p +=i
print(p)
