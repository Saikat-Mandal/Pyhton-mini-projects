import random
import words

stages = ['''

    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
 ==========        

''',

'''

    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
 ==========        

''',

'''

    +---+
    |   |
    o   |
   /|\  |
        |
        |
 ==========        

''',
'''

    +---+
    |   |
    o   |
   /|   |
        |
        |
 ==========        

''',
'''

    +---+
    |   |
    o   |
    |   |
        |
        |
 ==========        

''',
'''

    +---+
    |   |
    o   |
        |
        |
        |
 ==========        

''',
'''

    +---+
    |   |
        |
        |
        |
        |
 ==========        

''',
]

wordsi = words.word_list
 
chosen_word = random.choice(wordsi)

display = ["_"]* len(chosen_word)
print(chosen_word)
print(display)
eof = False
lives = 6
while eof == False:
    guess = input("guess a letter: ")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            if(guess in display):
                print("already guessed")
            display[i] = guess
    if(guess not in chosen_word[i]):
        print("you guessed a wrong word , you loose a lyf")
        lives -= 1
        if(lives == 0):
            eof = True
            print("DED you loose")    
        

    print(display) 
    
    if("_" not in display):
        eof = True;
        print("you win mf !")       
    print( stages[lives])    