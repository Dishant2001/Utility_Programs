from __future__ import absolute_import
import yagmail
yag=yagmail.SMTP()

content=[yagmail.inline("Diwali Leads.png")]
yagmail.send('dishant.rathee@gmail.com','Trial mail',content)