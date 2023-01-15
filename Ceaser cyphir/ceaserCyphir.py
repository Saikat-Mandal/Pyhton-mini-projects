alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 't', 'z' ]

def ceaser(text , shift , code):
    res = ""
    if code == "decode":
        shift *= -1        
    for letter in text:
        if(letter in alphabets):
            position = alphabets.index(letter)
            new_position = (position +shift)% len(alphabets)
            res += alphabets[new_position]
        else:
            res+=letter    
    print(res)

    
should = True

while(should):

    direction = input("Type 'encode' to encrypt and 'decode' to decrypt :\n")
    text = input("Type the message :\n").lower()
    shift = int(input("Type the amount to shifted :\n"))

    ceaser(text , shift , code=direction)
    val= input("do you wanna go again ?\n")
    if(val == "no"):
        should = False
        print("bye mf")




       
            
        