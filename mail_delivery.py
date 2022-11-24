import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

server = 'smtp.mail.ru'
user = 'Luhnikov2000@mail.ru'
password = 'fabyf4444'

#содержание письма
recipients = ["radikal2@mail.ru"]
sender = 'Luhnikov2000@mail.ru'
subject = "Уведомление"
text = """Здравствуйте. 
<p>Уведомляю вас, что на этой и следующей неделе занятий не будет.
<p>С уважением,  Ирина Савостьянова. 
"""
html = '<html><head></head><body><p>' + text + '</p></body></html>'

#файл
#filepath = ""
#basename = os.path.basename(filepath)
#filesize = os.path.getsize(filepath)

#формируем письмо
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = 'Ирина Савостьянова <' + sender + '>'
msg['To'] = ', '.join(recipients)
msg['Reply-To'] = sender
msg['Return-Path'] = sender
msg['X-Mailer'] = 'Python/' + (python_version())

#контент письма
part_text = MIMEText(text, 'plain')
part_html = MIMEText(html, 'html')
#part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
#part_file.set_payload(open(filepath, "rb").read())
#part_file.add_header('Content-Description', basename)
#part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
#encoders.encode_base64(part_file)

msg.attach(part_text)
msg.attach(part_html)
#msg.attach(part_file)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(sender, recipients, msg.as_string())
mail.quit()