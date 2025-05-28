import pandas

# Keyword Method with iterrows()
data = pandas.read_csv('nato_phonetic_alphabet.csv')
print(data.to_dict())

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print('PHONETIC DICTIONARY', phonetic_dictionary)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input('Enter a word: ').upper()
    try:
        output_list = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print('OUTPUT LIST', output_list)

generate_phonetic()