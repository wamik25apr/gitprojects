import random
list=['r','p','s']
ran=random.choice(list)
print(ran)
me=input("please choose between r,p,s ")
if me==ran:
    print('try again')
elif me=="r" and ran=="p":
    print("loose")


