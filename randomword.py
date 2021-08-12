import random

life=3
lost=False
word_list=["apple","bananna","orange"]
word=random.choice(word_list)
print("Guess the word")
#print(word)
word_len=len(word)
blank=[]
for i in range(word_len):
    blank+="_"
print(blank)
blank_count=1
while blank_count !=0:
    guess=input("what is your first letter? ")
    for p in range(word_len):
        letter=word[p]
        if guess==letter:
            blank[p]=letter
        
    print(blank)
    if guess not in word:
        life-=1
        if life==0:
            print("you lost")
            lost=True
            break
        print(f"one life lost remainig life:{life}")
    blank_count=int(blank.count("_"))
if not lost:
    print("you win")

        




    


