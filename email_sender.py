import smtplib, ssl
from getpass import getpass

port = 465  # For SSL
sender_email='dishant.rathee@gmail.com'
# receiver_email=['dishant.rathee@gmail.com','dishant2001.rathee@gmail.com','dishant2001.kumar@gmail.com','bbegins555@gmail.com']
receiver_email=['pranavkhatal0704@gmail.com','dishant.rathee@gmail.com']
emojis=['💛','😎','❤️💚💛💙']
message = """\
Subject: In the world of assorted mithai, you are our kaju katli {}

This Diwali let there be blasts of the laughter with your dear ones rather than crackers
May the gleam of auspicious Diyas lead you onto the road of growth and success!
We hope you take some time for yourself to celebrate with your family and come back with loads of energy {}

Wishing all our dynamic Leads and Co-Leads a very Happy Diwali! 
Thank you for being a part of GDSC!
{}

Warm Regards,
Pranav Khatal
""".format(emojis[0],emojis[1],emojis[2])
print(message)
print(emojis[0])

# Send email here
password = input("Type your password and press enter: ")
password=getpass(prompt='Password: ',stream=None)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("dishant.rathee@gmail.com", password)
    # TODO: Send email here
    for e in receiver_email:
        server.sendmail(sender_email, e, message)