import random


numbers = ['0' , '1','2','3','4','5','6','7' , '8' , '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

print("welcome to the password generator!\n")

nLetters = int(input("How many letters you want ?\n"))
nNumbers = int(input("How many numbers you want ?\n"))
nSymbols = int(input("How many symbols you want ?\n"))


password =[]


for i in range(1, nLetters+1):
    password.append(random.choice(letters))
for i in range(1, nNumbers+1):
    password.append(random.choice(numbers))
for i in range(1, nSymbols+1):
    password.append(random.choice(symbols))



random.shuffle(password)


res = ""

for i in password:
    res +=i



print(f"your password is : {res}")
