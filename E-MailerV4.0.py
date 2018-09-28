import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sendingAttatchment = "Y"
sendanotheremail = "N"
recipient = []
filename = []
for i in range(1,20):
    recipient.append("X")
for i in range(1,20):
    recipient.append("X")

print("Please enter your E-Mail.")
username = input()
print()
print("Please enter your password.")
password = getpass.getpass()
print()
print("Please enter the recipient's e-mail.")
recipient[0] = input()
print()
print("Would you like to send this to another E-mail? (Y or N)")
sendanotheremail = input()

for i in range(1,19):
    if(sendanotheremail == "Y" or sendanotheremail == "y" or sendanotheremail == "Yes" or sendanotheremail == "yes"):
        print()
        print("Please enter the recipient's e-mail.")
        recipient[i] = input()
        print()
        print("Would you like to send this to another E-mail? (Y or N)")
        sendanotheremail = input()

print()
print("Please enter your subject.")
subject = input()
print()
print("Please enter your message.")
message = input()
print()
print("Do you want to add an attachment? (Enter Y or N) Note that if the file size(s) are too big, the message may not send.")
sendingAttatchment = input()
print()

for i in range(0,19):
    if(sendingAttatchment == "Y" or sendingAttatchment == "y" or sendingAttatchment == "Yes" or sendingAttatchment == "yes"):
        print('Please enter the filename (With the extension). Make sure it it in the same directory as this program.')
        filename[i] = input()
        print()
        print('Would you like to send another attachment? Enter Y or N')
        sendingAttatchment = input()
        print()

msg = MIMEMultipart()

if (sendingAttatchment == "Y" or sendingAttatchment == "y" or sendingAttatchment == "Yes" or sendingAttatchment == "yes"):
    for i in range(0,19):
        if (filename[i] != "X"):
            attachment = open(filename[i],'rb')
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+filename)
            msg.attach(part)

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(username, password)

for i in range(0,19):
    if (recipient[i] != "X"):
        msg['From'] = username
        msg['To'] = recipient[i]
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        text = msg.as_string()

        server.sendmail(username, recipient[i], text)
    
server.quit()
print()
print("Message Sent!")
print()
end = input("Press enter to continue...")
