from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text,shift):
    encoded_text=""
    for letter in text:
        if letter in alphabet:
            index=alphabet.index(letter)  
            new_index=index+shift
            encoded_text+=alphabet[new_index]
        else:
            encoded_text+=letter
    
    print(f"The encoded text is {encoded_text}")

def decrypt(text,shift):
    decoded_text=""
    for letter in text:
        if letter in alphabet:
            index=alphabet.index(letter)
            new_index=index-shift
            decoded_text+=alphabet[new_index]
        else:
            decoded_text+=letter
    
    print(f"The encoded text is {decoded_text}")

user_yes=True

while(user_yes):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    if(direction=="encode"):
        encrypt(text,shift)
    else:
        decrypt(text,shift)
    
    again=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if(again=="no"):
        user_yes=False