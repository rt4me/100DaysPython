#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode = "r") as name_list:
    list_of_names = name_list.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()

for name in list_of_names:
    custom_letter = letter_text.replace("[name]", name.strip())
    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode = 'w') as output_letter:
        output_letter.write(custom_letter)
