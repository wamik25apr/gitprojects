print('Welcome to the tip calculator')
total_bill=float(input(f'what was the total bill? $'))
split=int(input(f'How many people to split the bill? '))
each=total_bill/split
tip_chose=int(input(f'what percentage of tip you wan to give? 10,12, or 15? '))

if tip_chose not in [10,12,15]:
    print('please choose proper tip')
else:
    tip=((total_bill*tip_chose)/100)/split
    print(f'Each person shoud pay: ${round(each+tip,2)}')

