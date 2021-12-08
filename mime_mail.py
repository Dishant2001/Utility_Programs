import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from getpass import getpass
# from data_extract import getEmails

sender_email = "dsc.vidyalankar@gmail.com"
password=getpass(prompt='Password: ',stream=None)
# message["Cc"]=cc

text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

html="""\
  <html>
  <body>
<div style="#f2f2f2;line-height:normal;font-size:12px;font-style:'Cabin;">
<div>
  <img src="https://share1.cloudhq-mkt3.net/822aba24a328a3.png" style="width:100%" />
</div>
<div style="background-color:#4285F4;text-align:center;color:white;padding:5px;font-style:'Cabin';font-size:12px"><p style="margin:auto;">DSA is all that you need and we got you covered | Google DSC VIT Mumbai</p></div>

<p style="font-size:12px;font-style:'Cabin;"><strong>Hola Geek,</strong></p>
<p style="font-size:12px;font-style:'Cabin;">
&nbsp; &nbsp; &nbsp; &nbsp; We know that the key to crack interviews is having a good grasp of <strong>DSA</strong> and hence <strong>GDSC VIT</strong> along with <strong>GeeksforGeeks</strong> bring to you the most awaited session, <strong>The World of DSA</strong>. Gear up for an exemplary session on <strong>Data Structures and Algorithms</strong> and get all your doubts resolved from the course mentor <strong>Kirti Gera</strong>.
<p style="font-size:12px;font-style:'Cabin;"><strong>Date: 13th November</strong></p>
<p style="font-size:12px;font-style:'Cabin;"><strong>Time: 4:00 pm</strong></p>


<p style="font-size:12px;font-style:'Cabin;">What's in store for you?</p>
<ul style="font-size:12px;font-style:'Cabin;">
  <li>Strengthening your <strong>DSA</strong> skills</li>
  <li>Enhancing your <strong>problem-solving</strong> skills</li>
  <li>Live sessions</li>
  <li>Google test series</li>
  <li><strong>Tips and tricks</strong> to ace the domain</li>
  <li>A <strong>Certificate</strong> to prove your excellence</li>
</ul>

<p style="font-size:12px;font-style:'Cabin;">Not only this, but you have much more out there! Come, let's explore together. 🤩</p>
<p style="font-size:12px;font-style:'Cabin;">Register for the event and join the whatsapp group for further details!</p>

<div style="display:flex;padding-top:1em;padding-bottom:1em;">
  <div style="margin:auto">
    <a href="https://bit.ly/3qdqPEO" target="_blank"><button style="width:12em;margin:auto;padding:0.7em;color:white;background-color:#2DC26B;background-color:rgb(45,194,107);border:none;border-radius:0.3em;font-style:'Cabin';font-size:12px">Register Here</button></a>
  </div>
  <div style="margin:auto">
  	<a href="https://bit.ly/3CQHcdH" target="_blank"><button style="width:12em;margin:auto;padding:0.7em;color:white;background-color:#2DC26B;background-color:rgb(45,194,107);border:none;border-radius:0.3em;font-style:'Cabin';font-size:12px">Join WhatsApp Group</button></a>
  </div>
</div>
<p style="font-size:12px;font-style:'Cabin;">Stay connected with us on our social handles. See you there!</p>
<p style="text-align:right;font-size:12px;font-style:'Cabin';">Regards,</p>
<p style="text-align:right;font-size:12px;font-style:'Cabin';">Team <strong>Google DSC VIT</strong></p>
<div style="background-color:#002266;padding-top:9px;">
  <div style="display:block;background-color:#b3b3b3;width:96%;height:0.012em;margin-top:0.1em;margin-left:auto;margin-right:auto;"></div>
  <div style="display:flex;padding-top:1em;padding-bottom:1em">
    <div style="margin:auto;width:50%;display:flex">
    	<img style="width:60%;margin:auto" src="https://share1.cloudhq-mkt3.net/1a892fe9b4495b.png" />
    </div>
    <div style="margin:auto;display:flex;width:50%;text-align:center;">
      <a href="https://instagram.com/gdsc.vit" style="margin-left:auto"><img style="margin:auto;" src="https://img.icons8.com/color/36/000000/instagram-new.png"/></a>
      <a href="https://www.linkedin.com/company/gdsc-vit-mumbai/" style="margin:auto"><img style="margin:auto;" src="https://img.icons8.com/fluency/36/000000/linkedin.png"/></a>
      <a href="https://discord.com/invite/9hqGRC9j9d" style="margin-right:auto"><img style="margin:auto;" src="https://img.icons8.com/color/36/000000/discord-new-logo.png"/></a>
    </div>
  </div>
	<div style="display:block;text-align:center;font-size:0.7em;background-color:#00284d;color:white;padding:5px;">All Rights Reserved © GDSC VIT 2021</div>
</div>
</div>
</body>
</html>
  """

# records=[['dishant.rathee@gmail.com','sonalibedade15@gmail.com'],['dishant2001.kumar@gmail.com','dishant.kumar@vit.edu.in'],['bbegins555@gmail.com']]
records=getEmails('all_mails')
for ind,batch in enumerate(records):
# receiver_email = ['dishant.rathee@gmail.com','dishant2001.kumar@gmail.com','bbegins555@gmail.com','dishant.kumar@vit.edu.in','disrat1998@gmail.com','navita.budhwar@gmail.com','devansh.rathee10@gmail.com']
# cc='dishant2001.rathee@gmail.com,bbegins555@gmail.com,dishant.kumar@vit.edu.in'
# receiver_email=['pranavkhatal0704@gmail.com','dishant.rathee@gmail.com']

  message = MIMEMultipart("alternative")
  message["Subject"] = "GDSC VIT x GEEKSforGEEKS | The World of DSA"
  message["From"] = sender_email
  message["To"] = ', '.join(batch).lower()

  # Turn these into plain/html MIMEText objects
  # part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  # message.attach(part1)
  message.attach(part2)
  # message.add_header('Happy Diwali', '<image1>')
  # message['Content-Disposition'] = f'inline; filename=image1.png'
  # message.attach(img)
  # print(message.keys())


  # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, batch, message.as_string()
      )
  print('{} Mails sent in Batch {}'.format(len(batch),ind+1))