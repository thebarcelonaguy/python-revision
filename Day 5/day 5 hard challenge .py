#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for l in range(0,nr_letters):
    ran_letter_index=random.randint(0,25)
    ran_letter=letters[ran_letter_index]
    password.append(ran_letter)

for s in range(0,nr_symbols):
    ran_sym_index=random.randint(0,len(symbols)-1)
    ran_symbol=symbols[ran_sym_index]
    password.append(ran_symbol) 

for n in range(0, nr_numbers):
    ran_num_index=random.randint(0,len(numbers)-1)
    ran_number=numbers[ran_num_index]
    password.append(ran_number)

print(password)
random.shuffle(password)
print(password)
final_pass=""
for i in password:
    final_pass+=i

print(f"Your password is {final_pass}")
