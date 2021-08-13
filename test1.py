import string
thelist = list(string.ascii_lowercase)
print (thelist[-1])
result_index=[]
shift_index=[]
word=""
def encode_decode(word,shift,direction):
    for i in word:
        result_index.append(thelist.index(i))
    if direction=="dcode":
        shift=-shift
    for j in result_index:
        shift_index.append(j+shift)
        

            
encode_decode("wamik",1,2)
    

        


