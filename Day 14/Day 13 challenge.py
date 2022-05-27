import art
import game_data
import random
import os


clear= lambda: os.system('clear')
def more_followers(celeb_A,celeb_B):
    if(celeb_A['follower_count']>celeb_B['follower_count']):
        return 0
    else:
        return 1
def high_lower_game():
    print(art.logo)
    celeb_A=random.choice(game_data.data)
    flag=True
    score=0
    while(flag):
        celeb_B=random.choice(game_data.data)
        while(celeb_A==celeb_B):
            celeb_B=random.choice(game_data.data)
        print(f"Compare A: {celeb_A['name']} , a {celeb_A['description']} from {celeb_A['country']}.")
        print(art.vs)
        print(f"Against B: {celeb_B['name']} , a {celeb_B['description']} from {celeb_B['country']}.")
        choice=input("Who has more followers? Type 'A' or 'B': ")
        x=more_followers(celeb_A,celeb_B)
        if((x==0 and choice=='A') or (x==1 and choice=='B') ):
            celeb_A=celeb_B
            score+=1
            clear()
            print(art.logo)
            print(f"You're right! Current score: {score}")
        elif(x==1 and choice=='A') or (x==0 and choice=='B'):
            flag=False
            clear()
        if flag == False:
            print(F"Sorry, that's wrong. Final score: {score}")
            return 0
            
            

high_lower_game()