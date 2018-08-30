from decouple import config, Csv
import smtplib


class Mailer():
	def __init__(self, course, url):
		self.course = course
		self.url = url
		pass

	def alert(self):
		FROM = config("EMAIL_HOST_USER")
		TO = config("TEMP_TO_EMAIL", cast=Csv())
		SUBJECT = "%s has free seats!" % self.course
		TEXT = "%s\n\n%s" % (SUBJECT, self.url)

		message = """From: %s\nTo: %s\nSubject: %s\n\n%s
		""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
		try:
			email_host = config("EMAIL_HOST", default="smtp.gmail.com")
			email_host_user = config("EMAIL_HOST_USER")
			email_host_pwd = config("EMAIL_HOST_PASSWORD")

			server = smtplib.SMTP(email_host, 587)
			server.ehlo()
			server.starttls()
			server.login(email_host_user, email_host_pwd)
			server.sendmail(FROM, TO, message)
			server.close()
			print "Successfully sent the mail to %s about %s" % (TO, self.course)
		except:
			print "Failed to send mail to %s about %s" % (TO, self.course)
