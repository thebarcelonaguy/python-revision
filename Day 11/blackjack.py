import art
import random
def input_cards(list_cards,card):
    list_cards.append(card)   
       
def sum_cards(list_cards):
    if(11 in list_cards and sum(list_cards)>21):
        list_cards.append(1)
        list_cards.remove(11)
    
    return sum(list_cards)

def computer_final_cards(computer_cards):
    while(sum_cards(computer_cards)<=16):
        input_cards(computer_cards,cards[random.randint(0,12)])  
    return computer_cards

def game_over_check(user_cards,computer_cards):
    if(sum_cards(user_cards)>21):
        return True
    else:
        return False
def print_cards(user_cards,computer_cards):
    print(f"Your cards: {user_cards}, current score: {sum_cards(user_cards)}" )
    print(f"Computer's first card: {computer_cards[0]}")
        

def final_check(user_cards,computer_cards):
    print(f"Your final hand: {user_cards}, final score: {sum_cards(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum_cards(computer_cards)}")
    if(sum_cards(user_cards)==21 and sum_cards(computer_cards)==21):
        print("One in a million. Both you and computer got a blackjack. Draw") 
    elif(sum_cards(user_cards)==21):
        print("you win the game with a perfect blackjack")
    elif(sum_cards(user_cards)>21):
        print("You lost the game. You went way over.")
    elif(sum_cards(computer_cards)>21):
        print("You won the game. Computer went way over.")
    elif(sum_cards(user_cards)==sum_cards(computer_cards)):
        print("It is a draw")
    elif(sum_cards(user_cards)>sum_cards(computer_cards)):
        print("You won the game.")
    else:
        print("You lost the game.")

game=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
if(game=='y'):
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    input_cards(user_cards,random.choice(cards))
    input_cards(user_cards,random.choice(cards))
    input_cards(computer_cards,random.choice(cards))
    flag=True
    if(sum_cards(user_cards)==21):
        computer_final_cards(computer_cards)
        final_check(user_cards,computer_cards)
        flag=False        
    while(flag):
        print_cards(user_cards,computer_cards)
        if(game_over_check(user_cards,computer_cards)==False):
            another_card=input("Type 'y' to get another card, type 'n' to pass: ")
            if(another_card=='y'):
                input_cards(user_cards,random.choice(cards))
            else:
                computer_final_cards(computer_cards)
                flag=False
                final_check(user_cards,computer_cards)   
        else:
            computer_final_cards(computer_cards)
            flag=False  
            final_check(user_cards,computer_cards)          
        

