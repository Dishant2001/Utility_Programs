from email.mime import text
from src.yagmail import yagmail
from getpass import getpass
# from data_extract import getEmails
tup=getEmails('gfg')
# leads=['dishant.rathee@gmail.com','pranavkhatal0704@gmail.com']
# android=['dishant.rathee@gmail.com','pranavkhatal0704@gmail.com']
# design=['dishant.rathee@gmail.com','pranavkhatal0704@gmail.com']
# events=['dishant.rathee@gmail.com','pranavkhatal0704@gmail.com']
# community=[['dishant.rathee@gmail.com'],['pranavkhatal0704@gmail.com']]
# web=['dishant.rathee@gmail.com','pranavkhatal0704@gmail.com']
# tech=['dishant.rathee@gmail.com','pranavkhatal0704@gmail.com']
# spons=['dishant.rathee@gmail.com','pranavkhatal0704@gmail.com']
# pr=['dishant.rathee@gmail.com','pranavkhatal0704@gmail.com']
# leads=getEmails('leads')
# android=getEmails('android')
# design=getEmails('design')
# events=getEmails('events')
# community=getEmails('community')
# web=getEmails('web')
# tech=getEmails('tech')
# spons=getEmails('spons')
# pr=getEmails('pr')
# mohit=['mohitchandorkar841@gmail.com']
# shivani=['shivani.palve07@gmail.com']

# community=[['dishant.rathee@gmail.com'],['dishant.kumar@vit.edu.in']]
# recipients=[leads,android,design,events,mohit,shivani,web,tech,spons,pr]
# template={'Android.png':android,'Design.png':design,'Events.png':events,'GDSC Leads.png':leads,'Mohit GDSC VIT.png':mohit,'PR.png':pr,'Shivani GDSC VIT.png':shivani,'Spons.png':spons,'Tech.png':tech,'Web.png':web}


password=getpass(prompt='Password: ',stream=None)

# emails=['pranavkhatal0704@gmail.com','dishant.rathee@gmail.com']
# emails=['dishant.rathee@gmail.com','navita.budhwar@gmail.com']
# yag=yagmail.SMTP("dsc.vidyalankar@gmail.com", password)
yag=yagmail.SMTP("", password)
# for e in emails:
# subject='In the world of assorted mithai, you are our Kaju Katli 💛'
subject={'Android.png':'Driven by the gleam of Diyas onto the road of growth and success 🪔','Design.png':'Driven by the gleam of Diyas onto the road of growth and success 🪔','Events.png':'Driven by the gleam of Diyas onto the road of growth and success 🪔','GDSC Leads.png':'In the world of assorted mithai, you are our Kaju Katli 💛','Mohit GDSC VIT.png':'In the world of assorted mithai, you are our Kaju Katli 💛','PR.png':'Driven by the gleam of Diyas onto the road of growth and success 🪔','Shivani GDSC VIT.png':'In the world of assorted mithai, you are our Kaju Katli 💛','Spons.png':'Driven by the gleam of Diyas onto the road of growth and success 🪔','Tech.png':'Driven by the gleam of Diyas onto the road of growth and success 🪔','Web.png':'Driven by the gleam of Diyas onto the road of growth and success 🪔'}
# subject='Newest Mail 2'
# content=[yagmail.inline("HappyDiwali.png"),'Cracket it!! Yeahh!!']
html="""\
           <div style="#f2f2f2;line-height:normal;color:#3333cc;font-size:12px;font-style:'Cabin;">
<div>
  <img src="https://share1.cloudhq-mkt3.net/822aba24a328a3.png" style="width:100%" />
</div>
<div style="background-color:#4285F4;text-align:center;color:white;padding:5px;font-style:'Cabin';font-size:12px"><p style="margin:auto;">DSA is all that you need and we got you covered | Google DSC VIT Mumbai</p></div>

<p style="color:#3333cc;font-size:12px;font-style:'Cabin;"><strong>Hola Geek,</strong></p>
<p style="color:#3333cc;font-size:12px;font-style:'Cabin;">
&nbsp; &nbsp; &nbsp; &nbsp; We know that the key to crack interviews is having a good grasp of <strong>DSA</strong> and hence <strong>GDSC VIT</strong> along with <strong>GeeksforGeeks</strong> bring to you the most awaited session, <strong>The World of DSA</strong>. Gear up for an exemplary session on <strong>Data Structures and Algorithms</strong> and get all your doubts resolved from the course mentor <strong>Kirti Gera</strong>.
<p style="color:#3333cc;font-size:12px;font-style:'Cabin;"><strong>Date: 13th November</strong></p>
<p style="color:#3333cc;font-size:12px;font-style:'Cabin;"><strong>Time: 4:00 pm</strong></p>


<p style="color:#3333cc;font-size:12px;font-style:'Cabin;">What's in store for you?</p>
<ul style="color:#3333cc;font-size:12px;font-style:'Cabin;">
  <li>Strengthening your <strong>DSA</strong> skills</li>
  <li>Enhancing your <strong>problem-solving</strong> skills</li>
  <li>Live sessions</li>
  <li>Google test series</li>
  <li><strong>Tips and tricks</strong> to ace the domain</li>
  <li>A <strong>Certificate</strong> to prove your excellence</li>
</ul>

<p style="color:#3333cc;font-size:12px;font-style:'Cabin;">Not only this, but you have much more out there! Come, let's explore together. 🤩</p>
<p style="color:#3333cc;font-size:12px;font-style:'Cabin;">Register for the event and join the whatsapp group for further details!</p>

<div style="color:#3333cc;display:flex;padding-top:1em;padding-bottom:1em;">
  <div style="margin:auto">
    <a href="https://bit.ly/3qdqPEO" target="_blank"><button style="margin:auto;padding:0.7em;color:white;background-color:#2DC26B;background-color:rgb(45,194,107);border:none;border-radius:0.3em;font-style:'Cabin';font-size:12px">Register Here</button></a>
  </div>
  <div style="margin:auto">
  	<a href="https://bit.ly/3CQHcdH" target="_blank"><button style="margin:auto;padding:0.7em;color:white;background-color:#2DC26B;background-color:rgb(45,194,107);border:none;border-radius:0.3em;font-style:'Cabin';font-size:12px">Join WhatsApp Group</button></a>
  </div>
</div>
<p style="color:#3333cc;font-size:12px;font-style:'Cabin;">Stay connected with us on our social handles. See you there!</p>
<p style="color:#3333cc;text-align:right;font-size:12px;font-style:'Cabin';">Regards,</p>
<p style="color:#3333cc;text-align:right;font-size:12px;font-style:'Cabin';">Team <strong>Google DSC VIT</strong></p>
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
    """

# for k in template.keys():
#     emails=template[k]
#     content=[yagmail.inline('images/'+k)]
#     yag.send(emails,subject[k],content)
#     print("Mails sent to {}".format(k.split('.')[0]))

cont='''
Hey Developer,

Thank you for joining us at The World of DSA with Ms. Kirti Gera, course mentor at GeeksforGeeks. The session was truly inspiring and we hope you enjoyed it. Please find attached your certificate of participation. Stay connected with us for such exciting events!

We are a community of enthusiastic and passionate technophiles with the motive of upskilling and growing. Be a part of this amazing community by connecting with us on all our social handles. Join us to never miss any updates!✨

Instagram : https://www.instagram.com/gdsc.vit/
Linkedin : https://www.linkedin.com/company/gdsc-vit-mumbai/
Discord : https://discord.gg/9hqGRC9j9d
Youtube : https://www.youtube.com/channel/UCl93weektPDXfHC_sklxnrg
Twitter : https://twitter.com/gdsc_vit
Github : https://github.com/GoogleDscVit
'''
content=[cont]
# community=['dishant.rathee@gmail.com','bbegins555@gmail.com']
community=tup[0]
# names=['Dishant Kumar','Batman Begins']
names=tup[1]
# print(community)
# print(names)
community_subject='Certificate - GDSC VIT X GeeksforGeeks'
# attachments='images/Dishant Kumar_Certificate.png'
for ind,batch in enumerate(community):
  try:
    yag.send(batch,community_subject,content,attachments='images/'+names[ind]+'.png')
    if ind%10==0 and ind!=0:
      print('Mails sent to {} Students'.format(ind))
  except:
    print('{} {} has issue'.format(names[ind]))
