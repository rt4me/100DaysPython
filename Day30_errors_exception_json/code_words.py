import pandas

try:
    data = pandas.read_csv("Day30_errors_exception_json/nato_phonetic_alphabet.csv")
except FileNotFoundError:
    print("Error: The specified file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
    
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def create_codeword():
    word = input("Enter a word: ").upper()
    output_list = []
    for letter in word:
        try:
            output_list.append(phonetic_dict[letter])
        except KeyError:
            print(f"Sorry, only letters in the alphabet please.")
            return create_codeword()  # Return the result of the recursive call
        except Exception as e:
            print(f"An unexpected error occurred during codeword creation: {e}")
            return create_codeword()
        else:
            return output_list    
        
        
print(create_codeword())