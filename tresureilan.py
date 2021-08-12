print('welcome to the tresure island.Your mission is to find the tressure')
direction=input("left or right? ")
if direction=="right":
    print('game over')
else:
    swim=input('swim or wait ?')
    if swim=="swim":
        print('game over')
    else:
        door=input('which door?')
        if door in ['red','blue']:
            print('game over')
        else:
            print('you win')


        

