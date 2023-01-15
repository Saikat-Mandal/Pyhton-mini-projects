import random


def guessing(lives):
    flag = True
    while flag:
        guess = int(input("Guess a number between 1 to 100\n"))
        if lives == 0:
            print("All lives lost , You loose!\n") 
            flag = False 
        elif guess > num:
            lives -= 1
            print(f"you have {lives} lives left\n")
            print("Choose a lower value !\n")
        elif guess < num:
            print(f"you have {lives} lives left\n")
            lives -= 1
            print("Choose a higher value !\n") 
        elif guess == num:
            print("Nice you won ! \n")
            flag = False    

num = random.randint(1,101)

count_easy = 10
count_hard = 5

level = input("Choose a level -> 'hard' or 'easy'\n")
if level == "hard":
    guessing(count_hard)
else:
     guessing(count_easy)

  
