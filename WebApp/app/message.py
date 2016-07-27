from flask import render_template, request, redirect
from app import app
import smtplib
from user import User
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import config

def send_confirmation_email_for_user(user):

    link = "http://127.0.0.1:5000/email_confirmation_form?token=" + user.email_confirmation_token
    smtp = smtplib.SMTP(config.MAIL_SERVER)
    smtp.starttls()
    smtp.login(config.MAIL_USERNAME, config.MAIL_PASSWORD)

    # me == my email address
    # you == recipient's email address
    sender = 'likedan5@gmail.com'
    recipient = user.email

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Confirmation Email"
    msg['From'] = sender
    msg['To'] = recipient

    # Create the body of the message (a plain-text and an HTML version).
    text = "Dear "+user.full_name+",\nWelcome to join us.\n" + link

#     html = '''
#     <html>
#       <head></head>
#       <body>
# <form action="'''+link+'''" method="POST">
#   <input type="hidden" name="email" value="'''+user.email+'''">
#   <input type="hidden" name="token" value="'''+user.email_confirmation_token+'''">
#   <input type="submit" value="Submit">
# </form>
#       </body>
#     </html>
#     '''
    print text
    # html = '''
    # <html>
    #   <head></head>
    #   <body>
    #   <a href="''' + link + '''">
    #   Confirm
    #  </a>
    #   </body>
    # </html>
    # '''
    # print html
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    # part2 = MIMEText(html, 'html')

    msg.attach(part1)
    # msg.attach(part2)

    try:
        smtp.sendmail(sender, recipient, msg.as_string())      
        print "Successfully sent email"
    except SMTPException:
        print "Error: unable to send email"