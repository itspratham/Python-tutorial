import smtplib

fromaddr = 'snsrajeshkumar@gmail.com'
to = 'runjeetprasad@gmail.com'
message = """
Hello, 
This is a sample message.

Best Regards
Rajesh
"""
try:
    smtpobj = smtplib.SMTP('smtp.gmail.com:587')
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.login(fromaddr, "put your password")
    smtpobj.sendmail(fromaddr, to, message)
    smtpobj.close()
    print("Email sent successfully")
except Exception as e:
    print(e)
