import os
from art import logo
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
a={}
next_bidder="yes"
print(logo)
print("Welcome to the secret auction program")
while next_bidder=="yes":
    name=input("What is your name? ")
    bid=input("what is your bid? ")
    a[name]=bid
    next_bidder=input("are there any other bidders? ")
    screen_clear()
    print(logo)
 
b=list(a.values())
b.sort()
highest_bid=b[-1]
highest_bid_index=list(a.values()).index(highest_bid)
highest_bid_value=list(a.keys())[highest_bid_index]

print(f"The winner is {highest_bid_value} with a bid of {highest_bid}")

