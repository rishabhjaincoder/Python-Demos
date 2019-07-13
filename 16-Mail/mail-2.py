#SMTP
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Create Message
msg = MIMEMultipart()
msg['Subject']="Account Created Successfully"
msg['CC']='amit2881988@gmail.com;rishabhjain.rdps@gmail.com'

#Body Attachment
body = '''
    <html>
        <body>
            <h1>Hello User</h1>
            <p>Your account is now ready to use</p>
        </body>
    </html>
'''
msg.attach(MIMEText(body, 'html'))


#File Attachment
filename="aakash.png"
file=open(filename,"rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((file).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename="+filename)
msg.attach(part)

#File Attachment
filename="aakash.txt"
file=open(filename,"rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((file).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)


smtp=smtplib.SMTP('smtp.gmail.com',587)
smtp.ehlo()
smtp.starttls()
smtp.login("niecspi","*Uncommon##")
sender= "niecspi@gmail.com"
body=msg.as_string()
receiver="amit2881988@gmail.com;"
try:
    smtp.sendmail(sender,receiver,body)
    print("Email Sent Successfully")
except:
    print("Coudln't Send Email")


