import hangman_art
import hangman_words
import random
print(hangman_art.logo)

random_word=hangman_words.word_list[random.randint(0,len(hangman_words.word_list)-1)]
word_list=[]
word_list=list(random_word)
len_word=len(word_list)
list_user=[]  
for i in random_word:
    list_user.append("_")
lives=7
while(lives>0):
    for i in list_user:
        print(i,end=" ")
    print("\n\n")
    user_guess=input("Guess a letter: ")
    
    if(user_guess in list_user):
        print("you have already guessed it. Try a separate letter")
    
    elif(user_guess in word_list):
        ind=[]
        for i in range(0,len(word_list)):
            if(word_list[i]==user_guess):
                ind.append(i)
        for i in ind:
            list_user[i]=user_guess            
    else:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        print(hangman_art.stages[lives-1])
        lives-=1
        
    if(list_user==word_list):
        print("You win!")
        break;
    
    if(lives==0):
        print(f"You lose. Lives over. Try again! The word was: {random_word}")
        break;    
