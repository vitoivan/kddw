import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask
from os import environ

# S M T P - Simple Mail Transfer protocol

def construct_email(to, subject, body):

	email_msg = MIMEMultipart()
	email_msg['from'] = environ.get('MAIL_FROM') 
	email_msg['to'] = to 
	email_msg['subject'] = subject 
	email_msg.attach(MIMEText(body, 'html'))	
	return email_msg

def create_sendMail_function():

	def send_mail(to, subject, body):
		host = environ.get('MAIL_HOST')
		login = environ.get('MAIL_LOGIN')
		port = environ.get('MAIL_PORT')
		password = environ.get('MAIL_PASSWD')
		# init server
		server = smtplib.SMTP(host, port)

		server.starttls()
		server.login(login, password)
		email = construct_email(to, subject, body)
		server.sendmail(email['from'], email['to'], email.as_string())
		server.quit()

	return send_mail

def init_app(app: Flask):
	app.sendMail = create_sendMail_function() 
