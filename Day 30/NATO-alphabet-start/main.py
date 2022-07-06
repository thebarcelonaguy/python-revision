import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}
new_df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_key = {row["letter"]: row["code"] for (index, row) in new_df.iterrows()}
is_error=True
while is_error:
    try:
        user_string = input("Enter a word: ").upper()
        phonetic_alphabet_user = [dict_key[x] for x in user_string]
    except KeyError:
        print("Sorry only letters in the alphabet please")
    else:
        print(phonetic_alphabet_user)
        is_error=False
