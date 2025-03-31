
import pandas

#TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(type(data))
NATO_dict = { row.letter: row.code for index, row in data.iterrows()}

print(NATO_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_Correct_Input = True

while is_Correct_Input:
    try:
        user_input = input("Enter your word: ").upper()
        user_input_list = list(user_input)
        phonetic_code_list = [NATO_dict[letter] for letter in user_input_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_Correct_Input = False
print(phonetic_code_list)
