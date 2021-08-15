import random
from hangman_art import logo,stages
from hangman_word import word_list
print(logo)

life = 6
lost = False
word = random.choice(word_list)

print("Guess the word")
# print(word)
word_len = len(word)
blank = []
input_letter=[]

for i in range(word_len):
    blank += "_"
print(blank)
blank_count = 1
while blank_count != 0:
    guess = input("what is your  letter? ")
    if guess in input_letter:
        print("letter already used please choose different letter")
    else:
        input_letter.append(guess)
        for p in range(word_len):
            letter = word[p]
            if guess == letter:
                blank[p] = letter

        print(blank)
        if guess not in word:
            life -= 1
            if life == 0:
                print(stages[life])
                print("you lost")
                print(word)
                lost = True
                break
            print(f"one life lost {stages[life]}")
        blank_count = int(blank.count("_"))
if not lost:
    print("you win")



















