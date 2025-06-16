import smtplib

# tb_test@myyahoo.com ; smtp.mail.yahoo.com
# berginVM@gmail.com ; smtp.gmail.com

my_email = "berginVM@gmail.com"
password = 'xxmd aaht tpgs ysor'

def email_someone(to_email, subject, message):
    print(f"Running email_someone to {to_email} about {message}")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(from_addr = my_email, 
                            to_addrs = to_email, 
                            msg = f"Subject:{subject}\n\n{message}"   # msg format: msg="Subject:Thanks\n\nThanks for you email!"
                            )


# my_email2 = "tb_test@myyahoo.com"
# password2 = ''  #Was unable to create password at time of configuration

# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user = my_email2, password = password2)
#     connection.sendmail(from_addr = my_email2, 
#                         to_addrs = 'berginVM@gmail.com', 
#                         msg="Subject:Thanks\n\nThanks for you email!"
#                         )
