import smtplib

from PyQt5.QtWidgets import QApplication, QFileDialog

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

from email import encoders

print("**WELCOME TO PYMAIL**")
print("==Send an email==")
print("-----------------")

fromaddr = 'aswinnbijuu@gmail.com'
message = input("Please enter your message below\n>")
toaddr = input("To:")
subject = input("Enter your subject:")
password = 'melv ytkf rbmw btst'

multi_ = MIMEMultipart()

multi_['From'] = fromaddr

multi_['To'] = toaddr

multi_['Subject'] = subject

html_msg = f'''<html>
<body>
<h2>{message}</h2>
</body>
</html>'''

multi_.attach(MIMEText(html_msg, 'html'))

if_attach = input("Would you like to attach files?(yes/no):")
if if_attach.startswith("y"):
    app = QApplication([])

    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    while True:
        if file_dialog.exec_() == QFileDialog.Accepted:
            file = file_dialog.selectedFiles()[0]
            rev_file = file[::-1]
            ind = rev_file.find("/")
            rev_file = rev_file[:ind:]
            filename = rev_file[::-1]
            attach = open(file, 'rb')
            base = MIMEBase('application', 'octet-stream')
            base.set_payload(attach.read())
            encoders.encode_base64(base)
            base.add_header('Content-disposition', 'attachment;filename=%s'%filename)
            multi_.attach(base)
            print("email sent succesfully!")
            break
        else:
            print("file selection cancelled")
            op = input("Would you still want to attach files?(yes/no):")
            if op:
                continue
            else:
                break

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromaddr, password)

msg = multi_.as_string()

s.sendmail(fromaddr, toaddr, msg)

s.close()