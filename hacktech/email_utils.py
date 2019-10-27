import smtplib
from email.mime.text import MIMEText
from hacktech import config

def send_email(to, msg, subject, use_prefix=True):
    """
  Sends an email to a user. Expects 'to' to be a comma separated string of
  emails, and for 'msg' and 'subject' to be strings.
  """
    msg = MIMEText(msg)

    if use_prefix:
        subject = '[Hacktech]' + subject

    msg['Subject'] = subject
    msg['From'] = 'auto@hacktech.io'
    msg['To'] = to

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.ehlo()
    environment = config.DEV
    server.login(environment.email, environment.em)
    server.sendmail('auto@hacktech.io', [to], msg.as_string())
    server.quit()
