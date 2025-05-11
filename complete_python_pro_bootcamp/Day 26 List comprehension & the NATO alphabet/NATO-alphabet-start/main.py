import pandas

# Keyword Method with iterrows()
data = pandas.read_csv('nato_phonetic_alphabet.csv')
print(data.to_dict())

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print('PHONETIC DICTIONARY', phonetic_dictionary)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word: ').upper()
output_list = [phonetic_dictionary[letter] for letter in word]
print('OUTPUT LIST', output_list)

