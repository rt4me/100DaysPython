import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
#print(nato_dict.keys())


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_in = input("Enter a word to 'NATO-ize': ").upper()
# The below is what I came up with...and it worked but it could have all been done with one line (see below this section)
# letter_list = [letter for letter in word_in]
# nato_letter_list = []
# for letter in word_in:
#     nato_letter_list.extend(value for (key,value) in nato_dict.items() if letter.upper() == key)
#
# print(nato_letter_list)

output_list = [nato_dict[letter] for letter in word_in]
print(output_list)