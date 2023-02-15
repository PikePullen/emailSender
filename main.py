import smtplib

password = "eltmghapflrjamra"

sender = "ppulleniv@gmail.com"
receivers =["pppullen@gmail.com","ppulleniv@hotmail.com","pike@cloudmasonry.com"]
message = "Subject:Hello Python Email Test\n\nThis is the body of the email."

# if you write it this way, dont have to close connection
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(from_addr=sender,
                        to_addrs=receivers,
                        msg=message)
