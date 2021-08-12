def shift_encode(inString, inOffset):
    return "".join([chr(ord(x) + inOffset) for x in inString])
def shift_dcode(inString, inOffset):
    return "".join([chr(ord(x) - inOffset) for x in inString])
def encode():
    cypher_input=input("type encode to encrypt and decode to dcrypt: ")

    if cypher_input=="encode":
        encode_word=input("enter the word: ")
        encode_shift=int(input("enter the letter shift number: "))
        print(f"your encoded word is:{shift_encode(encode_word,encode_shift)}")
    elif cypher_input=="decode":
        dcode_word=input("enter the word: ")
        dcode_shift=int(input("enter the letter shift number: "))
        print(f"your dcoded word is:{shift_dcode(dcode_word,dcode_shift)}")
    else:
        print("please choose encode or dcode")
        encode()
encode()


