import datetime as dt
import email_module as em
import random


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() # returns a number, with 0 being Monday

date_of_birth = dt.datetime(year= 1972, month = 10, day = 31)

# print(day_of_week)
# print(date_of_birth)

def get_phrase():
    with open('Day32_Email_Dates/quotes.txt', 'r') as file:
        quote_list = file.readlines()
        print(f"3rd entry on file is: {quote_list[2]}")
        return random.choice(quote_list)

# Send an email every Monday with a motivational message pulled from quotes.txt
if now.weekday() == 6:
    em.email_someone(to_email = 'tb_test@myyahoo.com', subject= "Buck Up!", message = get_phrase())
    print("Email sent")