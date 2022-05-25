import os
import art
print(art.logo)
clear = lambda: os.system('clear')
bidders=True
bidders_dict={}
def check_highestbidder(dictionary):
    highest_bid=0
    highest_bidder=""
    for key in dictionary:
         if(dictionary[key]>highest_bid):
            highest_bid=dictionary[key]
            highest_bidder=key
    print(f"The winner is {highest_bidder} with a bid of $ {bidders_dict[highest_bidder]}")     


while(bidders):
    name=input("What is your name?: ")
    bid= int(input("What is your bid? $"))
    bidders_dict[name]=bid
    again=input("Are there any other bidders? Type 'yes or 'no'.: ")
    clear()
    if(again=="no"):
        bidders=False
        check_highestbidder(bidders_dict)
                


