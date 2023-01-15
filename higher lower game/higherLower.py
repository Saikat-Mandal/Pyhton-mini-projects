import random
import logo_data
from game_data import data


# returns random account 
def random_account():
    return random.choice(data)



def format(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name} , {description} , {country} country"


def isValid(guess , account_a_followers , account_b_followers):
    if(account_a_followers > account_b_followers):
        return guess == 'a'
    else:
        return guess == 'b'    




def play():
    print(logo_data.logo)
    score = 0
    flag = True
    account_a = random_account()
    account_b = random_account()
    while flag:
        account_a = account_b
        account_b = random_account()    

        print(format(account_a))
        print(logo_data.vs)
        print(format(account_b))

        guess = input("Enter 'A' or 'B'").lower()
        account_a_followers = account_a['follower_count']
        account_b_followers = account_b['follower_count']

        correct = isValid(guess , account_a_followers , account_b_followers)

        print(logo_data.logo)
        if correct:
            score += 1
            print(f"your score is {score}")
        else:
            flag = False
            print(f"Wrong answer , your score is {score}")    

play()




