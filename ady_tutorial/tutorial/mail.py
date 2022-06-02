#################################
# from email import message
# import smtplib

# # create SMTP session

# sm = smtplib.SMTP('smtp.gmail.com', 587)
# sm.starttls()

# sm.login('s.pentaho@gmail.com', 'sigma@123')

# message = "Hello Adyant . welcome to the Tutorial Program"

# sm.sendmail('s.pentaho@gmail.com', ['harishsen0609@gmail.com', 'adyant.org@gmail.com'], message)

# sm.quit()
##############################################


from email.message import EmailMessage 
import smtplib

def notify():
    # create SMTP session

    msg = EmailMessage()
    msg.set_content("Hello Adyant . welcome to the Tutorial Program")

    msg['Subject'] = 'Welcome from Adyant'
    msg['From'] = "s.pentaho@gmail.com"
    msg['To'] = ['harishsen0609@gmail.com', 'adyant.org@gmail.com']

    sm = smtplib.SMTP('smtp.gmail.com', 587)
    sm.starttls()

    sm.login('s.pentaho@gmail.com', 'sigma@123')

    sm.send_message(msg)

    sm.quit()