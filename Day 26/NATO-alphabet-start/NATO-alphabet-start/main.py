import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}
new_df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_key = {row["letter"]: row["code"] for (index, row) in new_df.iterrows()}
user_string = input("Enter a word: ").upper()
phonetic_alphabet_user = [dict_key[x] for x in user_string]
print(phonetic_alphabet_user)
