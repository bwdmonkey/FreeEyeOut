from decouple import config, Csv
import smtplib
import sys


class Mailer():
	def __init__(self, course, url, to_emails):
		self.course = course
		self.url = url
		self.to_emails = to_emails
		pass

	def alert(self):
		FROM = config("EMAIL_HOST_USER")
		TO_LIST = self.to_emails
		TO_STRING = ", ".join(TO_LIST)
		SUBJECT = "%s has free seats!" % self.course
		TEXT = "%s\n\n%s" % (SUBJECT, self.url)

		message = """From: %s\nTo: %s\nSubject: %s\n\n%s
		""" % (FROM, TO_STRING, SUBJECT, TEXT)
		try:
			email_host = config("EMAIL_HOST", default="smtp.gmail.com")
			email_host_user = config("EMAIL_HOST_USER")
			email_host_pwd = config("EMAIL_HOST_PASSWORD")

			server = smtplib.SMTP(email_host, 587)
			server.ehlo()
			server.starttls()
			server.login(email_host_user, email_host_pwd)
			server.sendmail(FROM, TO_LIST, message)
			server.close()
			print("Successfully sent the mail to %s about %s" % (TO_STRING, self.course))
		except:
			print("Failed to send mail to %s about %s" % (TO_STRING, self.course))
			print("Unexpected error:", sys.exc_info()[0])
