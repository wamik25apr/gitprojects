import string
thelist = list(string.ascii_lowercase)
result_index=[]
shift_index=[]
word1=""
def encode_decode(word,shift,direction):
    for i in word:
        result_index.append(thelist.index(i))
    if direction=="dcode":
        shift=-shift
    elif direction=="encode":
        shift=shift
    else:
        print("choose encode or dcode")
    for j in result_index:
        print(j+shift)
        if direction=="encode" and j+shift==len(thelist)-shift:
            j=-1
            print(j+shift)
        print(thelist[j+shift],end="")
        
    
    
        

input_word=input("Please enter the word: ")         
input_shift=int(input("shift number: "))
enordcode=input("encode or dcode? ")
encode_decode(input_word,input_shift,enordcode)

    

        


