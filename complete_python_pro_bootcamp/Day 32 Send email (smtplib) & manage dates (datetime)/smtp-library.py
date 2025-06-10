import smtplib

my_email = 'kvn.education@gmail.com'
password = 'abcd1234()'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='kvn.education@gmail.com',
        msg='Hello\n\nThis is the body of my email.'
    )
