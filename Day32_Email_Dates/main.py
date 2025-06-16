##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import os
import email_module as em

today = dt.datetime.now()
df = pd.read_csv('Day32_Email_Dates/birthdays.csv')
letter_directory = "Day32_Email_Dates/letter_templates"
# Make a list of all template files in letter_templates directory
template_list = [f for f in os.listdir(letter_directory) if os.path.isfile(os.path.join(letter_directory, f))]


def create_message(name):
    # Pick a random letter template, replace [NAME] with the incoming name, return personalized text.
    letter = random.choice(template_list)
    with open(f'{letter_directory}/{letter}', 'r') as template_file:
        file_text = template_file.read()
        personal_text = file_text.replace('[NAME]', name)
        return personal_text
        
        
def email_happy_bday():
    for index, row in df.iterrows():
        if row['month'] == today.month and row['day'] == today.day:
            em.email_someone(to_email=row['email'], subject="Happy Birthday", message=create_message(row['name']))


if __name__ == "__main__":
    email_happy_bday()