import art
import random
import os
clear = lambda: os.system('clear')
print(art.logo)

def num_random():
    return random.randint(1,100)

def check_number(number):
    guess_number=int(input("Make a guess: "))
    if(number-guess_number>0):
        print("Too low. Try again!")
        return False
    elif(number-guess_number<0):
        print("Too high. Try again!")
        return False
    else:
        print(f"Yes, the correct number was {number}")
        return True      
    
def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number=num_random()
    flag=True
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if(difficulty=='easy'):
        lives=10                             
    elif(difficulty=="hard"):
        lives=5                
    else:
        print("Wrong input. Try again")
        return 0      
    while(flag):
        print(f"You have {lives} attempts remaining to guess the number.")
        if(check_number(number)==False):
            lives-=1
        else:
            flag=False
        if(lives==0): 
            print("Sorry, you are out of lives. Try again! ") 
            flag=False
   
guess_number()