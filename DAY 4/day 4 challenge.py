import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
input_user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
choice=[rock,paper,scissors]
user_choice=choice[input_user]
print(user_choice)
print("Computer chose:")
computer_choice=random.randint(0,2)
print(choice[computer_choice])
if(input_user==computer_choice):
    print("It's a draw")
elif(input_user==0 and computer_choice==1) or (input_user==2 and computer_choice==0) or (input_user==1 and computer_choice==2):
    print("You lose")
else:
    print("You win!")







